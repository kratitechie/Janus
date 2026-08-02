class RuleEngine:

    def decide(self, context):

        text = context["normalized_text"].lower()

        conversation = context["message"]["conversation_type"]

        forwarded = context["message"]["forwarded_count"]

        # -------------------------------------------------
        # OTP / SECURITY
        # -------------------------------------------------

        if any(x in text for x in [
            "otp",
            "verification code",
            "one time password",
            "verification otp",
            "login code"
        ]):

            return {
                "action": "notify",
                "message_type": "security",
                "reason": "Verification or OTP message.",
                "confidence": 0.99,
                "evidence_message_ids": []
            }

        # -------------------------------------------------
        # BANKING / FINANCE
        # -------------------------------------------------

        if any(x in text for x in [

            "bank",
            "credit card",
            "payment due",
            "upi",
            "debited",
            "credited",
            "transaction",
            "account",
            "balance",
            "emi",
            "loan",
            "statement",
            "refund",
            "hdfc",
            "icici",
            "axis",
            "sbi",
            "kotak"

        ]):

            return {
                "action": "notify",
                "message_type": "financial_update",
                "reason": "Financial notification.",
                "confidence": 0.98,
                "evidence_message_ids": []
            }

        # -------------------------------------------------
        # EDUCATION
        # -------------------------------------------------

        if any(x in text for x in [

            "assignment",
            "faculty",
            "attendance",
            "class",
            "semester",
            "exam",
            "offer letter",
            "project",
            "portal",
            "submission"

        ]):

            return {
                "action": "notify",
                "message_type": "education",
                "reason": "Academic reminder.",
                "confidence": 0.97,
                "evidence_message_ids": []
            }

        # -------------------------------------------------
        # DEADLINES
        # -------------------------------------------------

        if any(x in text for x in [

            "today",
            "tomorrow",
            "deadline",
            "meeting",
            "last date",
            "closing",
            "expires",
            "interview",
            "due",
            "before"

        ]):

            return {
                "action": "notify",
                "message_type": "deadline",
                "reason": "Time-sensitive reminder.",
                "confidence": 0.96,
                "evidence_message_ids": []
            }

        # -------------------------------------------------
        # TRAVEL
        # -------------------------------------------------

        if any(x in text for x in [

            "flight",
            "boarding",
            "train",
            "bus",
            "departure",
            "arrival",
            "pnr",
            "gate"

        ]):

            return {
                "action": "notify",
                "message_type": "travel",
                "reason": "Travel update.",
                "confidence": 0.97,
                "evidence_message_ids": []
            }

        # -------------------------------------------------
        # BUSINESS PROMOTIONS
        # -------------------------------------------------

        if (
            conversation == "business"
            and any(x in text for x in [

                "sale",
                "offer",
                "discount",
                "cashback",
                "coupon",
                "%",
                "deal",
                "shop now",
                "limited time",
                "buy now"

            ])
        ):

            return {
                "action": "digest",
                "message_type": "promotion",
                "reason": "Business promotion.",
                "confidence": 0.98,
                "evidence_message_ids": []
            }

        # -------------------------------------------------
        # SHOPPING
        # -------------------------------------------------

        if any(x in text for x in [

            "amazon",
            "flipkart",
            "myntra",
            "ajio",
            "meesho"

        ]):

            return {
                "action": "digest",
                "message_type": "shopping",
                "reason": "Shopping notification.",
                "confidence": 0.96,
                "evidence_message_ids": []
            }

        # -------------------------------------------------
        # FOOD DELIVERY
        # -------------------------------------------------

        if any(x in text for x in [

            "zomato",
            "swiggy"

        ]):

            return {
                "action": "digest",
                "message_type": "food",
                "reason": "Food delivery update.",
                "confidence": 0.95,
                "evidence_message_ids": []
            }

        # -------------------------------------------------
        # SPAM
        # -------------------------------------------------

        if (
            forwarded >= 5
            or any(x in text for x in [

                "lottery",
                "winner",
                "claim prize",
                "free gift",
                "click here",
                "earn money",
                "bitcoin",
                "investment scheme"

            ])
        ):

            return {
                "action": "mute",
                "message_type": "spam",
                "reason": "Likely spam.",
                "confidence": 0.99,
                "evidence_message_ids": []
            }

        # -------------------------------------------------
        # NO RULE
        # -------------------------------------------------

        return None