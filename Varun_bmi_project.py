
def BMI(height, weight):
    '''(float, float)-----> float

    This current function converts height from feet to inches and then calculates body mass Index and rounds the value to 2 decimal points

    >>>BMI(2,20)
    24.41
    '''
    height_inches=height*12
    bmi= (weight/(height_inches*height_inches))*703
    bmi=round(bmi, 2)
    if gender=="M":
        if (age==2 and bmi <= 14.8) or (age==3 and bmi <= 14.4) or (age==4 and bmi <= 14) or (age==5 and bmi <= 13.8) :
            print("Child's BMI is ", bmi)
            print("BMI is below 5th percentile")
            print("Child's Weight Status: Underweight")
            print("Advice: Please consult your family physician for a referral to a dietician to assess what your child needs")
        elif (age==2 and bmi > 14.8 and bmi <= 18.2) or (age==3 and bmi > 14.4 and bmi <= 17.4) or (age==4 and bmi > 14 and bmi <= 17) or (age==5 and bmi > 13.8 and bmi <= 16.8) :
            print("Child's BMI is ", bmi)
            print("BMI is between 5th percentile and 85th percentile")
            print("Child's Weight Status: Normal")
            print("Advice: Your child is perfectly alright. Maintain the same eating habits and exercise")
        elif (age==2 and bmi > 18.2 and bmi <= 19.3) or (age==3 and bmi > 17.4 and bmi <= 18.2) or (age==4 and bmi > 17 and bmi <= 17.8) or (age==5 and bmi > 16.8 and bmi <= 18) :
            print("Child's BMI is ", bmi)
            print("BMI is between 85th percentile and 95th percentile")
            print("Child's Weight Status: Overweight")
            print ("Advice: Please consult your physician for better advice")
        elif (age==2 and bmi > 19.3) or (age==3 and bmi >18.2) or (age==4 and bmi > 17.8) or (age==5 and bmi > 18) :
            print("Child's BMI is ", bmi)
            print("BMI is greater than or equal to 95th percentile")
            print("Child's Weight Status: Obese")
            print ("Advice: Your child is at high risk. Contact your physician immediately")
        else: 
            print("This calculator is only for children between 2 to 5 years of age") 
    elif gender=="F":
        if (age==2 and bmi <= 14.4) or (age==3 and bmi <= 14) or (age==4 and bmi <= 13.8) or (age==5 and bmi <= 13.6) :
            print("Child's BMI is ", bmi)
            print("BMI is below 5th percentile")
            print("Child's Weight Status: Underweight")
            print("Advice: Please consult your family physician for a referral to a dietitian to assess what your child needs")
        elif (age==2 and bmi > 14.4 and bmi <= 18) or (age==3 and bmi > 14 and bmi <= 17.2) or (age==4 and bmi > 13.8 and bmi <= 16.8) or (age==5 and bmi > 13.6 and bmi <= 16.8) :
            print("Child's BMI is ", bmi)
            print("BMI is between 5th percentile and 85th percentile")
            print("Child's Weight Status: Normal")
            print("Advice: Your child is perfectly alright. Maintain the same eating habits and exercise")
        elif (age==2 and bmi > 18 and bmi <= 19) or (age==3 and bmi > 17.2 and bmi <= 18.2) or (age==4 and bmi > 16.8 and bmi <= 18) or (age==5 and bmi > 16.8 and bmi <= 18.2) :
            print("Child's BMI is ", bmi)
            print("BMI is between 85th percentile and 95th percentile")
            print("Child's Weight Status: Overweight")
            print ("Advice: Please consult your physician for better advice")
        elif (age==2 and bmi > 19) or (age==3 and bmi >18.2) or (age==4 and bmi > 18) or (age==5 and bmi > 18.2) :
            print("Child's BMI is ", bmi)
            print("BMI is greater than or equal to 95th percentile")
            print("Child's Weight Status: Obese")
            print ("Advice: Your child is at high risk. Contact your physician immediately")
        else: 
            print("This calculator is only for children between 2 to 5 years of age") 
    

print ("This program will calculate the BMI for children between 2 to 5 years and also provides appropriate advice\n")    

age=input("Please Enter Child's Age (in years): ")
gender=str(input("Please Enter Child's gender (M/F): "))
height=input("Please Enter Height (in feets): ")
weight=input("Please Enter Weight (in pounds): ")

age=int(age)
height=float(height)
weight=float(weight)

BMI= BMI(height, weight)
