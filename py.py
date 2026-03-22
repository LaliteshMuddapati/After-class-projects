file = open('text.txt', 'r')
print(file.read(11))
file.close()

file = open('text.txt', 'r')
print(file.readline())
file.close()

file = open('text.txt', 'r')
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('text.txt', 'r')
for x in file:
    print(x)

file.close()