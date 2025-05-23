# evaluations/compositional_eval.py
from sklearn.metrics.pairwise import cosine_similarity

def compare_embeddings(embedding1, embedding2):
    """
    Compare two embeddings using cosine similarity.

    Parameters:
    - embedding1: First embedding vector
    - embedding2: Second embedding vector

    Returns:
    - Similarity score between 0 and 1
    """
    return cosine_similarity([embedding1], [embedding2])[0][0]

if __name__ == "__main__":
    # Example embeddings to test the comparison function
    embedding1 = [0.1, 0.2, 0.3, 0.4]
    embedding2 = [0.1, 0.2, 0.3, 0.5]
    
    similarity_score = compare_embeddings(embedding1, embedding2)
    print(f"Cosine Similarity: {similarity_score}")

