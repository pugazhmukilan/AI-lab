    
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
        
        
        
        
        
        
    answer = reverse(number)

    print("reverse of the number is ",answer)
    sum=sumofnumbers(answer)
    print("the sum of the reverse number is ",sum)


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
    
amstrong(143)