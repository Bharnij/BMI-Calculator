# BMI calculator 

height = input("What is your height?(in any metric units)")
weight = input("WHat is your weight?(in kilograms)")

height1 = float(height)
weight1 = int(weight)

BMI = weight1 / (height1**2)

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif 25 > BMI >= 18.5:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif 30 > BMI >= 25:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif 35 > BMI >= 30:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")