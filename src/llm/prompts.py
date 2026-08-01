import json


def build_decision_prompt(context):

    compact_context = {
        "message": context["message"],
        "user": context["user"],
        "group": context["group"],
        "business": context["business"],
        "retrieval": context["retrieval"][:3],   # only top 3 similar messages
        "recent_events": context["events"][:5] if context["events"] else []
    }

    return f"""
You are JANUS.

Route ONE WhatsApp message.

Actions:
- notify = interrupt now
- digest = show later
- mute = spam, scam, irrelevant or low priority

Consider:
- user history
- retrieved similar messages
- business/group trust
- urgency
- user engagement

Return ONLY JSON.

Schema:
{{
  "action": "notify|digest|mute",
  "message_type": "<category>",
  "reason": "<max 20 words>",
  "confidence": 0.0,
  "evidence_message_ids": ["id1","id2"]
}}

Context:
{json.dumps(compact_context, default=str)}
"""