months1= [1,3,5,7,8,10,12]
months2= [4,6,9,11]
day = int(input('enter day'))
month = int(input('enter month'))
year = int(input('enter year'))

if((year % 400 == 0) or 
    (year % 100 != 0) and
    (year % 4 == 0)):   
    leap = True  

else:  
    leap = False 


print (leap)

if ((1<=day<=31 and (month in months1)) or
    (1<=day<=30 and (month in months2)) or
    (leap and 1<=day<=29) or 
    ((not leap) and 1<=day<=28)):
     
    print('OK')
else:
    print('NOT OK')

