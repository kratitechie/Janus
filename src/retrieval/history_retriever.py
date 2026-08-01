from src.retrieval.vector_store import VectorStore


class HistoryRetriever:

    def __init__(self, loader):

        self.loader = loader
        self.store = VectorStore()

        count = self.store.collection.count()

        if count == 0:

            print("Building Vector Index...")

            history = loader.message_history.to_dict("records")

            self.store.add_messages(history)

            print("Vector Index Complete.")

        else:

            print(f"Loaded existing index ({count} vectors)")

    def retrieve(self, message_text, top_k=5):

        results = self.store.search(
            message_text,
            top_k
        )

        cleaned = []

        ids = results["ids"][0]
        docs = results["documents"][0]
        meta = results["metadatas"][0]
        dist = results["distances"][0]

        for i in range(len(ids)):

            cleaned.append({

                "message_id": ids[i],
                "document": docs[i],
                "metadata": meta[i],
                "distance": dist[i]

            })

        return cleaned