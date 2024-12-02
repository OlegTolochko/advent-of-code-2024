import numpy as np
safe_count = 0
safe_count2 = 0
input = open("in.txt", "r")


def check_validity(report, operator):
    for i in range(len(report)-1):
        if operator:
            if not 1 <= report[i] - report[i+1] <= 3:
                return False
        else:
            if not -3 <= report[i] - report[i+1] <= -1:
                return False
    return True


for line in input.readlines():
    report = line.strip("\n").split(" ")
    report = [int(i) for i in report]
    operator = report[0] > report[1]
    if report[0] == report[1]:
        validity = False
    else:
        validity = check_validity(report, operator)

    if validity:
        safe_count += 1
    else:
        for i in range(len(report)):
            report_copy = report.copy()
            del report_copy[i]
            operator = report_copy[0] > report_copy[1]
            if check_validity(report_copy, operator):
                validity = True
                break

    if validity:
        safe_count2 += 1

print(safe_count)
print(safe_count2)