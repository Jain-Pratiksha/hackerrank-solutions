#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    print(max(map(len,bin(int(input()))[2:].split('0'))))

