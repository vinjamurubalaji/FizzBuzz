
## Author : Balaji Vinjamuru
for i in range (1,100):
    ##if the number is divisible by 3 and 5 (15) print FizzBuzz; 
    if(i % 3 == 0 and i % 5 ==0):
        print('FizzBuzz')
    ##if the number is divisible by 3 print Fizz;
    elif i%3==0:
        print('Fizz')
    ##if the number is divisible by 5 print Buzz;
    elif i%5==0:
        print('Buzz')
    ## else, print the number
    else :
        print(i)
        
        
