class opover():
    def __init__(self):
        self.alist=[]
    
    def get_element(self):
        n=int(input("Enter the size of list"))
        for i in range(0,n):
            element=int(input("Enter element"))
            self.alist.append(element)

    
    def __add__(self,other):
        new_list=[]
        for i in range(0,len(self.alist)):
            new_list.append(self.alist[i]+other.alist[i])
        return new_list
    
    def __sub__(self,other):
        new_list=[]
        for i in range(0,len(self.alist)):
            new_list.append(self.alist[i]-other.alist[i])
        return new_list

    def __mul__(self,other):
        new_list=[]
        for i in range(0,len(self.alist)):
            new_list.append(self.alist[i]*other.alist[i])
        return (new_list)

    def __floordiv__(self,other):
        new_list=[]
        for i in range(0,len(self.alist)):
            new_list.append(self.alist[i]//other.alist[i])
        return (new_list)

    def __pow__(self,other):
        new_list=[]
        for i in range(0,len(self.alist)):
            new_list.append(self.alist[i]**other.alist[i])
        return (new_list)
