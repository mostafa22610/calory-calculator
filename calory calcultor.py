const=0
Gender = input("enter your gender:")
weight = int(input("enter your weight:"))
height = int(input("enter your height:"))
age = int(input("enter your age:"))
Sports = int(input("Enter your Activity status (1,2,3,4,5) \n 1-  you are very sedentary (little or no activity): \n 2- you are lightly active (light exercise/sports 1-3 days a week):\n 3- you are moderately active (moderate exercise/sports 3-5 days a week): \n 4- you are highly active (strenuous exercise/sports 6-7 days a week): \n5- you are hyperactive (very hard exercise/physical function sport or overtraining):"))
Bmr_male = 10*weight+6.25*height-5*age+5
Bmr_female = 10*weight+6.25*height-5*age-161

if Sports == 1:
   const = 1.2
elif Sports == 2:
    const = 1.375
elif Sports == 3:
    const = 1.55
elif Sports == 4:
    const = 1.725
elif Sports == 5:
    const = 1.9

if Gender == "male":
   result = Bmr_male*const
elif Gender == "female" :
    result = Bmr_female*const
print ("calories needed per day: ", result)
print ("If you want to gain weight:  ", result+500)
print ("If you want to lose weight:   ", result-500)
result = 0
Bmr_male = 0
Bmr_female =0

   


