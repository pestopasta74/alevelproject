import re

class TheValidation:

    def __init__(self):
        pass

    def lengthscheck(self, string, nums, option):
        # string = the string we are checking the length of
        # nums = the number we are comparing the length to
        # option = 1 for equal, 2 for greater than, 3 for less than
        if option == 1:
            if len(string) == nums:
                return True
            return False
        elif option == 2:
            if len(string) >= nums:
                return True
            return False
        elif option == 3:
            if len(string) <= nums:
                return True
            return False


    def emailcheck(self, email):
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if re.match(pattern, email):
            return True
        else:
            return False

    def passcheck(self, password):
        # Checks that the variable password has the characters necessary
        return bool(re.search(r'(?=.*\d)(?=.*[A-Z])(?=.*[+,?,#,£,%,&])', password))

    def rangecheck(self, number, lower, upper):
        # Check the value of the number to be between two other values
        return lower <= number <= upper

    def prescheck(self, inp):
        # Checks something has been inputted
        return bool(inp)

# testing
if __name__ == "__main__":
    validator = TheValidation()
    print(validator.lengthscheck("b3338", 10, 3))
    print(validator.emailcheck("dirguh@dfklj.com"))
    print(validator.passcheck("t8hareeAnonu?ms"))
    print(validator.rangecheck(23, 2, 60))
    print(validator.prescheck(""))