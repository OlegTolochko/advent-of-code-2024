import re
input = open("in.txt", "r")
sum = 0
sum2 = 0
allow_multiplication = True

def multiply(multiplication):
    strings = str.split(multiplication, ",")
    multiplication = [int(re.findall("[0-9]+", string)[0]) for string in strings]

    return multiplication[0] * multiplication[1]

for line in input.readlines():
    stripped_line = line.strip("\n")
    all_correct_formulas = re.findall("mul\\([0-9]+,[0-9]+\\)", stripped_line)
    for multiplication in all_correct_formulas:
        sum += multiply(multiplication)

    formulas_and_do = re.findall("mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)", stripped_line)
    for item in formulas_and_do:
        if item == "do()":
            allow_multiplication = True
        elif item == "don't()":
            allow_multiplication = False
        elif allow_multiplication:
             sum2 += multiply(item)

print(sum)
print(sum2)
