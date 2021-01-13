def prime_checker(number):
    isPrime=True
    if number==1:
        isPrime=False
    elif number==2:
        isPrime=True
    else: 
        for i in range(2,number+1):
            if number%i==0 and number!=i:
                isPrime=False
    if isPrime:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")
num=int(input("Check number if prime: "))
prime_checker(number=num)

#Tester
#for i in range(1,101):
#   prime_checker(number=i)