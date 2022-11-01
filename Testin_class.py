from Date import Date
print(" This Code is a test code for newly defined CLASS Named 'Date' >>>")

dd, mm, yyyy = input('Enter a date in this form - dd,mm,yyyy   >>:  ').split(',')
d1 = Date(int(dd), int(mm), int(yyyy))
d2 = Date(1,1,2000)
if d1.valid():
    print('The Day you Entered is >>:  ', d1)
    print('The order of the day in the year is  >>:  ', d1.order())
    if d1.leap(): 
        print('The year of the date you entered is <<LEAP YEAR>>')
    else :
        print('The year of the date you entered is <<NOT A LEAP YEAR>>')

    add = int(input('Enter a number to add to the Date you Entered  >>:  '))
    d2 = d1 + add
    print ('This Date >>:  ', d2, '  >>:is after the date you Entered by',add)
    dd, mm, yyyy = input('Enter First Date in this form - dd,mm,yyyy   >>:  ').split(',')
    d3 = Date(int(dd), int(mm), int(yyyy))
    dd, mm, yyyy = input('Enter Second Date in this form - dd,mm,yyyy   >>:  ').split(',')
    d4 = Date(int(dd), int(mm), int(yyyy))
    d5 = d3 - d4
    print('The absolute difference between>>:  ',d3,'and >>:   ',d4, '===',d5)
    print('you Can use the class to compare any date with a number representing order')