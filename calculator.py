"""
This script is a simple calculator. 
We can perform addtion and subtraction.
"""

class Calculator:

    def calculate(self, operation, a, b):
        if operation == "add":
            return self.add(a, b)
        elif operation == "subtract":
            return self.subract(a,b)
        else:
            return "Error: Invalid operation"

    def add (self, a, b):
        #add a and b
        sum = a + b
        return sum
    
    def subtract (self, a, b):
        #subtract b from a
        difference = a-b
        return difference
    
    def main():
        
        with open("input.txt", "r") as file:
            line = file.readline().strip()
            operation, a, b = line.split()
            a, b = int(a), int(b)
            
            result = Calculator.calculate(operation, a, b)

        with open("output.txt", "w") as file:
            file.write(str(result))
    
    if __name__ == "main":
        main()




            

    

    