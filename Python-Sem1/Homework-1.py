try:
    n = int(input())
    k = int(input())
    if n < 1 or k < 1:
        raise KeyError('Must be greater than 0')
except ValueError:
    print('int needed')
except KeyError as ex:
    print(ex.__str__)

list_1 = []
list_2 = []

while n > 0:
    try:
        number = int(input())
    except ValueError:
        print('int needed')
    if number > k:
        list_1.append(number)
    if number <= k and number > 0:
        list_2.append(number)
    n -= 1

print(list_1)
print(list_2)

proizvedenie = 1
for i in range(0, len(list_1)):
    if i % 2 == 1:
        proizvedenie *= list_1[i]
print(proizvedenie)

minPos = list_1.index(min(list_1))
print(minPos)

list_2.sort()
razlika = list_2[-1] - list_2[0]
print(razlika)

