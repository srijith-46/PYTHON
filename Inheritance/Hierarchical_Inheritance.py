class student:
  def __init__(self):
    self.usn=input("Enter usn")
    self.name=input("Enter name")
    self.age=int(input("Enter age"))
  def display(self):
    print("name :",self.name)
    print("usn :",self.usn)
    print("age :",self.age)
class ugstudent(student):
  def __init__(self):
    student.__init__(self)
    self.sem=input("Enter Semster")
    self.fees=int(input("Enter fee"))
    self.stipend=int(input("Enter stipend"))
    ugstudent.display(self)
  def display(self):
    student.display(self)
    print("SEMESTER :",self.sem)
    print("FEE :",self.fees)
    print("STIPEND :",self.stipend)
class pgstudent(student):
  def __init__(self):
    student.__init__(self)
    self.sem=input("Enter Semster")
    self.fees=int(input("Enter fee"))
    self.stipend=int(input("Enter stipend"))
    pgstudent.display(self)
  def display(self):
    student.display(self)
    print("SEMESTER :",self.sem)
    print("FEE :",self.fees)
    print("STIPEND :",self.stipend)
while True:
    print("1.ug\n2.pg\n3.exit")
    ch=int(input("Enter the choice"))
    if ch==1:
      ug=ugstudent()
    elif ch==2:
      pg=pgstudent()
    elif ch==3:
      break
    else:
      print("wrong input")
    break

