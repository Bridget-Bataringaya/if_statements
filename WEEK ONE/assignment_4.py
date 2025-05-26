# Infinite loop to keep asking for valid input until successful division
while True:
    try:
        # Ask the user to input the first number
        num1 = float(input("Enter the first number: "))
        
        # Ask the user to input the second number
        num2 = float(input("Enter the second number: "))
        
        # Perform division
        result = num1 / num2
        
        # Print the result
        print(f"Result: {num1} / {num2} = {result}")
        
        # If everything goes well, break out of the loop
        break

    # Handle the case where the user enters a non-numeric value
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    
    # Handle division by zero
    except ZeroDivisionError:
        print("Division by zero is not allowed. Please enter a non-zero second number.")
