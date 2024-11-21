import sys
if len(sys.argv) == 1:
    print("none")
elif len(sys.argv) >= 3:
    print("none")
else:
    letter = sys.argv[1]
    upcase = letter.upper()
    print(upcase)