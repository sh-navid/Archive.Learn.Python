F = 20


def draw_line(N: str):
    print(N * "-")


def table(header: list, data: list):
    N = len(header) * F
    draw_line(N)
    for x in header:
        print(x.center(F), end="")
    print()
    draw_line(N)
    draw_line(N)
    for x in data:
        for y in x:
            print(str(y).ljust(F), end="")
        print()
    draw_line(N)


table(
    ["Head 1", "Head 2", "Head 3"],
    [
        [1, 2, 3],
        [10, 20, 30],
        [100, 200, 300],
    ],
)
