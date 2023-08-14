# tests for #1

num1 = 250.5
num2 = 250.503
num3 = 224.83587582

num1 = str("{:.2f}".format(round(num1, 2)))
num2 = str("{:.2f}".format(round(num2, 2)))
num3 = float(str("{:.2f}".format(round(num3, 2))))
num3 += 0.12

print(num1)
print(num2)
print(num3)