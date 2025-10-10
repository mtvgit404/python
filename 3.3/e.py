# numbers = [1, 2, 3, 4, 5]
numbers = [number for number in range(16, 100, 4)]
print(f"numbers = {numbers}")
print({num for num in numbers if num == int(num ** 0.5) ** 2})
