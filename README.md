📌 Endee AI Marketing RAG
🚀 Overview

This project is an AI-powered marketing analytics system that leverages the Endee Vector Database to perform semantic search on both structured and unstructured data. It enables users to query customer and campaign data using natural language and visualize insights through interactive dashboards.

The system demonstrates a real-world AI pipeline combining data ingestion, embedding generation, vector storage, and semantic retrieval.

🎯 Key Features

🔍 Semantic Search using Endee Vector Database

📊 Interactive Data Visualization (Streamlit charts)

🧠 Natural Language Querying over customer data

📁 Handles both:

Structured data (CSV)

Unstructured data (text files)

⚡ Fast retrieval using vector similarity

🏗️ Modular architecture (ingest → query → UI)

)

🧠 System Architecture

Structured Data (CSV) + Unstructured Data (TXT)
                ↓
         Text Conversion
                ↓
     Embedding Generation (Sentence Transformers)
                ↓
        Endee Vector Database
                ↓
        Query Embedding
                ↓
      Semantic Retrieval (Top-K Results)
                ↓
         Streamlit UI + Charts

🛠️ Tech Stack

Python

Endee Vector Database

Sentence Transformers (Embeddings)

Streamlit (UI & Visualization)

Pandas (Data Processing)

Docker (Endee Server)

📂 Project Structure
endee-ai-project/
│
├── app.py           # Streamlit UI (graphs + query)
├── ingest.py        # Data ingestion into Endee
├── query.py         # Semantic search logic
├── bank-full.csv    # Structured dataset
├── docs.txt         # Unstructured text data
├── requirements.txt
└── README.md
⚙️ Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/Shwet2022/Marketing_analysis_rag.git
cd Marketing_analysis_rag
2️⃣ Setup Virtual Environment
python -m venv venv

Activate:

# Windows
.\venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Endee Server (Docker)
docker run --ulimit nofile=100000:100000 -p 8080:8080 -v "${PWD}\endee-data:/data" --name endee-server --restart unless-stopped endeeio/endee-server:latest
5️⃣ Ingest Data (Run Once)
python ingest.py
6️⃣ Run Application
streamlit run app.py

Open in browser:

http://localhost:8501
📊 Dataset

Bank Marketing Dataset

Contains customer attributes such as:

Age, Job, Marital Status

Education, Loans, Balance

Campaign outcomes (subscribed: yes/no)

🔍 Example Queries

Which customers are likely to subscribe?

Find high-value customers for marketing campaigns

Which users have housing loans?

Show financially stable customers

⚠️ Important Notes

Data ingestion is performed once using ingest.py

UI performs real-time retrieval only

Endee stores vector embeddings, not raw structured queries

Filtering is implemented on top of semantic search

🏆 Key Learning Outcomes

Built a real-world AI system using vector databases

Integrated structured + unstructured data

Implemented semantic search pipeline

Developed an interactive analytics dashboard

🚀 Future Improvements

Add LLM-based answer generation (RAG)

Implement advanced filtering using metadata

Enable file upload (CSV/PDF ingestion)

Improve ranking and recommendation logic

👨‍💻 Authors

Shwetangi Tiwari
GitHub: https://github.com/Shwet2022

⭐ Acknowledgements

Endee Vector Database

HuggingFace Sentence Transformers

Streamlit
