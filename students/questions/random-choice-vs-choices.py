import random

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
my_list = ["A", "B", "C"]

# میخواهیم از لیست بالا یک مورد تصادفی انتخاب کنیم
print("Choice:", random.choice(my_list))
"""
Choice: A
"""

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# میخواهیم از لیست بالا بیشتر از یک مورد تصادفی انتخاب کنیم
print("Choices:", random.choices(my_list, k=2))
"""
Choices: ['C', 'A']
"""


# [Optional]
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# میخواهیم با احتمال 75 درصد "رو"، و با احتمال 25 درصد "پشتِ" سکه ظاهر شود
coin = random.choices(["Front", "Back"], [0.25, 0.75])  # 0.25 + 0.75 = 1.0 ~ 100%
# از آنجایی که تابع
# choices
# یک لیست برمیگرداند ما فقط آیتم اول ان با ایندکس 0 را نمایش میدهیم
print(coin[0])

# اما میخواهیم بفهمیم آیا واقعا با احتمال 25 درصد "رو" آمده است یا خیر؟
# صد بار سکه می اندازیم
# البته
# برای اینکه به جواب دقیق تری برسیم بهتر است تعداد دفعاتی که سکه می اندازیم را افزایش دهیم
my_coin_list = []
N = 100
for i in range(N):
    coin = random.choices(["Front", "Back"], [0.25, 0.75])
    my_coin_list.append(coin[0])
# print(my_coin_list)
print("Probability of Front", my_coin_list.count("Front") / N)
print("Probability of Back", my_coin_list.count("Back") / N)
"""
نتیجه احتمالی با 100 پرتاب
Probability of Front 0.23
Probability of Back 0.77

نتیجه احتمالی با 100000 پرتاب
Probability of Front 0.24979
Probability of Back 0.75021
"""


# [Optional]
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# میخواهیم هر مورد با احتمال متفاوتی بصورت تصادفی انتخاب شود
# از کجا بدانیم که ایا این اعداد تصادفی با احتمال مد نظر ما ساخته میشوند؟
# به تعداد زیادی عدد تصادفی میسازیم و در یک لیست ذخیره میکنیم تا بتوانی بشمریم
# از هر مورد چند عدد تصادفی تابحال ساخته شده است
my_list = ["A", "B", "C"]
# احتمال رخ دادن هر کدام از ایتمها داخل لیست بالا
probabilities = [0.1, 0.7, 0.2]
my_selected_list = []
N = 100000
print("Wait until process ends...")
for i in range(N):
    rnd = random.choices(my_list, probabilities)
    # چون این تابع یک لیست بر میگرداند ما فقط اولین آیتم آن را
    # بر میداریم و در لیست موارد انتخاب شده خود قرار میدهیم
    my_selected_list.append(rnd[0])
# print(my_selected_list)
# میخواهیم اثبات کنیم آیا این تابع هر مورد را با احتمالی که خواسته ایم بدست آورده است یا خیر
pA = my_selected_list.count("A") / N
pB = my_selected_list.count("B") / N
pC = my_selected_list.count("C") / N
print("Count number of 'A's with probability of 0.1:", pA)
print("Count number of 'B's with probability of 0.7:", pB)
print("Count number of 'C's with probability of 0.2:", pC)

# ما 100 هزار مورد تصادفی ساختیم
# میخواستیم حرف
# "A"
# فقط با احتمال 0.1 بصورت تصادفی انتخاب شود
# همانطور که میبینید این حرف در واقعیت با احتمال 0.09996
# ظاهر شده است که بسیار نزدیک به عدد 0.1 است
"""
Count number of 'A's with probability of 0.1: 0.09996
Count number of 'B's with probability of 0.7: 0.69779
Count number of 'C's with probability of 0.2: 0.20225
"""
