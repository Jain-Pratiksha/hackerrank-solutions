n = int(input())
phone_book={}
for i in range(0,n):
    val = str(input()).split(' ')   
    name = val[0]
    number = int(val[1])
    phone_book[name] = number

while True:
    try:
        name = input()
        print("Not found" if name not in phone_book else name+"="+str(phone_book[name]))   
    except: break
    
