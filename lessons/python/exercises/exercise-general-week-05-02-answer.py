my_characters = []

class Character:
    def __init__(self, ch, no):
        self.ch = ch
        self.no = no

    def __str__(self) -> str:
        return f"Character: {self.ch} - {self.no}"

    def __repr__(self) -> str:
        # object representation in string format
        return f"Ch: {self.ch} - {self.no}"


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 1 <----- range(97, 123)
for counter in range(97, 123):
    my_characters.append(Character(chr(counter), counter))
print(my_characters)


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Answer 2 <-----
for character in my_characters:
    print(character)