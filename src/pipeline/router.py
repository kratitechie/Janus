import pandas as pd

from src.builders.context_builder import ContextBuilder
from src.agents.decision_agent import DecisionAgent


class Router:

    def __init__(self, loader):

        self.loader = loader

        self.builder = ContextBuilder(loader)

        self.agent = DecisionAgent()

    def run(self):

        results = []

        total = len(self.loader.messages)

        for index, row in self.loader.messages.iterrows():

            print(f"[{index+1}/{total}] Processing {row['message_id']}")
            context = self.builder.build(
                row["message_id"]
            )

            decision = self.agent.decide(context)

            results.append({

                "message_id": row["message_id"],

                "action": decision["action"],

                "message_type": decision["message_type"],

                "reason": decision["reason"],

                "confidence": decision["confidence"],

                "evidence_message_ids": ",".join(
                    decision["evidence_message_ids"]
                )

            })
            
            pd.DataFrame(results).to_csv(
                "output_partial.csv",
                index=False
            )

        return pd.DataFrame(results)