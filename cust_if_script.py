#!/usr/bin/env python3


score = float(input("Out of 100, what did you get score on the test?\n"))

if score >=90:
    print("Great, you got an A!")
elif score >= 80:
    print("Nice, you got a B!")
elif score >= 70:
    print("You got a C.")
elif score >= 60:
    print("D's get degrees")
else:
    print("Oh, no you got an F")
