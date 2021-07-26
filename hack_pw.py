import bcrypt
import time

fn = open("student_pwd.txt", "r")
letters = "abcdefghijklmnopqrstuvwxyz"
arr = []
arr2 = []
newarr = []

for i in letters:
    for j in letters:
        passwd = i+j
        passwd = passwd.encode()
        arr.append(passwd)

newarr = list(arr)

for line in fn:
    check = line.partition(',')[2]
    check = check.rstrip()
    check = check.encode()
    arr2.append(check)

while not len(arr2) == 0:
    check = arr2.pop()
    arr = list(newarr)  # everytime i pop a password, i reset my array elements
    while not len(arr) == 0:
        start = time.time()
        x = arr.pop()
        if bcrypt.checkpw(x, check) == True:
            print(check)
            print(x)
            end = time.time()
            print(start)
            print(end)



                
