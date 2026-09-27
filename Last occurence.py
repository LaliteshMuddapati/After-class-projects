def linear_search(numbers, key, length):
    for i in range(length):
        if(numbers[i]==key):
            return i

    return -1


numbers=[1, 2, 3, 3 ,4, 6, 4, 9, 10, 1]

key=1

last = linear_search(numbers, key, len(numbers))
print(" The last location of {} is index {}".format(key, len(numbers)-1))