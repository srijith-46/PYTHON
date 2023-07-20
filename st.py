print("Enter the choice")
sh=int(input("1.string\n2.tuple\n3.exit\n"))
if sh==1:
	str=input("Enter the string")
	print("1.Length\n2.uppercase\n3.lowercase\n4.concatination\n5.title\n6.reverse\n7.inalpha\n8.slice\n9.split\n10.count")
	while True:
		ch=int(input("Enter your choice"))
		if ch==1:
			print(len(str))
		elif ch==2:
			print(str.upper())
		elif ch==3:
			print(str.lower())
		elif ch==4:
			c=input("Enter one more string")
			print(str + c)
		elif ch==5:
			print(str.title())
		elif ch==6:
			print(str[::-1])
		elif ch==7:
			check=input("Enter the alphabet you want to check")
			if check in str:
				print("true")
			else:	
				print("False")
		elif ch==8:
			print(str[0:2])
		elif ch==9:
			i=input("Enter the string")
			print(str.split(i))
		elif ch==10:
			print(str.count("s"))
		elif ch==11:
			break
elif sh==2:
	while True:
		print("1.Enter the element to extract from the tuple")
		print("2.length of the tuple")
		print("3.combination of two elements in tuple")
		print("4.repeat the elements")
		print("5.count the elements")
		print("6.max tuple")
		print("7.min tuple")
		print("8.convert a tuple into list")
		print("9.print the last element of the tuple")
		print("10.extract a part of the tuple")
		print("11.exit")
		ch=int(input("Enter your choice"))
		t1=tuple(input("Enter the first tuple"))
		t2=tuple(input("Enter the second tuple"))

		if ch==1:
			c=int(input("Enter the elements"))
			print(t1[c])
		elif ch==2:
			print(len(t1))
		elif ch==3:
			print(t1 + t2)
		elif ch==4:
			c=int(input("Enter repetition count"))
			print(t1*c)
		elif ch==5:
			c=input("Enter element you want to count")
			print(t1.count(c))
		elif ch==6:
			print(max(t1))
		elif ch==7:
			print(min(t1))
		elif ch==8:
			l=list(t1)
			print(l)
		elif ch==9:
			print(t1[-1])
		elif ch==10:
			s=int(input("Enter the starting index"))
			e=int(input("Enter the ending index"))
			print(t1[s:e])
		elif ch==11:
			break
