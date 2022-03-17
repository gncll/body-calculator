import numpy as np

def fat_perc_male_cm_exp(abdomen, neck, height):
    abdomen_inc = abdomen / 2.54
    neck_inc = neck / (2.54)
    height_inc = height/(2.54)
    perc = (86.010 *np.log10(abdomen_inc - neck_inc)) - (70.041 *np.log10(height_inc)) + 36.76
    a= round(perc,2)
    if a>2 and a<5:
        print("Your body fat percantage is {}.".format(a))
        print("Your category is essential fat according to American Council on Exercise (ACE).")
    elif a>6 and a<13:
        print("Your body fat percantage is {}.".format(a))
        print("Your category atlethe body according to American Council on Exercise (ACE).")
    elif a>14 and a<17:
        print("Your body fat percantage is {}.".format(a))
        print("Your category fitness body according to American Council on Exercise (ACE).")
    elif a>18 and a<24:
        print("Your body fat percantage is {}.".format(a))
        print("Your category is acceptable according to American Council on Exercise (ACE).")
    elif a>25:
        print("Your body fat percantage is {}.".format(a))
        print("Category is obesity according to American Council on Exercise (ACE).")

def fat_perc_male_cm(abdomen, neck, height):
    abdomen_inc = abdomen / 2.54
    neck_inc = neck / (2.54)
    height_inc = height/(2.54)
    perc = (86.010 *np.log10(abdomen_inc - neck_inc)) - (70.041 *np.log10(height_inc)) + 36.76
    a= round(perc,2)
    print(a)

def fat_perc_male_inc_exp(abdomen, neck, height):
    perc = (86.010 *np.log10(abdomen - neck)) - (70.041 *np.log10(height)) + 36.76
    a = round(perc,2)
    if a>2 and a<5:
        print("Your body fat percantage is {}.".format(a))
        print("Your category is essential fat according to American Council on Exercise (ACE).")
    elif a>6 and a<13:
        print("Your body fat percantage is {}.".format(a))
        print("Your category atlethe body according to American Council on Exercise (ACE).")
    elif a>14 and a<17:
        print("Your body fat percantage is {}.".format(a))
        print("Your category fitness body according to American Council on Exercise (ACE).")
    elif a>18 and a<24:
        print("Your body fat percantage is {}.".format(a))
        print("Your category is acceptable according to American Council on Exercise (ACE).")
    elif a>25:
        print("Your body fat percantage is {}.".format(a))
        print("Category is obesity according to American Council on Exercise (ACE).")



def fat_perc_male_inc(abdomen, neck, height):
    perc = (86.010 *np.log10(abdomen - neck)) - (70.041 *np.log10(height)) + 36.76
    a = round(perc,2)
    print(a)

def fat_perc_female_inc_exp(abdomen, hip, neck, height):
    perc = (163.205 *np.log10(abdomen + hip - neck)) - (97.684 *np.log10(height)) - 78.387
    a= round(perc,2)
    if a>10 and a<13:
        print("Your body fat percantage is {}.".format(a))
        print("Your category is essential fat according to American Council on Exercise (ACE).")
    elif a>14 and a<20:
        print("Your body fat percantage is {}.".format(a))
        print("Your category atlethe body according to American Council on Exercise (ACE).")
    elif a>21 and a<24:
        print("Your body fat percantage is {}.".format(a))
        print("Your category fitness body according to American Council on Exercise (ACE).")
    elif a>25 and a<31:
        print("Your body fat percantage is {}.".format(a))
        print("Your category is acceptable according to American Council on Exercise (ACE).")
    elif a>32:
        print("Your body fat percantage is {}.".format(a))
        print("Category is obesity according to American Council on Exercise (ACE).")

def fat_perc_female_cm_exp(abdomen, hip, neck, height):
    abdomen_inc = abdomen / 2.54
    hip_inc = hip / 2.54
    neck_inc = neck / (2.54)
    height_inc = height/(2.54)
    perc = (163.205 *np.log10(abdomen_inc + hip_inc - neck_inc)) - (97.684 *np.log10(height_inc)) - 78.387
    a = round(perc,2)
    if a>10 and a<13:
        print("Your body fat percantage is {}.".format(a))
        print("Your category is essential fat according to American Council on Exercise (ACE).")
    elif a>14 and a<20:
        print("Your body fat percantage is {}.".format(a))
        print("Your category atlethe body according to American Council on Exercise (ACE).")
    elif a>21 and a<24:
        print("Your body fat percantage is {}.".format(a))
        print("Your category fitness body according to American Council on Exercise (ACE).")
    elif a>25 and a<31:
        print("Your body fat percantage is {}.".format(a))
        print("Your category is acceptable according to American Council on Exercise (ACE).")
    elif a>32:
        print("Your body fat percantage is {}.".format(a))
        print("Category is obesity according to American Council on Exercise (ACE).")


def fat_perc_female_cm(abdomen, hip, neck, height):
    val=int(abdomen)
    val2=int(neck)
    val3=int(height)
    val4=int(hip)
    abdomen_inc = abdomen / 2.54
    hip_inc = hip / 2.54
    neck_inc = neck / (2.54)
    height_inc = height/(2.54)
    perc = (163.205 *np.log10(abdomen_inc + hip_inc - neck_inc)) - (97.684 *np.log10(height_inc)) - 78.387
    a = round(perc,2)
    print(a)



def bmr_male_cm_exp(weight, height,age):
    val=int(weight)
    val2=int(height)
    val3=int(age)
    cal =(88.362) + (13.397 * weight ) + (4.799 * height) - (5.677 * age)
    b = str(round(cal))
    print("Hi, welcome to the BMR Calculator!")
    print("Your BMR is {} kcal".format(b))

def bmr_male_cm(weight, height,age):
    try:
        val=int(weight)
        val2=int(height)
        val3=int(age)
        cal =(88.362) + (13.397 * weight ) + (4.799 * height) - (5.677 * age)
        b = str(round(cal))
        print(b)
    except:
        print("Please input an integer.")

def bmr_male_inc_exp(weight, height,age):
    try:
        val=int(weight)
        val2=int(height)
        val3=int(age)
        height = height * 2.54
        cal =(88.362) + (13.397 * weight ) + (4.799 * height) - (5.677 * age)
        b = str(round(cal))
        print("Hi, welcome to the BMR Calculator!")
        print("Your BMR is {} kcal".format(b))
    except:
        print("Please input an integer.")
def bmr_male_inc(weight, height,age):
    try:
        val=int(weight)
        val2=int(height)
        val3=int(age)
        height = height * 2.54
        cal =(88.362) + (13.397 * weight ) + (4.799 * height) - (5.677 * age)
        b = str(round(cal))
        print(b)
    except:
        print("Please input an integer.")

def bmr_woman_cm_exp(weight, height,age):
    try:
        val=int(weight)
        val2=int(height)
        val3=int(age)
        cal = (447.593) + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        b = round(cal)
        print("Hi, welcome BMR Calculator!")
        print("Your BMR is {} kcal".format(b))
    except:
        print("Please input an integer.")

def bmr_woman_cm(weight, height,age):
    try:
        val=int(weight)
        val2=int(height)
        val3=int(age)
        cal = (447.593) + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        b = round(cal)
        print(b)
    except:
        print("Please input an integer.")
def bmr_woman_inc_exp(weight, height,age):
    try:
        val=int(weight)
        val2=int(height)
        val3=int(age)
        height = height * 2.54
        cal = (447.593) + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        b = round(cal)
        print("Hi, welcome BMR Calculator!")
        print("Your BMR is {} kcal".format(b))
    except:
        print("Please input an integer.")
def bmr_woman_inc(weight, height,age):
    try:
        val=int(weight)
        val2=int(height)
        val3=int(age)
        height = height * 2.54
        cal = (447.593) + (9.247 * weight) + (3.098 * height) - (4.330 * age)
        b = round(cal)
        print(b)
    except:
        print("Please input an integer.")

def bmi_kg_exp(weight, height):
    try:
        val = int(height)
        val2 = int(weight)
        #Height should be in meter, weight should be in kg.
        height = height / 100
        b = weight / ((height)**2)
        if b < 18.4 :
            b = round(b,2)
            print("Welcome to Body Mass Index Calculator!")
            print("Your BMI is {} you are underweight.".format(b))
            b = (height ** 2) * 18.4
            b = round(b,2)
            d = (height ** 2) * 25
            d = round(d,2)
            e = b - weight
            e = round(e,2)
            print("Your ideal weight range is between {} kg and {} kg.".format(b,d))
            print("You have to gain {} kg to be fit.".format(e))
        elif b > 18.4 and b < 24.9:
            b = round(b,2)
            print("Your BMI is {} you are healty, keep going!".format(b))
        elif b> 25 and b < 29.9:
            b = round(b,2)
            print("Welcome to Body Mass Index Calculator!")
            print("Your BMI is {} you are overweight!".format(b))
            b = (height ** 2) * 18.4
            b = round(b,2)
            d = (height ** 2) * 25
            d = round(d,2)
            e = weight - d
            e = round(e,2)
            print("Your ideal weight range is between {} kg and {} kg.".format(b,d))
            print("You have to lost {} kg to be fit.".format(e))
        elif b > 30 and b < 34.9:
            b = round(b,2)
            print("Welcome to Body Mass Index Calculator!")
            print("Your BMI is {} you are obese!".format(b))
            b = (height ** 2) * 18.4
            b = round(b,2)
            d = (height ** 2) * 25
            d = round(d,2)
            e = weight - d
            e = round(e,2)
            print("Your ideal weight range is between {} kg and {} kg.".format(b,d))
            print("You have to lost {} kg to be fit.".format(e))
        elif b > 35 and b < 44.9:
            b = round(b,2)
            print("Welcome to Body Mass Index Calculator!")
            print("Your BMI is {} you are second phase in obesity!.".format(b))
            b = (height ** 2) * 18.4
            b = round(b,2)
            d = (height ** 2) * 25
            d = round(d,2)
            e = weight - d
            print("Your ideal weight range is between {} kg and {} kg.".format(b,d))
            print("You have to lost {} kg to be fit.".format(e))
        elif b > 45:
            b = round(b,2)
            print("Welcome to Body Mass Index Calculator!")
            print("Your BMI is {} you are third phase in obesity".format(b))
            b = (height ** 2) * 18.4
            b = round(b,2)
            d = (height ** 2) * 25
            d = round(d,2)
            e = weight - d
            print("Your ideal weight range is between {} kg and {} kg.".format(b,d))
            print("You have to lost {} kg to be fit.".format(e))
    except:
        print("Please input an integer.")

def bmi_kg(weight, height):
    try:
        val = int(height)
        val2 = int(weight)
        #Height should be in meter, weight should be in kg.
        height = height / 100
        b = weight / ((height)**2)
        print(b)
    except:
        print("Please input an integer.")
