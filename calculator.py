import math
#adding this to check CI
#add2 to check CI
#test3 to check CI#test 4 for CI#test7
#another test for CICD
def square_root(x):
    """Calculates the square root of a non-negative number."""
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)

def factorial(x):
    """Calculates the factorial of a non-negative integer."""
    if not isinstance(x, int) or x < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(x)

def natural_log(x):
    """Calculates the natural logarithm (ln) of a positive number."""
    if x <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers.")
    return math.log(x)

def power_function(x, b):
    """Calculates x raised to the power of b (x^b)."""
    return math.pow(x, b)

def menu():
    """Displays the menu and handles user input."""
    print("\n--- Scientific Calculator Menu ---")
    print("1. Square Root (√x)")
    print("2. Factorial (!x)")
    print("3. Natural Logarithm (ln(x))")
    print("4. Power Function (x^b)")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")

        try:
            if choice == '1':
                x = float(input("Enter number (x): "))
                print(f"Result: √{x} = {square_root(x)}")
            
            elif choice == '2':
                x = int(input("Enter non-negative integer (x): "))
                print(f"Result: {x}! = {factorial(x)}")
            
            elif choice == '3':
                x = float(input("Enter positive number (x): "))
                print(f"Result: ln({x}) = {natural_log(x)}")
            
            elif choice == '4':
                x = float(input("Enter base (x): "))
                b = float(input("Enter exponent (b): "))
                print(f"Result: {x}^{b} = {power_function(x, b)}")
            
            elif choice == '5':
                print("Exiting calculator. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()