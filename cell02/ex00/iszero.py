def main():
    try:
        number = int(input("Enter a number: "))
        if number == 0:
            print("This number is equal to zero.")
        else:
            print("This number is different from zero.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
