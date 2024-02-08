def collatz(Num1):
    while(Num1!=1):
        print(Num1,end=" ")

        if(Num1%2==0):
            Num1 =  Num1//2
        else:
            Num1 =  3 * Num1 + 1 
    print(Num1)

print("Enter the Number: ")
x = int(input())
collatz(x)