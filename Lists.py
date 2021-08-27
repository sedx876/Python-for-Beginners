names = ['Sharon', 'Mike', 'Andy', 'Samarrah', 'Austin', 'Maryssa']
names[3] = 'Sam'
print(names[0])
print(names[2:4])


numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)