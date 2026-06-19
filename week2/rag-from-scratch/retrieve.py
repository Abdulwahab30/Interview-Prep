import numpy as np
from sentence_transformers import SentenceTransformer

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1,v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)

    return dot_product/ (norm_v1*norm_v2)


def retrieve_relevant_chunks(query, top_k=2):
    chunks = np.load("data/chunks.npy", allow_pickle=True)
    embeddings= np.load("data/embeddings.npy")

    model= SentenceTransformer('all-MiniLM-L6-v2')

    query_embedding = model.encode(query)

    scores = []

    for chunk_emb in embeddings:
        similarity = cosine_similarity(query_embedding,chunk_emb)
        scores.append(similarity)

    sorted_indices = np.argsort(scores)[::-1]

    results =[]
    for i in range(top_k):
        idx = sorted_indices[i]
        results.append({
            "text": chunks[idx],
            "score": scores[idx]
        })
        
    return results

# Quick test to make sure it works independently
if __name__ == "__main__":
    test_query = "What is the capacity of the quantum-gel battery?"
    matches = retrieve_relevant_chunks(test_query, top_k=1)
    print(f"Top Match Found:\n{matches[0]['text']}\n(Similarity Score: {matches[0]['score']:.4f})")