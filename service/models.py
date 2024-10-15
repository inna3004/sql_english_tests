class Answer:
    def __init__(self, value: str, id: int | None = None):
        self.id = id
        self.value = value

    def __str__(self):
        return self.value


class Question:
    answers: list[Answer]
    correct_answer: Answer

    def __str__(self):
        return self.text

    def __init__(self, text: str, id: int | None = None):
        self.id = id
        self.text = text


class Test:
    id: int|None = None
    title: str
    difficult: int
    category: str
    questions: list[Question]

    def __str__(self):
        return self.title

    def __init__(self,title: str, difficult: int, category: str, test_id: int = None):
        self.title = title
        self.difficult = difficult
        self.category = category
        self.id = test_id


class User:
    id: int|None = None
    username: str
    password: str
    is_admin: bool

class Results:
    id: int | None = None
    title: str
    username: str
    score: int

    def __init__(self,title: str, username: str, score: int, test_id: int = None):
        self.title = title
        self.username = username
        self.score = score
        self.id = test_id