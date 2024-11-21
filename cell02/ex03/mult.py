def main():
    try: 
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))

        result = first_number * second_number
        print(f"{first_number} x {second_number} = {result}")
        
        if result > 0:
            print("The result is positive.")
        elif result < 0:
            print("The result is negative.")
        else:
            print("The result is positive and negative.")  # สำหรับผลลัพธ์เป็น 0

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()
