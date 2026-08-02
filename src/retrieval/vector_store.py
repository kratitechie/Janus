import chromadb
from sentence_transformers import SentenceTransformer


class VectorStore:

    def __init__(self):

        self.embedder = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        self.client = chromadb.PersistentClient(
            path="cache/chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name="message_history"
        )

    def add_messages(self, messages):

        documents = []
        ids = []
        metadatas = []

        for message in messages:

            document = f"""
Message:
{message["message_text"]}

Conversation:
{message["conversation_type"]}

Forwarded:
{message["forwarded_count"]}

Business:
{message["business_id"]}

Group:
{message["group_id"]}
"""

            documents.append(document)
            ids.append(str(message["message_id"]))
            metadatas.append(message)

        embeddings = self.embedder.encode(
            documents,
            convert_to_numpy=True,
            normalize_embeddings=True
        ).tolist()

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(self, query, top_k=5):

        embedding = self.embedder.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        ).tolist()

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=top_k
        )