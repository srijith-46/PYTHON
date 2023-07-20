from magicmovements import *
ov1=opover()
ov2=opover()
ov1.get_element()
print(ov1.alist)
ov2.get_element()
print(ov2.alist)


while True:
    print("*"*50)
    print("Main Menu")
    print("*"*50)
    print("1.Add\n2.Subtract\n3.Multiply\n4.FloorDiv\n5.Power\n6.Exit")
    ch=int(input("Enter your choice"))
    if ch==1:
        print(ov1+ov2)
    elif ch==2:
        print(ov1-ov2)
    elif ch==3:
        print(ov1*ov2)
    elif ch==4:
        print(ov1//ov2)
    elif ch==5:
        print(ov1**ov2)
    elif ch==6:
        break
    else:
        print("Invalid choice")
