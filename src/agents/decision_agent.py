import hashlib
import json
from pathlib import Path

from src.agents.rule_engine import RuleEngine
from src.llm.gemini_client import GeminiClient
from src.llm.prompts import build_decision_prompt


class DecisionAgent:

    def __init__(self):

        self.llm = GeminiClient()

        self.rules = RuleEngine()

        self.cache = Path("cache/decisions")
        self.cache.mkdir(parents=True, exist_ok=True)

    def decide(self, context):

        # ---------------- Rule Engine ----------------

        rule = self.rules.decide(context)

        if rule is not None:

            print("[RULE ENGINE]")

            return rule
            
        # ---------------- Cache ----------------

        text = context["normalized_text"]

        cache_key = hashlib.md5(
            text.encode("utf-8")
        ).hexdigest()

        cache_file = self.cache / f"{cache_key}.json"

        if cache_file.exists():

            print("[DECISION CACHE]")

            return json.loads(
                cache_file.read_text(
                    encoding="utf-8"
                )
            )

        # ---------------- Gemini ----------------
        print("[GEMINI]")
        prompt = build_decision_prompt(context)

        try:

            decision = self.llm.generate_json(prompt)

            decision.setdefault("action", "digest")
            decision.setdefault("message_type", "unknown")
            decision.setdefault("reason", "No reason provided.")
            decision.setdefault("confidence", 0.5)
            decision.setdefault("evidence_message_ids", [])

            cache_file.write_text(

                json.dumps(
                    decision,
                    indent=2
                ),

                encoding="utf-8"

            )

            return decision

        except Exception as e:

            print(f"Decision Agent Error: {e}")

            return {

                "action": "digest",

                "message_type": "unknown",

                "reason": "Fallback after model failure.",

                "confidence": 0.5,

                "evidence_message_ids": []

            }