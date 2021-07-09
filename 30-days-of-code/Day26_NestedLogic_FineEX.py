#Day26: Nested Logic

# Enter your code here. Read input from STDIN. Print output to STDOUT
rday, rmonth, ryear = [int(x) for x in input().split(" ")]
dday, dmonth, dyear = [int(x) for x in input().split(" ")]
fine = 0
if ryear > dyear:
    fine = 10000
elif ryear == dyear:   
    if rmonth > dmonth:
        fine = 500 * (rmonth - dmonth)
    elif rmonth == dmonth and rday > dday:
        fine = 15 * (rday - dday)
print(fine)
