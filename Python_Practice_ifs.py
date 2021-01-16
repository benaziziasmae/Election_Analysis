temperature = int(input("What is the temperature outside?"))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#What is the score?
score = int(input("What is your test score?"))
#Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F')

#Using if-elif-else statements
#What is the score?
score = int(input("What is your test score?"))

#Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')