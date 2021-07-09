#Input
##6
##riya riya@gmail.com
##julia julia@julia.me
##julia sjulia@gmail.com
##julia julia@gmail.com
##samantha samantha@gmail.com
##tanya tanya@gmail.com
##
##Output
##julia
##julia
##riya
##samantha
##tanya

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    pattern = r"@gmail\.com$"
    regex = re.compile(pattern)
    lst = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        
        emailID = first_multiple_input[1]  
        
        if regex.search(emailID):
            lst.append(firstName)
    lst.sort()
    for name in lst:
        print(name)
