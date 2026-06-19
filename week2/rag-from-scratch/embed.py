import os
from sentence_transformers import SentenceTransformer
import numpy as np

def load_document(file_path):
    with open(file_path, 'r',encoding='utf-8') as f:
        text = f.read()
    return text

def split_text_into_chunks(text):
    raw_chunks = text.split('\n\n')

    cleaned_chunks = [' '.join(chunk.split()) for chunk in raw_chunks if chunk.strip()]

    return cleaned_chunks

def create_vector_store():
    print("Loading text document...")
    raw_text = load_document("data/notes.txt")
    
    print("Chunking document...")
    chunks = split_text_into_chunks(raw_text)
    print(f"Created {len(chunks)} chunks. Generating embeddings...")
    # Using a small, fast, and free local embedding model from HuggingFace
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    # For a 'from-scratch' project, we can save these locally as NumPy arrays 
    # instead of setting up a heavy Vector Database.
    np.save("data/chunks.npy", np.array(chunks))
    np.save("data/embeddings.npy", embeddings)
    print("Vector store saved successfully (chunks.npy and embeddings.npy)!")


if __name__ == "__main__":
    create_vector_store()