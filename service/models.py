class Question:
    id: int|None = None
    text: str


class Answer:
    id: int|None = None
    value: str


class Test:
    id: int|None = None
    title: str
    difficult: int
    category: str

    def __init__(self, title: str, difficult: int, category: str):
        self.title = title
        self.difficult = difficult
        self.category = category



