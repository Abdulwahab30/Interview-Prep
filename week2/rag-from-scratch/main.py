import os
from dotenv import load_dotenv
from retrieve import retrieve_relevant_chunks
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Initialize your LLM client pointing to OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY")
)

def run_rag_pipeline(user_question):
    print(f"\n--- User Question: {user_question} ---")
    
    # 1. RETRIEVE: Get facts from our vector store
    print("Searching local vector database...")
    retrieved_docs = retrieve_relevant_chunks(user_question, top_k=2)
    
    # Combine the retrieved text chunks together
    context = "\n\n".join([doc['text'] for doc in retrieved_docs])
    
    # 2. PROMPT: Construct the instructions for the LLM
    system_prompt = "You are a helpful assistant. Answer the user's question strictly using only the provided context. If the answer cannot be found in the context, say 'I don't know'."
    
    user_prompt = f"""Context information is below.
---------------------
{context}
---------------------
Given the context information above and not prior knowledge, answer the query.
Query: {user_question}
Answer:"""

    # 3. GENERATE: Pass the context + question to the LLM
    print("Synthesizing answer with LLM...")
    model_name = os.environ.get("OPENROUTER_MODEL", "openai/gpt-4o-mini")
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.0 # Keep temperature at 0 for factual RAG to reduce hallucinations
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    # Test your completed RAG pipeline!
    question = "what is Project Aetheris?"
    answer = run_rag_pipeline(question)
    
    print("\n--- Final LLM Response ---")
    print(answer)