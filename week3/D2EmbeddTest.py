import numpy as np
from sentence_transformers import SentenceTransformer
import matplotlib.pyplot as plt
import seaborn as sns

def test_expanded_embeddings():
    # 1. Curate 50 sentences across mixed topics (Duplicates, Negations, Distinct topics)
    sentences = [
        # --- Topic 1: Dogs & Canines (0-9) ---
        "The dog ran through the park.",                      # 0: Base dog
        "The dog ran through the park.",                      # 1: Exact Duplicate
        "A canine sprinted across the field.",                # 2: Semantic Duplicate
        "The puppy played with a ball in the yard.",          # 3: Related
        "A hound chased the rabbit through the forest.",       # 4: Related
        "The dog did not run through the park.",              # 5: Negation
        "No dogs were seen in the park today.",               # 6: Negation
        "Canines are known to be loyal domesticated animals.", # 7: Informational
        "I need to take my dog to the vet for a checkup.",    # 8: Contextual
        "A stray dog barked loudly at the passing car.",      # 9: Contextual
        
        # --- Topic 2: Cats & Felines (10-19) ---
        "The cat slept soundly on the living room sofa.",     # 10: Base cat
        "A feline rested quietly on the couch.",              # 11: Semantic Duplicate
        "The kitten chased a laser pointer across the rug.",  # 12: Related
        "The cat did not sleep on the sofa.",                 # 13: Negation
        "Lions and tigers are apex predators in the wild.",   # 14: Broad Feline
        "My cat purrs whenever I scratch behind its ears.",   # 15: Contextual
        "A black cat stretched out under the warm sun.",       # 16: Contextual
        "The mouse scurried away before the cat noticed.",    # 17: Interaction
        "Felines possess sharp claws and excellent vision.",  # 18: Informational
        "I bought a new scratching post for my pet cat.",     # 19: Contextual
        
        # --- Topic 3: AI & Machine Learning (20-29) ---
        "I love studying machine learning algorithms.",        # 20: Base ML
        "Artificial intelligence is a fascinating field.",    # 21: Semantic Duplicate
        "Deep learning neural networks require massive data.", # 22: Related
        "I do not like machine learning or AI.",              # 23: Negation
        "Computers are getting smarter every single day.",    # 24: Broad
        "Python is heavily utilized in data science.",        # 25: Contextual
        "Large language models can generate human-like text.", # 26: Specific AI
        "Supervised learning involves training on labeled data.",# 27: Technical
        "We built a predictive model using linear regression.",# 28: Technical
        "AI will completely transform the healthcare industry.",# 29: Impact
        
        # --- Topic 4: Weather & Nature (30-39) ---
        "The weather is incredibly sunny and warm today.",    # 30: Base Weather
        "It is beautifully bright and hot outside right now.", # 31: Semantic Duplicate
        "It is raining heavily with loud thunder strikes.",   # 32: Opposite Weather
        "The weather is not sunny at all today.",             # 33: Negation
        "A thick blanket of fog rolled over the morning bay.", # 34: Related
        "Meteorologists predict a massive blizzard tonight.", # 35: Related
        "The autumn leaves are turning vibrant shades of red.",# 36: Nature
        "Climate change is causing unpredictable global weather.",# 37: Broad
        "We went for a long hike up the rocky mountain trail.",# 38: Activity
        "A gentle breeze rustled the green trees in the valley.",# 39: Nature
        
        # --- Topic 5: Space & Astronomy (40-49) ---
        "The rover landed safely on the surface of Mars.",     # 40: Base Space
        "A robotic explorer touched down on the red planet.", # 41: Semantic Duplicate
        "The rover did not land safely on Mars.",             # 42: Negation
        "Astronomers discovered a new exoplanet in deep space.",# 43: Related
        "The Milky Way galaxy contains billions of stars.",    # 44: Broad
        "A massive solar flare erupted from the sun's surface.",# 45: Related
        "The James Webb Telescope captured stunning cosmic images.",# 46: Specific
        "Black holes possess an inescapable gravitational pull.",# 47: Related
        "Astronauts on the ISS conduct vital microgravity research.",# 48: Contextual
        "The rocket launched into orbit from the space coast." # 49: Contextual
    ]

    print("--- 1. Models Initialization ---")
    bge = SentenceTransformer("BAAI/bge-small-en-v1.5")
    mini = SentenceTransformer("all-MiniLM-L6-v2")

    print("\n--- 2. Generating Embeddings ---")
    bge_embeddings = bge.encode(sentences)
    mini_embeddings = mini.encode(sentences)

    print(f"BGE Embeddings Shape:  {bge_embeddings.shape} (Expected: (50, 384))")
    print(f"MiniLM Embeddings Shape: {mini_embeddings.shape} (Expected: (50, 384))")

    print("\n--- 3. Computing Pairwise Cosine Similarity Matrices ---")
    
    # Fast matrix-multiplication based pairwise cosine similarity calculation
    # Formula: (A • B) / (||A|| * ||B||)
    
    # Normalize the vectors first to make dot product equivalent to cosine similarity
    bge_norm = bge_embeddings / np.linalg.norm(bge_embeddings, axis=1, keepdims=True)
    mini_norm = mini_embeddings / np.linalg.norm(mini_embeddings, axis=1, keepdims=True)
    
    bge_matrix = np.dot(bge_norm, bge_norm.T)
    mini_matrix = np.dot(mini_norm, mini_norm.T)
    
    print(f"BGE Matrix Shape: {bge_matrix.shape}")
    print(f"MiniLM Matrix Shape: {mini_matrix.shape}")
    
    print("\n--- 4. Spot Checking Key Intersecting Pairs ---")
    
    def report_sim(label, i, j):
        print(f"{label}:")
        print(f"  -> BGE Score:    {bge_matrix[i, j]:.4f}")
        print(f"  -> MiniLM Score: {mini_matrix[i, j]:.4f}")

    report_sim("Exact Duplicates (Dog 0 ↔ Dog 1)", 0, 1)
    report_sim("Semantic Duplicates (Dog 0 ↔ Canine 2)", 0, 2)
    report_sim("Negation Check (Dog 0 ↔ Dog Negated 5)", 0, 5)
    report_sim("Cross-Topic Noise (Dog 0 ↔ Mars Space Rover 40)", 0, 40)
    
    # Optional Visualization block 
    # (Uncomment the lines below if you run this in a Jupyter notebook/local desktop to view maps)
    """
    plt.figure(figsize=(12, 10))
    sns.heatmap(bge_matrix, cmap='viridis')
    plt.title('BGE Pairwise Similarity Matrix')
    plt.show()
    """

if __name__ == "__main__":
    test_expanded_embeddings()

# OUTPUT:

# --- 2. Generating Embeddings ---
# BGE Embeddings Shape:  (50, 384) (Expected: (50, 384))
# MiniLM Embeddings Shape: (50, 384) (Expected: (50, 384))

# --- 3. Computing Pairwise Cosine Similarity Matrices ---
# BGE Matrix Shape: (50, 50)
# MiniLM Matrix Shape: (50, 50)

# --- 4. Spot Checking Key Intersecting Pairs ---
# Exact Duplicates (Dog 0 ↔ Dog 1):
#   -> BGE Score:    1.0000
#   -> MiniLM Score: 1.0000
# Semantic Duplicates (Dog 0 ↔ Canine 2):
#   -> BGE Score:    0.7903
#   -> MiniLM Score: 0.5943
# Negation Check (Dog 0 ↔ Dog Negated 5):
#   -> BGE Score:    0.8216
#   -> MiniLM Score: 0.6851
# Cross-Topic Noise (Dog 0 ↔ Mars Space Rover 40):
#   -> BGE Score:    0.4669
#   -> MiniLM Score: 0.0602