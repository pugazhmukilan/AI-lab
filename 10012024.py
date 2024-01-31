##PREOBLEM 1
def problem2reversethenumber():   
    number= 567894
    answer=0
    sum=0
    def reverse(number):
        an=0
        for i in range (len(str(number))):
            
            rem=number%10
            div= number /10
            
            
            #remainder=(number-rev)/10
            an=rem+(an*(10))
            
            number =int(div)
            
        
        return an;
        
    def sumofnumbers(number):
        sum=0
        print("process",number)
            
        
        for i in range (len(str(number))):    
            rem=number%10
            div =int(number/10)
            number =div
            sum=sum+rem
        if (len(str(sum)))>1 :
                
            return sumofnumbers(sum);
        else:
            return sum;
            
            
            
            
            
    
    print("========================================================")
    print("         REVERSING AND ADD THE DIGITS OF NUMBER         ")       
    print("========================================================")
    answer = reverse(number)

    print("reverse of the number is ",answer,"\n")
    sum=sumofnumbers(answer)
    print("the sum of the reverse number is ",sum)

##PROBLEM 2
def amstrong(number):
    original=number
    sum=0
    for i in range(len(str(number))):
        rem=number%10;
        cube= rem**3
        div =int(number/10)
        number =div
        sum=sum+cube
        print(sum)
    if sum==original:
        print("true")
        return True;
    else:
        print("false")
        return False;
print("========================================================")
print("         CHECKING 153 IS AMSTRONG NUMBER OR NOT         ")       
print("========================================================") 
amstrong(153)

##PROBLEM 3
def krishnamoorthi_number(number):
    def fac(num):
        factorial=1
        n=1
        
        for i in range(num):
            factorial=n*factorial
            n+=1
        
        return factorial;    
        
    original =number
    sum=0
    
    for i in range(len(str(number))):
        rem=number%10;
        fac1= fac(rem)
        
        div =int(number/10)
        number =div
        sum=sum+fac1
        
    if sum==original:
        print("true")
        return True;
    else:
        print("false")
        return False;
print("========================================================")
print("     CHECKING 145 IS KRISHNAMOORTHI NUMBER OR NOT       ")       
print("========================================================")    
krishnamoorthi_number(145)


##PROBLEM 4
print("MULTIPLICATION OF TWO NUMBERS WITHOUT USING THE OPERATOR---- 3x9")
sum=0
for i in range (1,9):
    sum+=3
print("multiplication value is----",sum)
    
