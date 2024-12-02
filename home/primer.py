# Для заданного числа N найти количество способов его записи
# в виде суммы положительных чисел
# (само число N также считать одной из форм записей такой суммы, т.е. N = N).

def num(N, k):
    if N == 0:
        return 1
    count = 0
    for d in range(1, min(N, k) + 1):
        count += num(N - d, d)
    return count


n = int(input("Введите число: "))
print(num(n, n))


ls = [34, 26, 45, 85, 1, 12, 14, 99, 9]
ls.sort(key=lambda x: sum(int(i) for i in str(x)))
print(ls)
