import json
import os

MEMORY_FILE = "memory_store.json"

class MockHindsightClient:
    def __init__(self):
        self.storage = self._load()

    def _load(self):
        if os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "r") as f:
                return json.load(f)
        return {}

    def _save(self):
        with open(MEMORY_FILE, "w") as f:
            json.dump(self.storage, f, indent=2)

    def retain(self, text):
        if "Meeting with " in text:
            try:
                content_split = text.split("Meeting with ")[1]
                parts = content_split.split(": ")
                if len(parts) >= 2:
                    contact_name = parts[0].strip().lower()
                    notes = ": ".join(parts[1:]).strip()
                    if contact_name in self.storage:
                        self.storage[contact_name].append(notes)
                    else:
                        self.storage[contact_name] = [notes]
                    self._save()  # ✅ Saves to file permanently
                    return True
            except Exception:
                return False
        return False

    def recall(self, query_name):
        contact_name = query_name.strip().lower()
        return self.storage.get(contact_name, [])

hindsight_db = MockHindsightClient()