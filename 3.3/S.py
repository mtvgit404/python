# numbers = {1, 2, 3, 4, 5}
numbers = set(range(1, 100))
# print(
#    {
#        num for num in numbers if str(num) not in
#        str([x for x in [
#            {j for i in range(2, j) if (j % i == 0)}
#            for j in numbers]
#            if x != set()
#        ]) and str(num) not in "10"
#    }
# )
# print(
#    [
#        numbers.symmetric_difference(item) for item in (
#            {j for i in range(2, j) if (j % i == 0)}
#            for j in numbers) if item > 1
#        if (item != set())
#    ]
# )

primes = {num for num in numbers if num > 1
          if all((num % i != 0) for i in range(2, int(num ** 0.5) + 1))
          }

# primes = {n for n in numbers if n > 1 and all(
#    n % d != 0 for d in range(2, int(n**0.5) + 1))}
print(primes)
