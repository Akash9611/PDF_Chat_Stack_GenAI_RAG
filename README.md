# PDF Chat Stack GenAI RAG 🚀

[![Animated Demo](https://github.com/Akash9611/PDF_Chat_Stack_GenAI_RAG/assets/animated-demo.gif)](https://github.com/Akash9611/PDF_Chat_Stack_GenAI_RAG)

> **Open-source “chat with any PDF” starter template!**  
> Built with **React + Tailwind CSS frontend**, **FastAPI backend**, **LangChain RAG (Retrieval-Augmented Generation) using OpenAI embeddings & GPT-4o**, vector search via **Pinecone/FAISS**, and **one-click deploy to Vercel + Docker**.

---

## 📦 Features

- **Chat with any PDF**: Upload a PDF and start chatting with it using state-of-the-art GenAI.
- **Frontend**: Beautiful, animated UI built in React & Tailwind CSS.
- **Backend**: FastAPI powers the API layer.
- **GenAI RAG Logic**: LangChain orchestrates Retrieval-Augmented Generation with OpenAI’s GPT-4o.
- **Vector Search**: Choose between Pinecone (cloud) or FAISS (local).
- **Deploy Easily**: One-click deploy to Vercel or run with Docker.

---

## 🎬 Visual Demo

![Animated UI](https://github.com/Akash9611/PDF_Chat_Stack_GenAI_RAG/assets/animated-demo.gif)

- **PDF Upload:** Drag & drop your PDF.  
- **Animated Chat:** Real-time, streaming chat responses with smooth UI transitions.  
- **Sources Highlighted:** See which PDF passages were referenced.  
- **Sidebar:** Conversation history and PDF management.

---

## 🛠️ Tech Stack

| Language   | % Usage |
|------------|---------|
| Python     | 33.8%   |
| CSS        | 28.6%   |
| TypeScript | 21.9%   |
| JavaScript | 9.8%    |
| HTML       | 5.9%    |

- **Frontend:** React, TypeScript, Tailwind CSS
- **Backend:** FastAPI (Python)
- **GenAI:** LangChain, OpenAI GPT-4o
- **Vector Stores:** Pinecone, FAISS

---

## 🚀 Quick Start

```bash
# 1️⃣ Clone the repo
git clone https://github.com/Akash9611/PDF_Chat_Stack_GenAI_RAG.git
cd PDF_Chat_Stack_GenAI_RAG

# 2️⃣ Run backend (FastAPI)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

# 3️⃣ Run frontend (React)
cd ../frontend
npm install
npm run dev

# 4️⃣ (Optional) Deploy with Docker or Vercel
# See docs/DEPLOY.md for details
```

---

## 🎨 Animated UI Preview

> The UI features smooth transitions, animated message bubbles, loading spinners, and highlighted references.  
> Designed for clarity, speed, and delightful user experience.

![Chat Animation](https://github.com/Akash9611/PDF_Chat_Stack_GenAI_RAG/assets/chat-animation.gif)

---

## 📚 How It Works

1. **Upload PDF**: Your document is chunked, embedded, and stored in a vector DB.
2. **Ask Questions**: Your queries are sent to the backend.
3. **RAG Pipeline**: LangChain retrieves relevant chunks, then GPT-4o composes answers.
4. **Sources**: Response shows citations from your PDF.

---

## 🐳 Docker Support

```bash
docker-compose up
# All services (frontend + backend) spin up together!
```

---

## 📄 License

Open-source under the [MIT License](LICENSE).

---

## 🙌 Contributing

Pull requests and issues welcome!

---

## 📞 Contact

- [GitHub Issues](https://github.com/Akash9611/PDF_Chat_Stack_GenAI_RAG/issues)
- [Email](mailto:akash9611@example.com)

---

## 🌟 Star this repo if you like it!

[![GitHub Repo stars](https://img.shields.io/github/stars/Akash9611/PDF_Chat_Stack_GenAI_RAG?style=social)](https://github.com/Akash9611/PDF_Chat_Stack_GenAI_RAG)

```

---

> _Built by [Akash9611](https://github.com/Akash9611) with ❤️_
