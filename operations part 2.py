import os


with open('words.txt', 'w') as f:
    f.write("Qwerty uiop asdf")
f.close()


with open('words.txt', 'r') as file:
    words=file.readlines()
    for line in words:
        word=line.split()
        print(word) 
file.close()



if os.path.exists("My_file.txt"):
    print("File exists")
else:
    print("File doesn't exists")

file = open('My_file.txt', 'w')


os.remove("sample_doc.txt")