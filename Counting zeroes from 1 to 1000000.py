zeros = []
for i in range(1,1000000):
    zeros.append(str(i).count('0'))
print(sum(zeros))