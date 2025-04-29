def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return f"Your BMI is {bmi:.2f}. You are underweight."
    elif 18.5 <= bmi < 24.9:
        return f"Your BMI is {bmi:.2f}. You have a normal weight."
    elif 25 <= bmi < 29.9:
        return f"Your BMI is {bmi:.2f}. You are overweight."
    else:
        return f"Your BMI is {bmi:.2f}. You are obese."

def bmi_calculator():
    print("Welcome to the BMI Calculator!")
    
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in meters): "))
    
    result = calculate_bmi(weight, height)
    print(result)

if __name__ == "__main__":
    bmi_calculator()
