while True:
    try:
        num = int(input("Enter an integer: "))
        print("You entered:", num)
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
