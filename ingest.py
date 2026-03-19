import pandas as pd
from endee import Endee
from sentence_transformers import SentenceTransformer

INDEX_NAME = "social_network_ads"
EMBEDDING_DIM = 384
CSV_FILE = "Social_Network_Ads.csv"
TXT_FILE = "docs.txt"

ROW_LIMIT = 400
BATCH_SIZE = 100


def load_documents():
    docs = []

    df = pd.read_csv(CSV_FILE)
    df = df.head(ROW_LIMIT)

    print("Loaded CSV rows:", len(df))
    print("Columns:", df.columns.tolist())

    for _, row in df.iterrows():
        text = (
            f"User with ID {row['User ID']}, gender {row['Gender']}, "
            f"age {row['Age']}, estimated salary {row['EstimatedSalary']}, "
            f"purchased {row['Purchased']}."
        )
        docs.append(text)

    try:
        with open(TXT_FILE, "r", encoding="utf-8") as f:
            txt_lines = [line.strip() for line in f if line.strip()]
            docs.extend(txt_lines)
            print("Loaded TXT lines:", len(txt_lines))
    except FileNotFoundError:
        print("docs.txt not found, skipping text file.")

    print("Total documents to ingest:", len(docs))
    return docs


def ingest_data():
    print("Connecting to Endee...")
    client = Endee()

    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    try:
        client.create_index(
            name=INDEX_NAME,
            dimension=EMBEDDING_DIM,
            space_type="cosine"
        )
        print("Index created.")
    except Exception:
        print("Index may already exist.")

    index = client.get_index(INDEX_NAME)

    docs = load_documents()

    total_inserted = 0

    for start in range(0, len(docs), BATCH_SIZE):
        end = min(start + BATCH_SIZE, len(docs))
        batch_docs = docs[start:end]

        print(f"Embedding batch {start} to {end - 1} ...")
        vectors = model.encode(batch_docs, batch_size=32, show_progress_bar=False)

        records = []
        for i, vec in enumerate(vectors):
            records.append({
                "id": f"doc_{start + i}",
                "vector": vec.tolist(),
                "meta": {"text": batch_docs[i]}
            })

        print(f"Upserting batch {start} to {end - 1} into Endee ...")
        index.upsert(records)
        total_inserted += len(records)

        print(f"Inserted so far: {total_inserted}")

    print(f"Done. Inserted {total_inserted} documents into Endee.")


if __name__ == "__main__":
    ingest_data()