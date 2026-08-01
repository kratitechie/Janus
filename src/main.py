from src.loaders.data_loader import DataLoader
from src.retrieval.vector_store import VectorStore


loader = DataLoader()

store = VectorStore()

messages = loader.message_history.to_dict("records")

store.add_messages(messages)

result = store.search(
    "maintenance payment due tomorrow"
)

print(result)