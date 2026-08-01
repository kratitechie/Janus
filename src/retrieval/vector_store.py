import chromadb

from src.llm.embedding_client import EmbeddingClient


class VectorStore:

    def __init__(self):

        self.embedder = EmbeddingClient()

        self.client = chromadb.PersistentClient(
            path="cache/chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name="message_history"
        )

    def add_messages(self, messages):

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

            embedding = self.embedder.embed(document)

            self.collection.add(

                ids=[str(message["message_id"])],

                documents=[document],

                embeddings=[embedding],

                metadatas=[message]

            )

    def search(self, query, top_k=5):

        embedding = self.embedder.embed(query)

        return self.collection.query(

            query_embeddings=[embedding],

            n_results=top_k

        )