## [Not Completed Yet]
## This idea is very simple; you can expand it with AI[ML, Expert System, ...]
## Name of this bot is آوآ

import random


def similarity(text, sub_text):
    text = text.split(" ")
    sub_text = sub_text.split(" ")
    score = 0
    for st in sub_text:
        if st in text:
            score += 1
    return score / len(st)


def clean_text(text: str):
    text = text.replace("@", " ")
    text = text.replace("&", " ")
    text = text.replace("?", " ")
    text = text.replace(";", " ")
    text = text.replace(",", " ")
    for _ in range(5):
        text = text.replace("  ", " ")
    text = text.strip()
    return text


class Q:  # Question
    def __init__(self, value: str, links: list) -> None:
        self.value = value
        self.links = links


class A:  # Answer
    def __init__(self, key: str, value: str, answers: tuple) -> None:
        self.key = key
        self.value = value
        self.answers = answers


# TODO: Add weight to each question and answer
# TODO: Save and load this bot dictionary somewhere; he/she should learn more
# TODO: Store chain of conversations to analyse later
# TODO: Questions also should be a collection; hello, hi, Greetings, are in the same category
# TODO: What if someone says "Hello, How are you?"; should i answer to hello? and also answer to How are you? Think!
# TODO: Should i use regular expressions to find the similarity patterns?

q1a0 = A("", "well", ["I am @", "@"])
q1a1 = A("old", "7", ["I am @ days old", "I am @", "@ days"])
q1a2 = A("tall", "", ["I do not know the answer"])
q1a3 = A("happy", "", ["I do not know the answer"])
q1 = Q("how @ are you &", [q1a0, q1a1, q1a2, q1a3])

q2a1 = A("name", "AvA", ["My name is @", "I am @", "@"])
q2a2 = A("child name", "", ["I do not have a child"])
q2 = Q("what is your @", [q2a1, q2a2])

knowledge = [q1, q2]


while True:
    answer = clean_text(input("Write something for me: "))

    q_selected = None
    q_similarity = -1
    MIN_SIMILARITY_TRESH = 0.59

    for q in knowledge:
        key = clean_text(q.value)
        sim = similarity(key, answer)
        print(sim, key)

        if sim > MIN_SIMILARITY_TRESH:
            if q_selected is None or q_similarity < sim:
                q_selected = q
                q_similarity = sim

    print("-----")
    print(q_selected.value, q_similarity)

    # FIXME: complete this section
    if q_selected is not None:
        for a in q_selected.links:
            say = random.choice(a.answers).replace("@", a.value)
            print("Possible Answers:", say)
