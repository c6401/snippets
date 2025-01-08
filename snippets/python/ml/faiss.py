import numpy as np
from sentence_transformers import SentenceTransformer
import faiss


model = SentenceTransformer("all-MiniLM-L6-v2")
blobs: list[str]

# index
embeddings = model.encode([i for i in blobs])
index = faiss.IndexFlatL2(len(embeddings[0]))
index.add(np.array(embeddings))

# search
query: str
query_embedding = model.encode([query])
D, I = index.search(np.array(query_embedding), 10)
result = [blobs[i] for i in I[0]]
