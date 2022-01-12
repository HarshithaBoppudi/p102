print('1-addition, 2-subtraction,3-multiplication,4-division')
print('enter one of the options:')
options=int(input('your choice:'))
if options==1:
    num1=int(input('enter a number:'))
    num2=int(input('enter a number:'))
    print('sum of: ',num1,'+',num2,'=',(num1+num2))

elif options==2:
    num1=int(input('enter a number:'))
    num2=int(input('enter a number:'))
    print('subtraction of: ',num1,'-',num2,'=',(num1-num2))
    
elif options==3:
    num1=int(input('enter a number:'))
    num2=int(input('enter a number:'))
    print('multiplication of: ',num1,'*',num2,'=',(num1*num2))
    
elif options==4:
    num1=int(input('enter a number:'))
    num2=int(input('enter a number:'))
    if num2==0:
        print("undefined")
    else:
        print('division of: ',num1,'/',num2,'=',(num1/num2))

    
