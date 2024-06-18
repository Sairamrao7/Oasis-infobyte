def calculate_BMI(Weight, Height):
    return Weight / (Height ** 2)

def classify_BMI(BMI):
    if BMI < 18.5:
        return "Underweight"
    elif 18.5 <= BMI < 25:
        return "Normal weight"
    elif 25 <= BMI < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    Weight = float(input("Enter your weight in kilograms: "))
    Height = float(input("Enter your height in meters: "))

    BMI = calculate_BMI(Weight, Height)
    category = classify_BMI(BMI)

    print(f"Your BMI is: {BMI:.2f}")
    print(f"You are classified as: {category}")

if __name__ == "__main__":
    main()
