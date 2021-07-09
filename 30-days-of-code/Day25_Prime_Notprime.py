#Prime and Not Prime

# Enter your code here. Read input from STDIN. Print output to STDOUT
##T = int(input())
##def prime(n):
##    for i in range(2,int(n**0.5)+1):
##        if n%i==0:
##            return False
##    return True
##for _ in range(T):
##    n = int(input())
##    print("Prime" if n>=2 and prime(n) else "Not prime")



#Way 2

T = int(input())  
for _ in range(T):
    n = int(input())
    count=0
    for i in range(2,n):
        if n%i==0:
            count+=1
    print("Not prime" if count>1 else "Prime")
