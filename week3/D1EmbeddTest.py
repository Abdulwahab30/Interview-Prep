import os
import numpy as np
from sentence_transformers import SentenceTransformer


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def test_embeddings():
    sentences = [
        "The dog ran through the park.",  # Index 0 (Dog)
        "A canine sprinted across the field.",  # Index 1 (Canine)
        "I love machine learning.",  # Index 2 (Machine Learning)
        "Artificial intelligence is fascinating.",  # Index 3 (AI)
        "The weather is sunny today.",  # Index 4 (Weather)
        "It is raining heavily outside.",  # Index 5
        "Python is a programming language.",  # Index 6
        "I enjoy writing code in Python.",  # Index 7
        "The cat slept on the sofa.",  # Index 8 (Cat)
        "A feline rested on the couch.",  # Index 9 (Feline)
    ]

    print("--- Generating Embeddings ---")
    # Load models
    bge = SentenceTransformer("BAAI/bge-small-en-v1.5")
    mini = SentenceTransformer("all-MiniLM-L6-v2")

    # Generate embeddings
    bge_embeddings = bge.encode(sentences)
    mini_embeddings = mini.encode(sentences)

    # Print shapes and confirm 384 dimensions
    print(f"BGE Embedding Shape: {bge_embeddings.shape}")
    print(f"MiniLM Embedding Shape: {mini_embeddings.shape}")

    print(f"Confirm BGE returns 384 dimensions: {bge_embeddings.shape[1] == 384}")
    print(
        f"Confirm MiniLM returns 384 dimensions: {mini_embeddings.shape[1] == 384}"
    )
    print("-" * 30)

    # Define the pairs to compare by their index in the sentences list
    pairs = [
        ("Dog ↔ Canine", 0, 1),
        ("Cat ↔ Feline", 8, 9),
        ("Machine Learning ↔ AI", 2, 3),
        ("Dog ↔ Weather", 0, 4),
    ]

    print("\n--- Computing Cosine Similarities ---")
    for label, idx1, idx2 in pairs:
        # Extract specific vectors for BGE
        bge_sim = cosine_similarity(bge_embeddings[idx1], bge_embeddings[idx2])

        # Extract specific vectors for MiniLM
        mini_sim = cosine_similarity(
            mini_embeddings[idx1], mini_embeddings[idx2]
        )

        print(f"{label}:")
        print(f"  -> BGE Similarity:    {bge_sim:.4f}")
        print(f"  -> MiniLM Similarity: {mini_sim:.4f}\n")


if __name__ == "__main__":
    test_embeddings()


# OUTPUT:

# BGE Embedding Shape: (10, 384)
# MiniLM Embedding Shape: (10, 384)
# Confirm BGE returns 384 dimensions: True
# Confirm MiniLM returns 384 dimensions: True
# ------------------------------

# --- Computing Cosine Similarities ---
# Dog ↔ Canine:
#   -> BGE Similarity:    0.7903
#   -> MiniLM Similarity: 0.5943

# Cat ↔ Feline:
#   -> BGE Similarity:    0.7919
#   -> MiniLM Similarity: 0.6571

# Machine Learning ↔ AI:
#   -> BGE Similarity:    0.7758
#   -> MiniLM Similarity: 0.6669

# Dog ↔ Weather:
#   -> BGE Similarity:    0.4924
#   -> MiniLM Similarity: 0.0724