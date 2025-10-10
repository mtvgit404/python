numbers = [1, 1, 3, 1, 10, 2, 4, 6, 7, 1, 2, 7]

print(str(' - '.join([str(digit)
      for digit in sorted(set(number for number in numbers))])))
