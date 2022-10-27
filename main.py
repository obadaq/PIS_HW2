class myDate:
    
    def __init__(self,day,month,year) :
        self.day = day
        self.month = month
        self.year = year
        
        
    def valid_date(self) :
        months31= [1,3,5,7,8,10,12]
        months30= [4,6,9,11]
        if((self.year % 400 == 0) or 
           (self.year % 100 != 0) and
           (self.year % 4 == 0)):   
            leap = True  
        else:  
            leap = False 

        if ((1<=self.day<=31 and (self.month in months31)) or
            (1<=self.day<=30 and (self.month in months30)) or
            (leap and 1<=self.day<=29) or 
            ((not leap) and 1<=self.day<=28)):
                return True
        else:
                return False


    def __add__(self,other):
        self.day = self.day + other
        return print(self)


    def __str__ (self) :
        return str(self.day) +'\\' + str(self.month) + '\\'+str(self. year)

d1 = myDate(10,12,2022)
d2 = myDate(20,12,2022)
d3 = d1+10

#print(d3)

'''
    def CheckLeap(Year):  
  # Checking if the given year is leap year  
        if((Year % 400 == 0) or 
           (Year % 100 != 0) and
           (Year % 4 == 0)):   
            print("Given Year is a leap Year");  
  # Else it is not a leap year  
        else:  
             print ("Given Year is not a leap Year")  
'''