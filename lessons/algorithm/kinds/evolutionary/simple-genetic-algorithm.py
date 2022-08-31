## This is not the exact version of Genetic Algorithm
import random
import math


MIN, MAX = 100, 500
MAX_RESULT = 99999999999999


best_values = (None, None, None, None)
best_answer = MAX_RESULT
counter = 0


def goal(x, y, z, t):
    try:
        return (((x * math.pi) / y) * z + math.cos(t)) / t / 2
    except:
        return MAX_RESULT


def check(x, y, z, t):
    global counter, best_values, best_answer
    is_valuable = False
    counter += 1
    result = goal(x, y, z, t)
    if result < best_answer:
        best_answer = result
        best_values = (x, y, z, t)
        print("\nFounded,", best_answer, best_values)
        is_valuable = True
    if counter % 10000 == 0:
        print(".", end="")
    return is_valuable


def linear_algorithm():
    for x in range(MIN, MAX):
        for y in range(MIN, MAX):
            for z in range(MIN, MAX):
                for t in range(MIN, MAX):
                    check(x, y, z, t)


def simplified_genetic_algorithm():
    G = [[MIN, MIN, MIN, MIN], [MAX, MAX, MAX, MAX]]

    while True:
        NEW = [None, None, None, None]

        # CROSSOVER
        for index in range(4):
            NEW[index] = G[random.choice([0, 1])][index]

        # MUTATION
        NEW[random.choice([0, 1, 2, 3])] = random.randint(MIN, MAX)

        # REMOVE WORST MEMBER
        x, y, z, t = NEW
        if check(x, y, z, t):
            G[random.choice([0, 1])] = NEW


if __name__ == "__main__":
    # linear_algorithm()
    simplified_genetic_algorithm()
