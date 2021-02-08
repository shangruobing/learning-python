for number in range(1, 21):
    print(number)

million = list(range(1, 1000))
print(million)
print(sum(million))

numbers = list(range(1, 21, 2))
print(numbers)
for num in numbers:
    print(num)

cubes = [value ** 3 for value in range(1, 11)]
for cube in cubes:
    print(cube)
