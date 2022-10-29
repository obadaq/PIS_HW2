from main import Date
user_ch = ''
user_ch = input('''
    This Program is a Test Code for newly defined class named 'Date' if you want to Exit write 'esc'
    if you want to proceed enter anything else
    ''')
while user_ch != 'esc':
    dd, mm, yyyy = input("Enter a Date in this form dd,mm,yyyy::>>    ").split(',')
    d1 = Date(int(dd), int(mm), int(yyyy))
    print('First Date === ', d1)
    print('First Date Order ===', d1.order())
    print('Is this year leap ? >>> ', d1.leap())

    dd, mm, yyyy = input("Enter a Date in this form dd,mm,yyyy::>>    ").split(',')
    d2 = Date(int(dd), int(mm), int(yyyy))
    print('Second Date === ', d2)
    print('Second Date Order ===', d2.order())
    print('Is this year leap ? >>> ', d2.leap())

    user_ch = input('do you want to continue -c- or Exit -esc- ??>> ')
    if user_ch == 'esc': break
    
while user_ch != 'esc':
    user_ch = int(input('''what test you want to perform ??
    1. add a number to dates to know what is the next date ?
    2. subtract the first and the second dates ? 
    3. Test if First Date order > second date order?
    4. Test if First Date order < second date order?
    5. Test if First Date order >= second date order?
    6. Test if First Date order <= second date order?
    7. Test if First Date order = second date order?
    8. Test if First Date order != second date order?
    '''))

    if user_ch == 1:
        print(d1+ int(input('Enter a number to add to first Date   + [ ]   =')))
    elif user_ch == 2:
        print(d1 - d2)
    elif user_ch == 3:
        print(d1 > d2)
    elif user_ch == 4:
        print(d1 < d2)
    elif user_ch == 5:
        print(d1 >= d2)
    elif user_ch == 6:
        print(d1 <= d2)
    elif user_ch == 7:
        print(d1 == d2)
    elif user_ch == 8:
        print(d1 != d2)