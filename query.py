from endee import Endee
from sentence_transformers import SentenceTransformer
from ingest import INDEX_NAME   # import from previous ingest file


def search_query(user_query, top_k=10):
    client = Endee()
    model = SentenceTransformer("all-MiniLM-L6-v2")

    index = client.get_index(INDEX_NAME)
    query_vector = model.encode([user_query])[0]

    results = index.query(
        vector=query_vector.tolist(),
        top_k=top_k
    )

    retrieved_texts = []
    for item in results:
        meta = item.get("meta", {})
        retrieved_texts.append(meta.get("text", "No text found"))

    query_lower = user_query.lower()
    filtered = []

    # Hybrid filtering for Social_Network_Ads dataset

    if "male" in query_lower:
        filtered = [text for text in retrieved_texts if "gender male" in text.lower()]

    elif "female" in query_lower:
        filtered = [text for text in retrieved_texts if "gender female" in text.lower()]

    elif "purchased" in query_lower or "bought" in query_lower or "buyers" in query_lower:
        if "no" in query_lower or "not" in query_lower:
            filtered = [text for text in retrieved_texts if "purchase status 0" in text.lower()]
        else:
            filtered = [text for text in retrieved_texts if "purchase status 1" in text.lower()]

    elif "not purchased" in query_lower or "did not buy" in query_lower:
        filtered = [text for text in retrieved_texts if "purchase status 0" in text.lower()]

    elif "young" in query_lower:
        filtered = []
        for text in retrieved_texts:
            try:
                age_part = text.lower().split("age is ")[1].split(",")[0]
                age = int(age_part)
                if age < 30:
                    filtered.append(text)
            except:
                pass

    elif "old" in query_lower or "older" in query_lower:
        filtered = []
        for text in retrieved_texts:
            try:
                age_part = text.lower().split("age is ")[1].split(",")[0]
                age = int(age_part)
                if age >= 40:
                    filtered.append(text)
            except:
                pass

    elif "high salary" in query_lower:
        filtered = []
        for text in retrieved_texts:
            try:
                salary_part = text.lower().split("estimated salary is ")[1].split(",")[0].strip().rstrip(".")
                salary = int(salary_part)
                if salary >= 100000:
                    filtered.append(text)
            except:
                pass

    elif "low salary" in query_lower:
        filtered = []
        for text in retrieved_texts:
            try:
                salary_part = text.lower().split("estimated salary is ")[1].split(",")[0].strip().rstrip(".")
                salary = int(salary_part)
                if salary < 50000:
                    filtered.append(text)
            except:
                pass

    # fallback to semantic search results
    if filtered:
        return filtered[:3]

    return retrieved_texts[:3]


if __name__ == "__main__":
    query = input("Enter your query: ")
    results = search_query(query)

    print("\nTop Results:")
    for r in results:
        print("-", r)