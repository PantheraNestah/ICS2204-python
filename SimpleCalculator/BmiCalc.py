# SCT211-0071/2022 Gift Nestah

def func_bmiCalc():
  float(weight) = input("Enter weight :")
  float(height) = input("Enter height :") 
  float(bmi) = weight / (height * height)
  if (bmi < 24.0):
    print("BMI below normal")
  elif (bmi > 24.0):
    print("BMI above normal") 
  else:
    print("BMI normal")

func_bmiCalc()
