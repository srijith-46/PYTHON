while True:
    print("1.Check Value Error")
    print("2.Check File Not Found Error")
    print("3.Check Type Error")
    print("4.Check IOError")
    print("5.Name Error")
    print("0.Exit")
    ch=int(input("Enter Choice:"))
    if ch==1:
        try:
            f = open('f1.txt', 'z')
            print("Successful")
        except ValueError:
            print("Value Error")
    elif ch==2:
        try:
            f = open('f9.txt', 'r')
            print("Successful")
        except FileNotFoundError:
            print("File Not Found error")
    elif ch==3:
        try:
            f = open('f1.txt', 'r',"w")
            print("Successful")
        except TypeError:
            print("Type Error")
    elif ch==4:
        try:
            f = open('f1', 'w+')
            f.write("Sample")
            f1 = open('f2', 'r')
            print("Successful")
        except IOError:
            print("IO Error")
    elif ch==5:
        try:
            f=opens('f1.txt',"r")
            print("Successful")
        except NameError:
            print("Name Error")
    elif ch==0:
        break
    else:
        print("Invalid input")
