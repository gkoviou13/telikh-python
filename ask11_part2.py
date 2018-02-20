import random
import string
main_list=[]
for i in range(100):
    list1 = [random.choice(string.ascii_uppercase) for x in range(100)]
    main_list.append(list1)
for s in main_list:
    print(s)
file = input("give me a file name: ")
file += '.txt'
infile = open(file, 'r')
list_of_words = [line.rstrip() for line in infile]
infile.close()
list_check=[]
for word in list_of_words:
    for i in range(100):
        for j in range(100):
            if word[0] == main_list[i][j]:
                str1 = word[0]
                p = 1
                while p < len(word) and (i + p < 100):
                    if word[p] == main_list[i + p][j]:
                        str1 += main_list[i + p][j]
                    p += 1
                    if len(str1) == len(word):
                        if str1 not in list_check:
                            print(str1)
                    list_check.append(str1)
                str1 = word[0]
                p = 1
                while p < len(word) and (j + p < 100):
                    if word[p] == main_list[i][j + p]:
                        str1 += main_list[i][j + p]
                    p += 1
                    if len(str1) == len(word):
                        if str1 not in list_check:
                            print(str1)
                    list_check.append(str1)