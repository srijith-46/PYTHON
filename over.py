class Student:
  def show(self,name=None,age=None,grade=None):
    if(name==None and age==None and grade==None):
      print("No data is given")
    elif(age==None and grade==None):
      self.name=name
      print("My name is ",self.name)
    elif(grade==None):
      self.name=name
      self.age=age
      print("My name is ",self.name,"and age is",self.age)
    else:
      self.name=name
      self.age=age
      self.grade=grade
      print("Name:",self.name,"Age:",self.age,"Class:",self.grade)

s=Student()

while True:
  print("1.No arguments\n2.One arguments\n3.Two arguments\n4.Three arguments\n")
  c=int(input("Enter the options"))
  if(c==1):
    s.show()
  elif(c==2):
    s.show("Srijith")
  elif(c==3):
    s.show("Varun",22)
  else:
    s.show("jaga",22,10)
