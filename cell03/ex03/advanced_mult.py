import sys
if len(sys.argv) > 1:
    argument = sys.argv[1]
    print("none")
else:
    for i in range (0,11):
        print("Table de", i,":", 0, i+(0*i), i+(1*i),i+(2*i),i+(3*i),i+(4*i),i+(5*i),i+(6*i),i+(7*i),i+(8*i),i+(9*i))