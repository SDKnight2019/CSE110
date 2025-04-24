#/DIRECTORY\################################################################################################
grade_percentage = int(input("Enter your grade percentage: "))
#/FUNC\####################################################################################################
if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"
# determine grade sign (if able) ------------------------
if letter != "A" and letter != "F":
    last_digit = grade_percentage % 10 #devide for last number, then seeing absed off that determine if its a low high or med score for that bracket
    if last_digit >= 7:
        sign = "+"
    elif last_digit < 3:
        sign = "-"
    else:
        sign = ""
else:
    sign = ""  # no sign
# special case handler ------------------------------
if letter == "A" and grade_percentage < 93:
    sign = "-"
#/PRINT STATEMENT\##############################################################################
if grade_percentage >= 70:
    print("Congratulations! You passed the course.")
else:
    print("You did not pass the course. Keep trying and you'll improve next time!")
print(f"Your final grade is: {letter}{sign}")