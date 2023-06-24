import time
name = input("Enter Your Name to Continue : ")
time.sleep(0.2)
print()
print("Hi ",name," Please take a moment to read game rules below ,")
print()
time.sleep(2)
print("------------Game Rules------------")
print()
print(" * You will be provided with 5 information about a number \n * You have to identify and input the correct number \n * you have 3 hints")
print()
time.sleep(2)

print('------------Level 1------------ ') # Answer = 16
print()
print('*This Number is located Between 0 and 20')
print('*Power of this number is greater than 200')
print('*This is divisible by 2')
print()
answer = int(input('Enter Your Answer : '))
x = int(0)
if answer != 16:
    while x<3:
        if answer < 16:
            print()
            print(answer,' is less than the number')
        else:
            print()
            print(answer, ' is greater than the number')
        x = x + 1
        print()
        answer = int(input('Enter Your New Answer : '))
        if answer == 16:
            x = 3
        time.sleep(0.2)
if answer != 16:
    print(name,', You have failed the Level 1, You cannot move to the Level 2 ')
    time.sleep(2)
    import sys
    sys.exit()
else:
    print('Congratulations ',name,'! You have Successfully completed the Level 1.\n Let us Move to the Next Level')
    print()
    print('Loading level 2 ...')
    time.sleep(5)
    import os
    os.system('cls')
 
    print('------------Level 2------------ ') # asnwer = 512
    print()
    print('This Number is Located Between 100 and 1100 ')
    print('Cubc root of this number is divisable by 2')
    print('Last digit of this Number is not 0')
    print()
    answer = int(input('Enter Your Answer : '))
    x = int(0)
    if answer != 512:
        while x<3:
            if answer < 512:
                print()
                print(answer,' is less than the number')
            else:
                print()
                print(answer, ' is greater than the number')
            x = x+1
            print()
            answer = int(input('Enter Your Answer : '))
            if answer == 512:
                x = 3
            time.sleep(0.2)

        if answer != 512:
            print(name,', You have failed the Level 2, You cannot move to the Level 3 ')
            time.sleep(2)
            import sys
            sys.exit()
        else:
            print('Congratulations ',name,'! You have Successfully completed the Level 2.\n Let us Move to the Next Level')
            print()
            print('Loading level 3 ...')
            time.sleep(5)
            import os
            os.system('cls')


print('------------Level 3------------ ') #answer = 5625
print()
print('*This Number is located Between 5000 and 10000')
print('*Squre root of this number is divisible by 15')
print('*Last Digit of this number is 5')
print()
answer = int(input('Enter Your Answer : '))
x = int(0)
if answer != 5625:
    while x<3:
        if answer < 5625:
            print()
            print(answer,' is less than the number')
        else:
            print()
            print(answer, ' is greater than the number')
        x = x + 1
        print()
        answer = int(input('Enter Your New Answer : '))
        if answer == 5625:
            x = 3
        time.sleep(0.2)
if answer != 5625:
    print(name,', You have failed the Level 3,')
    time.sleep(0.3)
    print('Good Bye',name,"!")
    time.sleep(2)
    import sys
    sys.exit()
else:
    print('Congratulations ',name,'! You have Successfully completed the Level 3.')
    time.sleep(0.3)
    print("Good Bye",name,"!")
    time.sleep(2)
    import sys
    sys.exit()


            

            






    



    

    


    




        




      
