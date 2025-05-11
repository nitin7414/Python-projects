while True:
 def power():
    sum = 0
    try:
     n = int(input('Enter the exponent: '))
     b = int(input('Enter the Base: '))
     power = b**n
     while power > 0:
        rem = power % 10
        sum+=rem
        power = power // 10
     print(f"The sum of digits of number is {sum}")
    except ValueError as val:
       print('The value is not correct!........')
 power()
 ask_user = input("Don't you wish to try again? ")
 if ask_user =='n':
    print('👋Bye....')
    break
 elif ask_user=='y':
   power()