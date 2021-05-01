import random
while True:
    findnumber = random.randint(1000,9999)
    
    n1 = findnumber // 1000
    n2 = (findnumber // 100) % 10
    n3 = ((findnumber // 10) % 100) % 10
    n4 = findnumber % 10
    '''
    print (n1)
    print (n2)
    print (n3)
    print (n4)
    '''
    list = []
    list = list + [n1] + [n2] + [n3] + [n4]


    if len(list) > len(set(list)):
        pass
    else:
        break
while True:
    your_guess = int(input("Enter your guess "))
    y1 = your_guess // 1000
    y2 = (your_guess // 100) % 10
    y3 = ((your_guess // 10) % 100) % 10
    y4 = your_guess % 10
    y_list = []
    y_list = y_list + [y1] + [y2] + [y3] + [y4]
    k = 0
    m = 0
    for i in list:
        for j in y_list:
            if i == j and list.index(i) == y_list.index(j):
               k+=1
            elif i == j and list.index(i) != y_list.index(j):
                m+=1
    if k == 0 and m == 0:
        print ("No match found")
    elif k == 4:
        print ("You find this number...Congratulations!!! This is number is ", + findnumber)
    else:
        print ("You find %s бык and %s корова" % (k, m))

