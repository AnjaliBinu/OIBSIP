def run_bmi_calculator():
    print("=== BMI Calculator ===")

    # 1. User Input and Validation
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))
    except ValueError:
        print("Error: Please enter valid numbers.")
        return

    # 2. Input Validation for Positive Values
    if weight <= 0 or height <= 0:
        print("Error: Values must be greater than zero.")
        return

    # 3. Smart Auto-Conversion (Handles cm to meters if needed)
    if height > 3:
        height = height / 100

    # 4. BMI Calculation
    bmi = round(weight / (height ** 2), 2)

    # 5. Categorization Logic
    if bmi < 18.5:
        status = "Underweight"
    elif 18.5 <= bmi < 24.9:
        status = "Normal weight"
    elif 24.9 <= bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obese"

    # 6. Displaying the Results
    print(f"\nYour BMI is: {bmi}")
    print(f"Category: {status}")

if __name__ == "__main__":
    run_bmi_calculator()