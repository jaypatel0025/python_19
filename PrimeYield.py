def prime(n):
    for num in range(2, n + 1):

        if num % 2 != 0:
            for i in range(3, int(num/2) + 1, 2):
                if num % i == 0:
                    break
            else:
                yield num

for j in prime(10):
    print(j)
