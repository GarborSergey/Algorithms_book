from random import randint

x = []

for i in range(20):
    x.append(randint(0, 100))

print(x)

# SORTED
for i in range(len(x)-1):
    for j in range(len(x)-1-i):  # Чтобы не трогать уже проверенные элементы
        if x[j] > x[j+1]:
            x[j], x[j+1] = x[j+1], x[j]

print(x)
