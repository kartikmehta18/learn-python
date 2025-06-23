class Student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths
        # self.percentage=str((self.phy + self.chem +self.maths )/3) + "%" #when i do this % not updated
       
       #its update 
    @property
    def percentage(self):
        return str((self.phy + self.chem +self.maths )/3) + "%"
        
st1=Student(67,78,89)
print(st1.percentage)


st1.phy=86
print(st1.percentage)
