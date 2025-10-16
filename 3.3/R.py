numbers = {1, 2, 3, 4, 5}

print(
    dict([(j, [i for i in
          range(1, j + 1) if j % i == 0])
          for j in numbers
          ])
)
