class Question:
    def __init__(self, text: str, id: int | None = None):
        self.id = id
        self.text = text


class Answer:
    def __init__(self, value: str, id: int | None = None):
        self.id = id
        self.value = value


class Test:
    id: int|None = None
    title: str
    difficult: int
    category: str

    def __init__(self, title: str, difficult: int, category: str):
        self.title = title
        self.difficult = difficult
        self.category = category



