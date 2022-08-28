## [Not Completed Yet]
## This idea is very simple; you can expand it with AI[ML, Expert System, ...]
## Name of this bot is آوآ


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


# TODO: Add weight to each question and answer
# TODO: Save and load this bot dictionary somewhere; he/she should learn more
# TODO: Store chain of conversations to analyse later
# TODO: Questions also should be a collection; hello, hi, Greetings, are in the same category
# TODO: What if someone says "Hello, How are you?"; should i answer to hello? and also answer to How are you? Think!
# TODO: Should i use regular expressions to find the similarity patterns?
# TODO: Make a CLASS structure to store different types of information about each ENTITY
bot_data = {
    "how @ are you &": {
        "old": {"answer": "[CMD:BIRTH]", "patterns": ["I am @ days old","I am @", "@ days"]}
    },
    "what is your @": {
        "name": {"answer": "AavAa", "patterns": ["My name is @", "I am @", "@"]},
        "pets name": {
            "answer": "",
            "patterns": ["I do not have one", "I do not have any"],
        },
    },
    "do you have a @": {
        "pet": {
            "answer": "",
            "patterns": ["No, I do not have one", "No, I do not have any"],
        },
    },
}

while True:
    answer = clean_text(input("Write something for me: "))

    selected_key = None
    selected_sim = -1
    MIN_SIMILARITY_TRESH = 0.59

    for key in bot_data.keys():
        key = clean_text(key)
        sim = similarity(key, answer)
        print(sim, key)

        if sim > MIN_SIMILARITY_TRESH:
            if selected_key is None:
                selected_key = key
                selected_sim = sim
            elif selected_sim < sim:
                selected_key = key
                selected_sim = sim

    print(selected_key, selected_sim)
