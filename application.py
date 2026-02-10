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
ct_list={}
section_no=int(input("Enter Number Of Sections in your class: "))
i=0
if i<section_no:
    name=input("Enter Class Teacher: ")
    name=name.upper()
    section=input("Enter Section: ")
    ct_list[name]=section
    i=i+1
print("---Class Teacher Section---")
ct_name=input("Name of the Class teacher: ")
verify=ct_list.get(ct_name.upper(),"Not Found")
if verify=="Not Found":
    print("Verification Unsuccessful")
    exit
else:
    ct_section=verify
    print("Verification Successful")
stud_name=input("Enter Student Name: ")
stud_rollno=int(input("Enter Student Roll Number: "))
credit_subject=[]
credit_subject_code=[]
credit_subject_credit=[]
credit_cie1=[]
credit_cie2=[]
credit_subject_lab_record=[]
credit_assignment=[]
credit_lab_exam=[]
credit_exe=[]
comp_subject=[]
comp_subject_code=[]
comp_cie1=[]
comp_cie2=[]
comp_assignment=[]
no_subject=int(input("Enter Number of Subjects: "))
i=0
while i<no_subject:
    subject=input("Enter the Subject: ")
    subject_code=input("Enter Subject Code: ")
    subject_credit=input("Enter Subject Credit: ")
    if subject_credit>0:
        credit_subject.append(subject)
        credit_subject_code.append(subject_code)
        credit_subject_credit.append(subject_credit)
        marks=int(input("Enter CIE 1 Marks(Out of 45): "))
        credit_cie1.append(marks)
        marks=int(input("Enter CIE 2 Marks(Out of 45): "))
        credit_cie2.append(marks)
        marks=int(input("Enter Lab Record Marks(Out of 10): "))
        credit_subject_lab_record.append(marks)
        marks=int(input("Enter marks of assignment(Out of 10): "))
        credit_assignment.append(marks)
        marks=int(input("Enter Lab Exam Marks(Out of 15): "))
        credit_lab_exam.append(marks)
        marks=int(input("Enter SEE Marks(Out of 100): "))
        credit_exe.append(marks)
    else:
        comp_subject.append(subject)
        comp_subject_code.append(subject_code)
        marks=int(input("Enter your CIE 1 Marks: (Out of 30) "))
        comp_cie1.append(marks)
        marks=int(input("Enter CIE 2 marks: (Out of 30) "))
        comp_cie2.append(marks)
        marks=int(input("Enter Assignment marks: (Out of 50) "))
        comp_assignment.append(marks)
print("---STUDENT'S PROFILE---")
print("Name: ",stud_name)
print("Roll Number: ",stud_rollno)
print("Section: ",ct_section)
print("Class Teacher: ",ct_name)
print("PART-A: Credit Subjects")
sum_credit=sum(credit_subject_credit)
i=0
credit_total_marks=[]
backlog=[]
cgpa=0
while i<len(credit_subject):
    print("Subject: ",credit_subject[i])
    print("Subject Code: ",credit_subject_code[i])
    print("Subject Credit: ",credit_subject_credit[i])
    print("CIE 1 Marks: ",credit_cie1[i])
    print("CIE 2 Marks: ",credit_cie2[i])
    print("Assignment Marks: ",credit_assignment[i])
    print("Lab Record Marks: ",credit_subject_lab_record[i])
    print("Lab Exam: ",credit_lab_exam)
    print("SEE Exam Marks: ",credit_exe[i])
    marks=((credit_cie1[i]+credit_cie2[i])/6)+(credit_assignment[i])+(credit_lab_exam[i])+(credit_subject_lab_record[i])+((credit_exe)/2)
    credit_total_marks.append(marks)
    cgpa=cgpa+((marks*(credit_subject_credit[i]/sum_credit))*0.1)
    print("Total Marks: ",credit_total_marks[i])
    if credit_total_marks[i]<40:
        print("Student Failed")
        backlog.append(credit_subject[i])
    else:
        print("Student Passed")
    i=i+1
print("Part B: Compulsory Subjects")
i=0
while i<len(comp_subject):
    print("Subject: ", comp_subject[i])
    print("Subject Code: ",comp_subject_code[i])
    print("CIE 1: ", comp_cie1[i])
    print("CIE 2: ",comp_cie2[i])
    print("Assignment: ",comp_assignment[i])
    marks=((comp_cie1[i]+comp_cie2[i])/60)*50
    ext_marks=marks+comp_assignment[i]
    if ext_marks>40:
        print("Your Student Passed")
    else:
        print("Your Student failed")
    i=i+1
if len(backlog)>0:
    print("You have backlog in following subjects: ")
    print(backlog)
    print("Your CGPA: ",cgpa)
else:
    print("Congratulation. You do not have any backlog.")
    print("Your CGPA: ",cgpa)




    

        
    
    






    