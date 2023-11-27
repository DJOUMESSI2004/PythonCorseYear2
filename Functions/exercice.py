
# def factors(n):
#     factors = []
#     for i in range(1,n):
#         if n%i == 0:
#             factors.append(i)
#     factors.append(n)
#     return factors


# print(factors(5))     




def factors(n):
    factors = [i for i in range(1, n + 1) if n % i == 0]
    return factors

print(factors(8)) 