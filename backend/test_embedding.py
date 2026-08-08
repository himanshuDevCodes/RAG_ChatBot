from rag.embeddings import get_embedding_model

embedding_model = get_embedding_model()

vector = embedding_model.embed_query(
    "Python is amazing"
)

print(vector[:10])