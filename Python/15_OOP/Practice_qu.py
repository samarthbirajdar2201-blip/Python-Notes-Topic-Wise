class Student:
     def __init__(self, name , marks):
         self.name = name 
         self.marks = marks 
         
     def avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi ",self.name, "Your avg marks is :" , sum/3)
        
        
s1 = Student("sam" , [36,28 ,58])
s1.avg()

# s1.name  = " ironman"
# s1.avg()