import json


def build_decision_prompt(context):

    retrieval = []

    for item in context["retrieval"][:2]:

        retrieval.append({

            "message": item["metadata"]["message_text"],

            "distance": round(item["distance"], 3)

        })

    compact_context = {

        "message": context["normalized_text"],

        "conversation_type":
            context["message"]["conversation_type"],

        "forwarded":
            context["message"]["forwarded_count"],

        "retrieval":
            retrieval

    }

    return f"""
You are JANUS.

Decide whether this WhatsApp message should:

- notify
- digest
- mute

Rules:

- Banking, OTP, payments, deadlines, travel -> notify
- Promotions -> digest
- Spam or scams -> mute

If unsure, use retrieved examples.

Return ONLY valid JSON.

{{
"action":"",
"message_type":"",
"reason":"",
"confidence":0.0,
"evidence_message_ids":[]
}}

Context:

{json.dumps(compact_context)}
"""