numbers = [17, 12, 15, 11]
max_value = numbers[0]

for index in range(1,len(numbers)):
    if (numbers[index]>max_value):
        max_value=numbers[index]
print(max_value)