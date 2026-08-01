from src.media.media_router import MediaRouter
from typing import Dict, Any
from src.retrieval.history_retriever import HistoryRetriever

class ContextBuilder:

    def __init__(self, loader):
        
        self.loader = loader
        self.media = MediaRouter(loader)
        self.retriever = HistoryRetriever(loader)

    def build(self, message_id) -> Dict[str, Any]:

        message = self.loader.messages[
            self.loader.messages["message_id"] == message_id
        ].iloc[0]
        normalized_text = self.media.process(message)
        
        context = {

            "message": message.to_dict(),
            
            "normalized_text": normalized_text,

            "retrieval": None,
            
            "user": None,

            "group": None,

            "business": None,

            "history": None,

            "events": None,

            "media": None,
        }

        # ---------------- User ----------------

        user = self.loader.users[
            self.loader.users["user_id"] == message["user_id"]
        ]

        if not user.empty:
            context["user"] = user.iloc[0].to_dict()

        # ---------------- Group ----------------

        if message["group_id"]:

            group = self.loader.groups[
                self.loader.groups["group_id"] == message["group_id"]
            ]

            if not group.empty:
                context["group"] = group.iloc[0].to_dict()

        # ---------------- Business ----------------

        if message["business_id"]:

            business = self.loader.business_accounts[
                self.loader.business_accounts["business_id"] == message["business_id"]
            ]

            if not business.empty:
                context["business"] = business.iloc[0].to_dict()

        # ---------------- History ----------------

        history = self.loader.message_history[
            self.loader.message_history["user_id"] == message["user_id"]
        ]

        context["history"] = history.to_dict("records")

        # ---------------- Events ----------------

        events = self.loader.message_events[
            self.loader.message_events["user_id"] == message["user_id"]
        ]

        context["events"] = events.to_dict("records")

        print("[RAG] Retrieving...")
        print("[RAG] Done")
        context["retrieval"] = self.retriever.retrieve(
            normalized_text
            
        )
        print("Retrieval complete.")
        return context