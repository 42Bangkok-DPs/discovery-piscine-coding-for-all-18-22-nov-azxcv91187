def main():
    try:
        number = int(input("Enter a number: "))
        if number >0:
            print("This number is positive.")
        elif number <0:
            print("This number is negative.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
if __name__ == "__main__":
    main()