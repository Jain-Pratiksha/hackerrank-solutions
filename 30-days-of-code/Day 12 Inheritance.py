

class Student(Person):
    #   Class Constructor
    def __init__(self,firstName, lastName, idNum, scores):
        super().__init__(firstName, lastName, idNum)
        for i in scores:
            self.scores = sum(scores)
            self.scores = self.scores/len(scores)
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        if self.scores >= 90:
            return "O"
        elif self.scores >= 80 and self.scores <90:
            return "E"
        elif self.scores >= 70 and self.scores <80:
            return "A"
        elif self.scores >= 55 and self.scores <70:
            return "P"
        elif self.scores >= 40 and self.scores <55:
            return "D"
        else:
            return "T"

