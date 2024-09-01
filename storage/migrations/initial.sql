create table answers (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    value VARCHAR(255) NOT NULL,
    question INT REFERENCES questions(id)
);


create table questions (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    text VARCHAR(255) NOT NULL,
    correct_answer_id integer,
    FOREIGN KEY (correct_answer_id) REFERENCES answers(id)
);
