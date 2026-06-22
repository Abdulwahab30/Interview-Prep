- Step 1: Document Ingestion
PDF
→ extract text
→ chunk text
- Step 2: Embeddings

Each chunk becomes:

text
→ embedding vector

A high-dimensional numerical representation.

- Step 3: Storage

Store:

chunk
embedding
metadata

inside a vector database.

- Step 4: User Query

User asks:

"What are the eligibility requirements?"

Convert question to embedding.

- Step 5: Retrieval

Compare query embedding against stored embeddings.

Similarity metric:

Cosine Similarity

Retrieve top-k chunks.

- Step 6: Reranking

Optional but common.

A reranker examines retrieved chunks and reorders them.

Goal:

better relevance

before sending to LLM.

- Step 7: Generation

Prompt contains:

Question
+
Retrieved Context

LLM generates answer.

- Step 8: Citation

Return:

Answer
Source
Page Number

so users can verify information.

One-Sentence Interview Version

RAG works by embedding documents into a vector space, retrieving the most relevant chunks using cosine similarity,
optionally reranking them, and then providing that context to an LLM so answers are grounded in source documents rather 
than relying solely on model memory.