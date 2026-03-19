import time
import pandas as pd
from endee import Endee, Precision
from sentence_transformers import SentenceTransformer

INDEX_NAME = f"social_network_ads_a1"
CSV_FILE = "Social_Network_Ads.csv"

def ingest_data():
    client = Endee()
    model = SentenceTransformer("all-MiniLM-L6-v2")

    client.create_index(
        name=INDEX_NAME,
        dimension=384,
        space_type="cosine",
        precision=Precision.INT8
    )

    index = client.get_index(INDEX_NAME)

    df = pd.read_csv(CSV_FILE).head(500)

    docs = []
    for _, row in df.iterrows():
        docs.append(
            f"Customer gender {row['Gender']}, age is {row['Age']}, "
            f"estimated salary is {row['EstimatedSalary']}, "
            f"purchase status {row['Purchased']}."
        )

    vectors = model.encode(docs, show_progress_bar=False)

    records = []
    for i, vec in enumerate(vectors):
        records.append({
            "id": f"doc_{i}",
            "vector": vec.tolist(),
            "meta": {"text": docs[i]}
        })

    index.upsert(records)
    print("Inserted successfully into", INDEX_NAME)

if __name__ == "__main__":
    ingest_data()
