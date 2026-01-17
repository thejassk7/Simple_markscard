print("---Principal Profile---")
college=input("College Name: ")
i=1
while i<4:
    code=int(input("College Code: "))
    if code>100 and code<10000:
        break
    else:
        print("Invalid Statement. Try again.")
        i=i+1
if i>3:
    exit
i=1
while i==1:
    password=int(input("Enter Password: "))
    confirm=int(input("Confirm Password: "))
    if password==confirm:
        print("School Profile Created Successfully")
        i=0
    else:
        print("Invalid Entry. Try again.")
print("---Teacher's Section---")


