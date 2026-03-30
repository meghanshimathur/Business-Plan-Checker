
import os
import streamlit as st
import PyPDF2

from dotenv import load_dotenv, find_dotenv
from groq import Groq
load_dotenv(find_dotenv())




api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

#---------------------------------------------------------------------------------
def split_into_chunks(text, chunk_size=1800):
    chunks = []
    words = text.split()
    current_chunk = []
    current_length = 0
    
    for word in words:
        current_length += len(word) + 1
        if current_length > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(word)

    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

#------------------------------------------------------------------------------------------
def extract_pdf_text(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

#---------------------------------------------------------------------

def ask_groq(chunk, question):
    prompt = f"""
You are a startup pitch deck analyst.
Answer the user's question only from this chunk.

Question: {question}

Chunk:
\"\"\"{chunk}\"\"\"
If nothing relevant found, reply: "No relevant info in this chunk."
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    say = response.choices[0].message.content
    return say


#----------------------------------------------------

def combine_answers(answers):
    prompt = f"""
You are a startup expert. Combine the following extracted answers
from multiple PDF chunks into one final clean answer.

Extracted answers:
{answers}

Provide a structured, clear final answer.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

#--------------------------------------------------------------
st.title("Business Plan Checker")
st.write("Upload a pdf and ask related question.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
question = st.text_input("Ask a question about the PDF:")

if st.button("Get Answer"):
    if not uploaded_file:
        st.error("Please upload a PDF.")
    elif not question.strip():
        st.error("Please enter a question.")
    else:
        with st.spinner("Reading PDF..."):
            pdf_text = extract_pdf_text(uploaded_file)
            chunks = split_into_chunks(pdf_text)
            st.success(f"PDF Loaded! Total chunks: {len(chunks)}")

      

        chunk_answers = []
        for i, c in enumerate(chunks):
            st.write(f"Analyzing {i+1}/{len(chunks)}...")
            ans = ask_groq(c, question)
            chunk_answers.append(ans)

        final_answer = combine_answers("\n".join(chunk_answers))

        st.subheader(" Answer")
        st.write(final_answer)




