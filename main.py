def cel2fal(cel):
  return cel * 1.8 + 32
print(cel2fal(10))

def fal2cel(fal):
  return (fal - 32) / 1.8
print(fal2cel(50))

def multiplication(max_value):
  for i in range(1, max_value+1):
    for j in range(1, max_value+1):
      print(f'{i*j:^4}', end=' ')
    print()

n = int(input("Введите максимальное значение: "))
print(multiplication(n))