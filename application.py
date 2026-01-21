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
subject1=input("Enter Subject 1 Name: ")
subject_code1=int(input("Enter Subject 1 Code: "))
subject_credit1=int(input("Enter Subject 1 Credit: "))
if subject_credit1>0:
    print("This is Credit Course")
    cie11=int(input("Enter CIE 1 marks (Out of 45): "))
    cie21=int(input("Enter CIE 2 marks (Out of 45): "))
    avg_cie1=((cie11+cie21)/90)*15
    lab_record1=int(input("Enter Practical Record Submission Marks(Out of 10): "))
    assignment1=int(input("Enter Assignment Marks(out of 10): "))
    lab1=int(input("Enter Lab Marks(out of 15): "))
    int_total1=avg_cie1+lab_record1+assignment1+lab1
    ext1=int(input("Enter SEE Marks: "))
    total1=int_total1+ext1
else:
    print("This is Non-credit Mandatory Subject.")
    cie_11=int(input("Enter CIE 1 marks(Out of 30): "))
    cie_21=int(input("Enter CIE 2 marks(Out of 30)"))
    int_total1=((cie_11+cie_21)/60)*50
    assignment1=int(input("Enter Assignment 1: (Out of 10)"))
    total1=int_total1+(assignment1*5)
subject2=input("Enter Subject 1 Name: ")
subject_code2=int(input("Enter Subject 1 Code: "))
subject_credit2=int(input("Enter Subject 1 Credit: "))
if subject_credit2>0:
    print("This is Credit Course")
    cie12=int(input("Enter CIE 1 marks (Out of 45): "))
    cie22=int(input("Enter CIE 2 marks (Out of 45): "))
    avg_cie2=((cie11+cie21)/90)*15
    lab_record2=int(input("Enter Practical Record Submission Marks(Out of 10): "))
    assignment2=int(input("Enter Assignment Marks(out of 10): "))
    lab2=int(input("Enter Lab Marks(out of 15): "))
    int_total2=avg_cie2+lab_record2+assignment2+lab2
    ext2=int(input("Enter SEE Marks: "))
    total2=int_total2+ext2
else:
    print("This is Non-credit Mandatory Subject.")
    cie_12=int(input("Enter CIE 1 marks(Out of 30): "))
    cie_22=int(input("Enter CIE 2 marks(Out of 30)"))
    int_total2=((cie_12+cie_22)/60)*50
    assignment2=int(input("Enter Assignment 2: (Out of 10)"))
    total2=int_total2+(assignment2*5)
subject3=input("Enter Subject 1 Name: ")
subject_code3=int(input("Enter Subject 1 Code: "))
subject_credit3=int(input("Enter Subject 1 Credit: "))
if subject_credit3>0:
    print("This is Credit Course")
    cie13=int(input("Enter CIE 1 marks (Out of 45): "))
    cie23=int(input("Enter CIE 2 marks (Out of 45): "))
    avg_cie3=((cie13+cie23)/90)*15
    lab_record3=int(input("Enter Practical Record Submission Marks(Out of 10): "))
    assignment3=int(input("Enter Assignment Marks(out of 10): "))
    lab3=int(input("Enter Lab Marks(out of 15): "))
    int_total3=avg_cie3+lab_record3+assignment3+lab3
    ext3=int(input("Enter SEE Marks: "))
    total3=int_total3+ext3
else:
    print("This is Non-credit Mandatory Subject.")
    cie_13=int(input("Enter CIE 1 marks(Out of 30): "))
    cie_23=int(input("Enter CIE 2 marks(Out of 30)"))
    int_total3=((cie_13+cie_23)/60)*50
    assignment3=int(input("Enter Assignment 1: (Out of 10)"))
    total3=int_total3+(assignment3*5)
subject4=input("Enter Subject 1 Name: ")
subject_code4=int(input("Enter Subject 1 Code: "))
subject_credit4=int(input("Enter Subject 1 Credit: "))
if subject_credit4>0:
    print("This is Credit Course")
    cie14=int(input("Enter CIE 1 marks (Out of 45): "))
    cie24=int(input("Enter CIE 2 marks (Out of 45): "))
    avg_cie4=((cie14+cie24)/90)*15
    lab_record4=int(input("Enter Practical Record Submission Marks(Out of 10): "))
    assignment4=int(input("Enter Assignment Marks(out of 10): "))
    lab4=int(input("Enter Lab Marks(out of 15): "))
    int_total4=avg_cie4+lab_record4+assignment4+lab4
    ext4=int(input("Enter SEE Marks: "))
    total4=int_total4+ext4
else:
    print("This is Non-credit Mandatory Subject.")
    cie14=int(input("Enter CIE 1 marks(Out of 30): "))
    cie_24=int(input("Enter CIE 2 marks(Out of 30)"))
    int_total4=((cie_11+cie_21)/60)*50
    assignment4=int(input("Enter Assignment 1: (Out of 10)"))
    total4=int_total4+(assignment4*5)
subject5=input("Enter Subject 1 Name: ")
subject_code5=int(input("Enter Subject 1 Code: "))
subject_credit5=int(input("Enter Subject 1 Credit: "))
if subject_credit5>0:
    print("This is Credit Course")
    cie15=int(input("Enter CIE 1 marks (Out of 45): "))
    cie25=int(input("Enter CIE 2 marks (Out of 45): "))
    avg_cie5=((cie15+cie25)/90)*15
    lab_record5=int(input("Enter Practical Record Submission Marks(Out of 10): "))
    assignment5=int(input("Enter Assignment Marks(out of 10): "))
    lab5=int(input("Enter Lab Marks(out of 15): "))
    int_total5=avg_cie5+lab_record5+assignment5+lab5
    ext5=int(input("Enter SEE Marks: "))
    total5=int_total5+ext5
else:
    print("This is Non-credit Mandatory Subject.")
    cie_15=int(input("Enter CIE 1 marks(Out of 30): "))
    cie_25=int(input("Enter CIE 2 marks(Out of 30)"))
    int_total5=((cie_15+cie_25)/60)*50
    assignment5=int(input("Enter Assignment 5: (Out of 10)"))
    total5=int_total5+(assignment5*5)
subject6=input("Enter Subject 1 Name: ")
subject_code6=int(input("Enter Subject 1 Code: "))
subject_credit6=int(input("Enter Subject 1 Credit: "))
if subject_credit6>0:
    print("This is Credit Course")
    cie16=int(input("Enter CIE 1 marks (Out of 45): "))
    cie26=int(input("Enter CIE 2 marks (Out of 45): "))
    avg_cie6=((cie16+cie26)/90)*15
    lab_record6=int(input("Enter Practical Record Submission Marks(Out of 10): "))
    assignment6=int(input("Enter Assignment Marks(out of 10): "))
    lab6=int(input("Enter Lab Marks(out of 15): "))
    int_total6=avg_cie6+lab_record6+assignment6+lab6
    ext6=int(input("Enter SEE Marks: "))
    total6=int_total6+ext6
else:
    print("This is Non-credit Mandatory Subject.")
    cie_16=int(input("Enter CIE 1 marks(Out of 30): "))
    cie_26=int(input("Enter CIE 2 marks(Out of 30)"))
    int_total6=((cie_16+cie_26)/60)*50
    assignment6=int(input("Enter Assignment 1: (Out of 10)"))
    total6=int_total6+(assignment6*5)
subject7=input("Enter Subject 1 Name: ")
subject_code7=int(input("Enter Subject 1 Code: "))
subject_credit7=int(input("Enter Subject 1 Credit: "))
if subject_credit7>0:
    print("This is Credit Course")
    cie17=int(input("Enter CIE 1 marks (Out of 45): "))
    cie27=int(input("Enter CIE 2 marks (Out of 45): "))
    avg_cie7=((cie11+cie21)/90)*15
    lab_record7=int(input("Enter Practical Record Submission Marks(Out of 10): "))
    assignment7=int(input("Enter Assignment Marks(out of 10): "))
    lab7=int(input("Enter Lab Marks(out of 15): "))
    int_total7=avg_cie7+lab_record7+assignment7+lab7
    ext7=int(input("Enter SEE Marks: "))
    total7=int_total7+ext7
else:
    print("This is Non-credit Mandatory Subject.")
    cie_17=int(input("Enter CIE 1 marks(Out of 30): "))
    cie_27=int(input("Enter CIE 2 marks(Out of 30)"))
    int_total7=((cie_17+cie_27)/60)*50
    assignment7=int(input("Enter Assignment 1: (Out of 10)"))
    total7=int_total7+(assignment7*5)
subject8=input("Enter Subject 1 Name: ")
subject_code8=int(input("Enter Subject 1 Code: "))
subject_credit8=int(input("Enter Subject 1 Credit: "))
if subject_credit8>0:
    print("This is Credit Course")
    cie18=int(input("Enter CIE 1 marks (Out of 45): "))
    cie28=int(input("Enter CIE 2 marks (Out of 45): "))
    avg_cie8=((cie18+cie28)/90)*15
    lab_record8=int(input("Enter Practical Record Submission Marks(Out of 10): "))
    assignment8=int(input("Enter Assignment Marks(out of 10): "))
    lab8=int(input("Enter Lab Marks(out of 15): "))
    int_total8=avg_cie8+lab_record8+assignment8+lab8
    ext8=int(input("Enter SEE Marks: "))
    total8=int_total8+ext8
else:
    print("This is Non-credit Mandatory Subject.")
    cie_18=int(input("Enter CIE 1 marks(Out of 30): "))
    cie_28=int(input("Enter CIE 2 marks(Out of 30)"))
    int_total8=((cie_18+cie_28)/60)*50
    assignment8=int(input("Enter Assignment 1: (Out of 10)"))
    total8=int_total8+(assignment8*5)
subject9=input("Enter Subject 1 Name: ")
subject_code9=int(input("Enter Subject 1 Code: "))
subject_credit9=int(input("Enter Subject 1 Credit: "))
if subject_credit9>0:
    print("This is Credit Course")
    cie19=int(input("Enter CIE 1 marks (Out of 45): "))
    cie29=int(input("Enter CIE 2 marks (Out of 45): "))
    avg_cie9=((cie19+cie29)/90)*15
    lab_record9=int(input("Enter Practical Record Submission Marks(Out of 10): "))
    assignment9=int(input("Enter Assignment Marks(out of 10): "))
    lab9=int(input("Enter Lab Marks(out of 15): "))
    int_total9=avg_cie9+lab_record9+assignment9+lab9
    ext9=int(input("Enter SEE Marks: "))
    total9=int_total9+ext9
else:
    print("This is Non-credit Mandatory Subject.")
    cie_19=int(input("Enter CIE 1 marks(Out of 30): "))
    cie_29=int(input("Enter CIE 2 marks(Out of 30)"))
    int_total9=((cie_19+cie_29)/60)*50
    assignment9=int(input("Enter Assignment 1: (Out of 10)"))
    total9=int_total9+(assignment9*5)
subject10=input("Enter Subject 1 Name: ")
subject_code10=int(input("Enter Subject 1 Code: "))
subject_credit10=int(input("Enter Subject 1 Credit: "))
if subject_credit10>0:
    print("This is Credit Course")
    cie110=int(input("Enter CIE 1 marks (Out of 45): "))
    cie210=int(input("Enter CIE 2 marks (Out of 45): "))
    avg_cie10=((cie110+cie210)/90)*15
    lab_record10=int(input("Enter Practical Record Submission Marks(Out of 10): "))
    assignment10=int(input("Enter Assignment Marks(out of 10): "))
    lab10=int(input("Enter Lab Marks(out of 15): "))
    int_total10=avg_cie10+lab_record10+assignment10+lab10
    ext10=int(input("Enter SEE Marks: "))
    total10=int_total10+ext10
else:
    print("This is Non-credit Mandatory Subject.")
    cie_110=int(input("Enter CIE 1 marks(Out of 30): "))
    cie_210=int(input("Enter CIE 2 marks(Out of 30)"))
    int_total10=((cie_110+cie_210)/60)*50
    assignment10=int(input("Enter Assignment 1: (Out of 10)"))
    total10=int_total10+(assignment10*5)
print("---STUDENT'S SECTION---")
i=1
while i==1:
    user_section=input("Enter your Section: ")
    if user_section==ct_section:
        break
    else:
        print("Information about the given section is not present.")
i=1
while i==1:
    user_name=input("Enter Name: ")
    if user_name.lower()==stud_name.lower():
        break
    else:
        print("Information not available now")
i=1
while i==1:
    user_rollno=int(input("Enter Roll Number: "))
    if user_rollno==stud_rollno:
        break
    else:
        print("Invalid Roll Number")
print("Student Name: ",stud_name)
print("Section: ",ct_section)
print("Roll Number: ",stud_rollno)
print("Subject 1",subject1)
print("Subject Code: ",subject_code1)
print("Subject Credit: ",subject_credit1)
if subject_credit1>0:
    print("CIE 1: ",cie11)
    print("CIE-2: ",cie21)
    print("Average: ",avg_cie1)
    print("Lab Record: ",lab_record1)
    print("Assignment: ",assignment1)
    print("Lab Exam: ",lab1)
    print("Internals: ",int_total1)
    print("SEE Exam: ",ext1)
    print("Total: ",total1)
    if total1>40:
        print("Course Passed")
    else:
        print("Course Failed")
else: 
    print("CIE-1: ",cie11)
    print("CIE-2: ",cie21)
    print("Internals: ",int_total1)
    print("Assignment: ",assignment1)
    print("Totals: ",total1)
    if total1>40:
        print("Course Passed")
    else:
        print("Course Failed")
print("Subject 2",subject2)
print("Subject Code: ",subject_code2)
print("Subject Credit: ",subject_credit2)
if subject_credit2>0:
    print("CIE 1: ",cie12)
    print("CIE-2: ",cie22)
    print("Average: ",avg_cie2)
    print("Lab Record: ",lab_record2)
    print("Assignment: ",assignment2)
    print("Lab Exam: ",lab2)
    print("Internals: ",int_total2)
    print("SEE Exam: ",ext2)
    print("Total: ",total2)
    if total2>40:
        print("Course Passed")
    else:
        print("Course Failed")
else: 
    print("CIE-1: ",cie12)
    print("CIE-2: ",cie22)
    print("Internals: ",int_total2)
    print("Assignment: ",assignment2)
    print("Totals: ",total2)
    if total2>40:
        print("Course Passed")
    else:
        print("Course Failed")
print("Subject 3",subject3)
print("Subject Code: ",subject_code3)
print("Subject Credit: ",subject_credit3)
if subject_credit3>0:
    print("CIE 1: ",cie13)
    print("CIE-2: ",cie23)
    print("Average: ",avg_cie3)
    print("Lab Record: ",lab_record3)
    print("Assignment: ",assignment3)
    print("Lab Exam: ",lab3)
    print("Internals: ",int_total3)
    print("SEE Exam: ",ext3)
    print("Total: ",total3)
    if total3>40:
        print("Course Passed")
    else:
        print("Course Failed")
else: 
    print("CIE-1: ",cie13)
    print("CIE-2: ",cie23)
    print("Internals: ",int_total3)
    print("Assignment: ",assignment3)
    print("Totals: ",total3)
    if total3>40:
        print("Course Passed")
    else:
        print("Course Failed")
print("Subject 4",subject4)
print("Subject Code: ",subject_code4)
print("Subject Credit: ",subject_credit4)
if subject_credit4>0:
    print("CIE 1: ",cie14)
    print("CIE-2: ",cie24)
    print("Average: ",avg_cie4)
    print("Lab Record: ",lab_record4)
    print("Assignment: ",assignment4)
    print("Lab Exam: ",lab4)
    print("Internals: ",int_total4)
    print("SEE Exam: ",ext4)
    print("Total: ",total4)
    if total4>40:
        print("Course Passed")
    else:
        print("Course Failed")
else: 
    print("CIE-1: ",cie14)
    print("CIE-2: ",cie24)
    print("Internals: ",int_total4)
    print("Assignment: ",assignment4)
    print("Totals: ",total4)
    if total4>40:
        print("Course Passed")
    else:
        print("Course Failed")
print("Subject 3",subject5)
print("Subject Code: ",subject_code5)
print("Subject Credit: ",subject_credit5)
if subject_credit5>0:
    print("CIE 1: ",cie15)
    print("CIE-2: ",cie25)
    print("Average: ",avg_cie5)
    print("Lab Record: ",lab_record5)
    print("Assignment: ",assignment5)
    print("Lab Exam: ",lab5)
    print("Internals: ",int_total5)
    print("SEE Exam: ",ext5)
    print("Total: ",total5)
    if total5>40:
        print("Course Passed")
    else:
        print("Course Failed")
else: 
    print("CIE-1: ",cie15)
    print("CIE-2: ",cie25)
    print("Internals: ",int_total5)
    print("Assignment: ",assignment5)
    print("Totals: ",total5)
    if total5>40:
        print("Course Passed")
    else:
        print("Course Failed")
print("Subject 3",subject3)
print("Subject Code: ",subject_code3)
print("Subject Credit: ",subject_credit3)
if subject_credit3>0:
    print("CIE 1: ",cie16)
    print("CIE-2: ",cie26)
    print("Average: ",avg_cie6)
    print("Lab Record: ",lab_record6)
    print("Assignment: ",assignment6)
    print("Lab Exam: ",lab6)
    print("Internals: ",int_total6)
    print("SEE Exam: ",ext6)
    print("Total: ",total6)
    if total6>40:
        print("Course Passed")
    else:
        print("Course Failed")
else: 
    print("CIE-1: ",cie16)
    print("CIE-2: ",cie26)
    print("Internals: ",int_total6)
    print("Assignment: ",assignment6)
    print("Totals: ",total6)
    if total6>40:
        print("Course Passed")
    else:
        print("Course Failed")
print("Subject 3",subject7)
print("Subject Code: ",subject_code7)
print("Subject Credit: ",subject_credit7)
if subject_credit7>0:
    print("CIE 1: ",cie17)
    print("CIE-2: ",cie27)
    print("Average: ",avg_cie7)
    print("Lab Record: ",lab_record7)
    print("Assignment: ",assignment7)
    print("Lab Exam: ",lab7)
    print("Internals: ",int_total7)
    print("SEE Exam: ",ext7)
    print("Total: ",total7)
    if total7>40:
        print("Course Passed")
    else:
        print("Course Failed")
else: 
    print("CIE-1: ",cie17)
    print("CIE-2: ",cie27)
    print("Internals: ",int_total7)
    print("Assignment: ",assignment7)
    print("Totals: ",total7)
    if total7>40:
        print("Course Passed")
    else:
        print("Course Failed")
print("Subject 8",subject8)
print("Subject Code: ",subject_code8)
print("Subject Credit: ",subject_credit8)
if subject_credit8>0:
    print("CIE 1: ",cie18)
    print("CIE-2: ",cie28)
    print("Average: ",avg_cie8)
    print("Lab Record: ",lab_record8)
    print("Assignment: ",assignment8)
    print("Lab Exam: ",lab8)
    print("Internals: ",int_total8)
    print("SEE Exam: ",ext8)
    print("Total: ",total8)
    if total8>40:
        print("Course Passed")
    else:
        print("Course Failed")
else: 
    print("CIE-1: ",cie18)
    print("CIE-2: ",cie28)
    print("Internals: ",int_total8)
    print("Assignment: ",assignment8)
    print("Totals: ",total8)
    if total8>40:
        print("Course Passed")
    else:
        print("Course Failed")
print("Subject 9",subject9)
print("Subject Code: ",subject_code9)
print("Subject Credit: ",subject_credit9)
if subject_credit9>0:
    print("CIE 1: ",cie19)
    print("CIE-2: ",cie29)
    print("Average: ",avg_cie9)
    print("Lab Record: ",lab_record9)
    print("Assignment: ",assignment9)
    print("Lab Exam: ",lab9)
    print("Internals: ",int_total9)
    print("SEE Exam: ",ext9)
    print("Total: ",total9)
    if total9>40:
        print("Course Passed")
    else:
        print("Course Failed")
else: 
    print("CIE-1: ",cie19)
    print("CIE-2: ",cie29)
    print("Internals: ",int_total9)
    print("Assignment: ",assignment9)
    print("Totals: ",total9)
    if total9>40:
        print("Course Passed")
    else:
        print("Course Failed")
print("Subject 3",subject10)
print("Subject Code: ",subject_code10)
print("Subject Credit: ",subject_credit10)
if subject_credit10>0:
    print("CIE 1: ",cie110)
    print("CIE-2: ",cie210)
    print("Average: ",avg_cie10)
    print("Lab Record: ",lab_record10)
    print("Assignment: ",assignment10)
    print("Lab Exam: ",lab10)
    print("Internals: ",int_total10)
    print("SEE Exam: ",ext10)
    print("Total: ",total10)
    if total10>40:
        print("Course Passed")
    else:
        print("Course Failed")
else: 
    print("CIE-1: ",cie110)
    print("CIE-2: ",cie210)
    print("Internals: ",int_total10)
    print("Assignment: ",assignment10)
    print("Totals: ",total10)
    if total10>40:
        print("Course Passed")
    else:
        print("Course Failed")
