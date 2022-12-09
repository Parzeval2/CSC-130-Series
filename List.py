from random import randint
numbers = []
count = 0
while (count<20):
    numbers.append(randint(1,99))
    count += 1
#print(numbers)

for outer_index in range(0, len(numbers)):
    min_index=outer_index

    for inner_index in range(outer_index+1, len(numbers)):
        if (numbers[inner_index]<numbers[min_index]):
            min_index=inner_index
    temp = numbers[outer_index]
    numbers[outer_index] = numbers[min_index]
    numbers[min_index] = temp
print(numbers)
