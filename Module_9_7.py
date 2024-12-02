def is_prime(func):
    def wrapper(*args):
        a = func(*args)
        b = 0
        for x in range(2, a // 2 + 1):
            if a % x == 0:
                b = b + 1
        if b <= 0:
            return f'Простое'
        else:
            return f'Составное'
    return wrapper


@is_prime
def sum_three(*args):
    sum_num = sum(args)
    print(sum_num)
    return sum_num

result = sum_three(2, 3, 6)
print(result)
# result2 = sum_three(4, 6, 8)
# print(result2)
