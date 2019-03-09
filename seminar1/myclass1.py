class Person:
         def __init__(self,Hight=100,Weight=50):
                 self.Hight=Hight
                 self.Weight=Weight


         def info(self):
               print("Height is", self.Height)
               print("Weight is", self.Weight)
         def set_info(self, Height, Weight):
               self.Height=Height
               self.Weight=Weight
