import random

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# یک کلاس برای تاس ساختیم، هر نمونه از این کلاس میتواند در حکم یک
# تاس مجزا عمل کند
class Dice:
    number = None
    name = "Default"

    def roll(self):
        self.number = random.choice([1, 2, 3, 4, 5, 6])

    def __str__(self):
        return f"{self.name} - {self.number}"


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۱
# در هر اجرا ۲ تاس ساخته و انداخته میشود
# برنامه را به شکلی تغییر دهید که در هر اجرا ۸ تاس ساخته و انداخته
# شود و نتیجه اجرای برنامه را نمایش دید
# dice1 = Dice()
# dice2 = Dice()
# dice1.roll()
# dice2.roll()

dice_list: list[Dice] = []
for _ in range(0, 8):
    dice_list.append(Dice())

for dice in dice_list:
    dice.roll()
    print(dice)

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# تمرین ۲
# به هر تاس یک نام اختصاص دهید تا بدانیم هر عدد را کدام تاس بدست
# آورده است
# برای نمونه نام تاس ها میتواند به شکل زیر باشد
# DiceNo1, DiceNo2, ..., DiceNo8

for index, dice in enumerate(dice_list):
    dice.roll()
    dice.name = str.format("DiceNo{}", index)
    print(dice)
