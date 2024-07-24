a = 0
b = 10

try:
    c = b / a
except ZeroDivisionError:
    c = 10**6

print(c)