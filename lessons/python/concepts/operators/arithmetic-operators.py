# [Arithmetic Operators]

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def calc(a, b, op, op_name):
    result = eval(f"{a}{op}{b}")
    print(f"{a}\t{op}\t{b}\t->\t{result}\t{op_name}".expandtabs(6))

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
calc(10, 4, "+", "Addition")
calc(10, 4, "-", "Subtraction")
calc(10, 4, "*", "Multiplication")
calc(10, 4, "/", "Division")
calc(10, 4, "//", "Floor division")
calc(10, 4, "**", "Exponentiation")
calc(10, 4, "%", "Modulus")

# 10    +     4     ->    14    Addition
# 10    -     4     ->    6     Subtraction
# 10    *     4     ->    40    Multiplication
# 10    /     4     ->    2.5   Division
# 10    //    4     ->    2     Floor division
# 10    **    4     ->    10000 Exponentiation
# 10    %     4     ->    2     Modulus

