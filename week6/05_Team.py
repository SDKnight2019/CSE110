grade = float( input ( "Enter your grade percentage: " ) )

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else: 
    letter = "F"
if letter == "A" and letter != "F" :
    percentage = grade % 10
    sign = "-"
else:
     sign = ""

if letter == "A" and grade < 93:
    sign =  "-"
if grade >= 70:
    print ("Congradulations! You passed this course.")
else:
    print ( "Sorry you did not pass this class. Keep trying to pass this class, because you will get better!" )
print ( f"your final grade is: {letter}{sign}" )