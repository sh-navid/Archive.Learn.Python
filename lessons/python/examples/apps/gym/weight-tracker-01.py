##---------------------------------------------------------------------------##
# DOCUMENTATION
# If input is not working in "VSCode" Terminal, add this
# "code-runner.runInTerminal": true
# to Settings.json in .vscode folder

##---------------------------------------------------------------------------##
# MUTABLES
my_weights = ["78", "75", "65"]


##---------------------------------------------------------------------------##
# FUNCTIONS
def print_text_chart():
    for i, number in enumerate(my_weights):
        print(f"Week {i+1}", "-" * int(int(number) / 2), ">", number)


##---------------------------------------------------------------------------##
# APPLICATION
while True:
    print("*" * 79)
    print("*" + "My Weight Application".center(77) + "*")
    print("*" * 79)
    answer = input("(1-Enter weight, 2-Show weights, 3-Exit app): ")

    if answer == "3":
        print("[This application is ended]")
        quit()
    elif answer == "2":
        print(my_weights)
        print_text_chart()
    else:
        weight = input("Enter your new weight: ")
        my_weights.append(weight)


##---------------------------------------------------------------------------##
# OUTPUT
"""
*******************************************************************************
*                            My Weight Application                            *
*******************************************************************************
(1-Enter weight, 2-Show weights, 3-Exit app): 2
['78', '75', '65']
Week 1 --------------------------------------- > 78
Week 2 ------------------------------------- > 75
Week 3 -------------------------------- > 65
"""