<h1 align="center">📌 Endee AI Marketing RAG</h1>
<p align="center">
  <b>AI-powered marketing analytics with semantic search, vector storage, and interactive dashboards</b>
</p>

<hr>

<h2>🚀 Overview</h2>
<p>
  This project is an <b>AI-powered marketing analytics system</b> that leverages the
  <b>Endee Vector Database</b> to perform semantic search on both
  <b>structured</b> and <b>unstructured</b> data.
  It enables users to query customer and campaign data using natural language
  and visualize insights through interactive dashboards.
</p>

<p>
  The system demonstrates a real-world AI pipeline combining
  <b>data ingestion</b>, <b>embedding generation</b>, <b>vector storage</b>,
  and <b>semantic retrieval</b>.
</p>

<hr>

<h2>🎯 Key Features</h2>
<ul>
  <li>🔍 <b>Semantic Search</b> using Endee Vector Database</li>
  <li>📊 <b>Interactive Data Visualization</b> with Streamlit charts</li>
  <li>🧠 <b>Natural Language Querying</b> over customer data</li>
  <li>📁 Handles both:
    <ul>
      <li><b>Structured data</b> (CSV)</li>
      <li><b>Unstructured data</b> (Text files)</li>
    </ul>
  </li>
  <li>⚡ Fast retrieval using <b>vector similarity</b></li>
  <li>🏗️ Modular architecture: <b>ingest → query → UI</b></li>
</ul>

<hr>

<h2>🧠 System Architecture</h2>
<p align="center">
  <img width="1024" height="1536" alt="system_arc" src="https://github.com/user-attachments/assets/360e716a-7370-4832-92cf-64dc6a49b5bf" />

</p>

<hr>

<h2>🛠️ Tech Stack</h2>
<ul>
  <li>Python</li>
  <li>Endee Vector Database</li>
  <li>Sentence Transformers (Embeddings)</li>
  <li>Streamlit (UI &amp; Visualization)</li>
  <li>Pandas (Data Processing)</li>
  <li>Docker (Endee Server)</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>
<pre>
endee-ai-project/
│
├── app.py           → Streamlit UI (graphs + query)
├── ingest.py        → Data ingestion into Endee
├── query.py         → Semantic search logic
├── bank-full.csv    → Structured dataset
├── docs.txt         → Unstructured text data
├── requirements.txt → Dependencies
└── README.md        → Documentation
</pre>

<hr>

<h2>⚙️ Setup Instructions</h2>

<h3>1️⃣ Clone Repository</h3>
<pre><code>git clone https://github.com/Shwet2022/Marketing_analysis_rag.git
cd Marketing_analysis_rag</code></pre>

<h3>2️⃣ Setup Virtual Environment</h3>
<pre><code>python -m venv venv</code></pre>

<p><b>Activate:</b></p>
<p><b>Windows</b></p>
<pre><code>.\venv\Scripts\activate</code></pre>

<h3>3️⃣ Install Dependencies</h3>
<pre><code>pip install -r requirements.txt</code></pre>

<h3>4️⃣ Run Endee Server (Docker)</h3>
<pre><code>docker run --ulimit nofile=100000:100000 -p 8080:8080 -v "${PWD}\endee-data:/data" --name endee-server --restart unless-stopped endeeio/endee-server:latest</code></pre>

<h3>5️⃣ Ingest Data (Run Once)</h3>
<pre><code>python ingest.py</code></pre>

<h3>6️⃣ Run Application</h3>
<pre><code>streamlit run app.py</code></pre>

<p><b>Open in browser:</b></p>
<pre><code>http://localhost:8501</code></pre>

<hr>

<h2>📊 Dataset</h2>
<p><b>Bank Marketing Dataset</b></p>
<p>Contains customer attributes such as:</p>
<ul>
  <li>Age, Job, Marital Status</li>
  <li>Education, Loans, Balance</li>
  <li>Campaign outcomes (subscribed: yes/no)</li>
</ul>

<hr>

<h2>🔍 Example Queries</h2>
<ul>
  <li>Which customers are likely to subscribe?</li>
  <li>Find high-value customers for marketing campaigns</li>
  <li>Which users have housing loans?</li>
  <li>Show financially stable customers</li>
</ul>

<hr>

<h2>⚠️ Important Notes</h2>
<ul>
  <li>Data ingestion is performed once using <code>ingest.py</code></li>
  <li>UI performs real-time retrieval only</li>
  <li>Endee stores vector embeddings, not raw structured queries</li>
  <li>Filtering is implemented on top of semantic search</li>
</ul>

<hr>

<h2>🏆 Key Learning Outcomes</h2>
<ul>
  <li>Built a real-world AI system using vector databases</li>
  <li>Integrated structured + unstructured data</li>
  <li>Implemented semantic search pipeline</li>
  <li>Developed an interactive analytics dashboard</li>
</ul>

<hr>

<h2>🚀 Future Improvements</h2>
<ul>
  <li>Add LLM-based answer generation (RAG)</li>
  <li>Implement advanced filtering using metadata</li>
  <li>Enable file upload (CSV/PDF ingestion)</li>
  <li>Improve ranking and recommendation logic</li>
</ul>

<hr>

<h2>👨‍💻 Authors</h2>
<p>
  <b>Shwetangi Tiwari</b><br>
  GitHub:
  <a href="https://github.com/Shwet2022" target="_blank">https://github.com/Shwet2022</a>
</p>

<hr>

<h2>⭐ Acknowledgements</h2>
<ul>
  <li>Endee Vector Database</li>
  <li>HuggingFace Sentence Transformers</li>
  <li>Streamlit</li>
</ul>

<hr>

<h2>📸 Response SS</h2>
<p align="center">
  <b>Sample Output / Query Response Screenshots</b>
</p>


<img width="1887" height="942" alt="image" src="https://github.com/user-attachments/assets/17167a94-916d-401b-8c69-934024dca74d" />

<img width="1892" height="914" alt="image" src="https://github.com/user-attachments/assets/37d37ce9-6578-48c5-b92a-fd31938b55dd" />
