'''Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.'''
import math
X = 0
Y = 0
while X < 1 or X > 999:
    X = int(input('первое число '))
while Y < 1 or Y > 999:
    Y = int(input('первое число '))
print(X)
print(Y)

S = X + Y
P = X * Y

# Y = S - Х
# P = X (S - X)
# X*X - S*X + P = 0
# X =

print (S)
print (P)
D = S*S -4*P
print (D)

X1 = (S+ math.sqrt(D))/2

Y1 = S - X1


if X1 > 0 and Y1 > 0:
    print(f"есть такое решение: X = {X1}, Y = {Y1}")



