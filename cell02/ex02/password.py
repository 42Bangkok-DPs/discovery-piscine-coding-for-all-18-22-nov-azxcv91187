def main():
    correct_password = "Python is awesome"
    password = input("Enter a password: ")
    if password==correct_password:
        print("Access Grantes.")
    else:
        print("Access Denied.")

if __name__ == "__main__":
    main()