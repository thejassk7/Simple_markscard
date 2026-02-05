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
    password=input("Enter Password: ")
    confirm=input("Confirm Password: ")
    if password==confirm:
        print("School Profile Created Successfully")
        i=0
    else:
        print("Invalid Entry. Try again.")
print("---Class Teacher's Section---")
i=0
while i<2:
    ct_password=input("Enter password: ")
    if ct_password==password:
        print("Verified Password")
        break
    else:
        print("Try again. You have",2-i,"attempts left.")
        i=i+1
if i>2:
    exit
i=0
while i<2:
    ct_code=int(input("Enter College Code: "))
    if ct_code==code:
        print("Verfied Successfully")
        break
    else:
        print("Try again. You have", 2-i,"attempts left.")
        i=i+1
if i>2:
    exit
ct_name=input("Name of the teacher: ")
ct_section=input("Enter Section: ")
stud_name=input("Enter Student Name: ")
stud_rollno=int(input("Enter Student Roll Number: "))
no_subject=int(input("Enter number of Subjects: "))
i=0
if i<n:
    subject_credit=int(input(""))