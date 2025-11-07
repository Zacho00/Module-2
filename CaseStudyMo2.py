#Zach Thomas
#CaseStudyMo2.py
#This program  will accept student names and GPAs to test what honors they qualify for
#https://github.com/Zacho00/Module-2

#variables
firstName = ''
lastName = ''
GPA = 0
terminate = 'ZZZ'

#initialize loop
while lastName != terminate:
    #receive student's first name
    firstName = input("Enter Student's first name: ")
    #receive student's last name
    lastName = input("Enter Student's last name or exit with ZZZ: ")
    if lastName == terminate:
        break
    #receive student's GPA(float)
    GPA = float(input("Enter Student's GPA: "))
    #test for Dean's List
    if GPA > 3.5:
        print(firstName, lastName, "qualifies for Dean's List.")
    #test for Honor Roll
    elif GPA > 3.25 and GPA < 3.5:
        print(firstName, lastName, "qualifies for Honor Roll.")
    else:

        print(firstName, lastName, "does not qualify for extra honors.")
