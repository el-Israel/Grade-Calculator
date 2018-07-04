#BMI CALCULATOR BY CALLING A FUNCTION
name1= "Emmanuella"
height_m1 = float (1.52)
weight_kg1 = float (86.9)

name2 = "julius"
height_m2 = float(1.75)
weight_kg2 = float (75)

name3 = "jumoke"
height_m3 = float (2.5) 
weight_kg3 = float (142.2)

def bmi_calculator (name, height_m, weight_kg):
    bmi = weight_kg / (height_m **2)
    print ("bmi: ")
    print (bmi)
    if bmi > 25 :
        return name + " is over weight"
    else:
        return name + " is not over weight"

result1= bmi_calculator (name1, height_m1, weight_kg1)
result2= bmi_calculator (name2, height_m2, weight_kg2)
result3= bmi_calculator (name3, height_m3, weight_kg3)

print (result1)
print (result2)
print (result3)
