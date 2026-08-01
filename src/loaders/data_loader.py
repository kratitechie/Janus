from pathlib import Path
import pandas as pd


class DataLoader:
    """
    Loads all CSV datasets into pandas DataFrames.
    """

    def __init__(self, dataset_path="dataset"):

        self.dataset_path = Path(dataset_path)

        self.messages = self._load("messages.csv")
        self.users = self._load("users.csv")
        self.groups = self._load("groups.csv")
        self.group_members = self._load("group_members.csv")

        self.business_accounts = self._load("business_accounts.csv")
        self.user_business_history = self._load("user_business_history.csv")

        self.message_history = self._load("message_history.csv")
        self.message_events = self._load("message_events.csv")

        self.images = self._load("images.csv")
        self.voice_notes = self._load("voice_notes.csv")

        self.notification_summary = self._load(
            "daily_notification_summary.csv"
        )

        self.sample_messages = self._load(
            "sample_messages.csv"
        )

    def _load(self, filename):

        path = self.dataset_path / filename

        return pd.read_csv(path)