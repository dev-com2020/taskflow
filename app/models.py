from datetime import datetime

class Task:
    def __init__(self, title: str, description: str = ""):
        if not title or not title.strip():
            raise ValueError("Tytuł zadania nie może być pusty")
        if len(title) > 200:
            raise ValueError("Tytuł nie może przekraczać 200 znaków")
        self.title = title.strip()
        self.description = description
        self.done = False
        self.created_at = datetime.utcnow()
 
    def complete(self):
        self.done = True
 
    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "created_at": self.created_at.isoformat(),
        }