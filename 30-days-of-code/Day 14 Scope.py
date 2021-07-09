class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        self.maximumDifference = 0
        self.val = 0 
        for i in range(0,len(self.__elements)):
            for j in range(1,len(self.__elements)):
                self.val = abs(a[i] - a[j])
                self.maximumDifference = max(self.val,self.maximumDifference)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
