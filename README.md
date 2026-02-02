📊 Business Plan Checker

An AI-powered web application that analyzes **Business Plan PDFs** and answers user queries intelligently using **Large Language Models (LLMs)**.  
Built with **Streamlit** and powered by the **Groq API (LLaMA 3.1)** for fast, free inference.

---
🌐 Live Demo

🚀 **Access the deployed application here:**  
👉 [https://your-streamlit-app-link.streamlit.app](https://business-plan-checker-vuxxyztsw3gcve2eqcxton.streamlit.app/)


🚀 Live Features

- Upload a **Business Plan PDF**
- Ask **custom questions** related to the document
- Intelligent **chunk-wise document analysis**
- Combines insights from multiple chunks into a **single structured answer**
- Fast responses using **Groq LLaMA 3.1 model**
- Simple and interactive **Streamlit UI**

---

🧠 How It Works

1. User uploads a PDF business plan
2. The PDF text is extracted using `PyPDF2`
3. Text is split into manageable chunks
4. Each chunk is analyzed using an LLM
5. Individual answers are combined into a **final clean response**

---

🛠️ Tech Stack

- **Python**
- **Streamlit** – frontend & deployment
- **PyPDF2** – PDF text extraction
- **Groq API** – LLaMA 3.1 language model
- **python-dotenv** – environment variable management

---

📂 Project Structure

```text
Business Plan Checker/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation


