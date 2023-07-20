print("Enter the choice")
sh=int(input("1.list\n2.set\n3.exit\n"))
if sh==1:
	l=eval(input("Enter the list"))
	print("1.len\n2.slicing\n3.max\n4.min\n5.append\n6.insert\n7.pop\n8.remove\n9.update\n10.extend\n11.exit\n")
	while True:
		ch=int(input("Enter your choice"))
		if ch==1:
			print(len(l))
		elif ch==2:
			s=int(input("Enter the starting index"))
			e=int(input("Enter the ending index"))
			print(l[s:e])
		elif ch==3:
			print(max(l))
		elif ch==4:
			print(min(l))
		elif ch==5:
			a=eval(input("Enter the value you want to append"))
			l.append(a)
			print(l)
		elif ch==6:
			i=int(input("enter the index at which you want insert"))
			n=eval(input("enter the data"))
			l.insert(i,n)
			print(l)
		elif ch==7:
			print(l.pop())
			print(l)
		elif ch==8:
			r=eval(input("Enter the item you want to remove"))
			l.remove(r)
			print(l)
		elif ch==9:
			i=int(input("enter the index you want to update"))
			u=eval(input("enter the data which you want to update"))
			l[i]=u
			print(l)
		elif ch==10:
			l2=eval(input("Enter the another list"))
			print(l.extend(l2))
			print(l)
		elif ch==11:
			break
elif sh==2:
	s1=eval(input("enter the set1"))
	s2=eval(input("enter the set2"))
	while True:
		print("1.len\n2.union\n3.intersection\n4.difference\n5.subset\n6.superset\n7not equivavlent\n8.equivalent \n9.disjoint\n10.clear\n11.exit")
		ch=int(input("Enter your choice"))
		if ch==1:
			print(len(s1))
		elif ch==2:
			print(s1 | s2)
		elif ch==3:
			print(s1 & s2)
		elif ch==4:
			print(s1.difference(s2))
		elif ch==5:
			print(s1.issubset(s2))
		elif ch==6:
			print(s1.issuperset(s2))
		elif ch==7:
			print(s1 != s2)
		elif ch==8:
			print(s1 == s2)
		elif ch==9:
			print(s1.isdisjoint(s2))
		elif ch==10:
			s1.clear()
			print(s1)
		elif ch==11:
			break
