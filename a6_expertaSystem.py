def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return weight / (height_m ** 2)

def main():
    print("Medical Expert System")
    print("Focus Area: Diabetes, Hypertension, BMI, General Risk")


    # Collect basic inputs
    age = int(input("Enter your age: ").strip())
    weight = float(input("Enter your weight (in kg): ").strip())
    height_cm = float(input("Enter your height (in cm): ").strip())

    fasting_sugar = float(input("Enter fasting blood sugar (mg/dL): ").strip())
    post_meal_sugar = float(input("Enter post-meal blood sugar (mg/dL): ").strip())

    systolic_bp = int(input("Enter systolic BP: ").strip())
    diastolic_bp = int(input("Enter diastolic BP: ").strip())

    # Symptom checks
    history_diabetes = input("Do you have diabetes? (yes/no): ").strip().lower()
    frequent_thirst = input("Do you often feel thirsty? (yes/no): ").strip().lower()
    frequent_urination = input("Do you urinate frequently? (yes/no): ").strip().lower()
    blurred_vision = input("Do you have blurred vision? (yes/no): ").strip().lower()
    fatigue = input("Do you feel tired often? (yes/no): ").strip().lower()
    chest_pain = input("Do you experience chest pain? (yes/no): ").strip().lower()
    headache = input("Do you experience frequent headaches? (yes/no): ").strip().lower()

    print("\n--- Diagnosis Report ---")

    # Risk flags
    diabetes_risk = False
    hypertension_risk = False
    mild_warning = False
    bmi_warning = False

    # BMI calculation
    bmi = calculate_bmi(weight, height_cm)
    print(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("BMI Status: Underweight")
        bmi_warning = True
        print("Suggestion: Gain weight through healthy diet. Consult nutritionist.\n")
    elif 18.5 <= bmi <= 24.9:
        print("BMI Status: Normal\n")
    elif 25 <= bmi < 30:
        print("BMI Status: Overweight")
        bmi_warning = True
        print("Suggestion: Watch diet and exercise to avoid future complications.\n")
    else:
        print("BMI Status: Obese")
        bmi_warning = True
        print("Suggestion: High risk for diabetes, heart disease. Consult dietician.\n")

    # Diabetes Evaluation
    if fasting_sugar >= 126 and post_meal_sugar >= 200:
        diabetes_risk = True
        print("Diagnosis: Likely diabetic")
        if history_diabetes == "yes":
            print("Note: Diabetes history + high sugar = critical risk.")
        else:
            print("Warning: Diabetic range sugar without known history.")
        print("Suggestion: Immediate consultation with diabetologist.\n")
    elif 100 <= fasting_sugar < 126 or 140 <= post_meal_sugar < 200:
        diabetes_risk = True
        print("Diagnosis: Pre-diabetic stage.")
        print("Suggestion: Lifestyle control. Reverse is possible.\n")
    elif (frequent_thirst == 'yes' or frequent_urination == 'yes' or  blurred_vision == 'yes' or fatigue == 'yes') and (fasting_sugar > 110 or post_meal_sugar > 160):
        diabetes_risk = True
        print("Diagnosis: Early diabetes symptoms detected.")
        print("Suggestion: Take HbA1c test. Meet physician.\n")
    else:
        print("Blood sugar levels are within safe range.\n")

    # Hypertension Evaluation
    if systolic_bp >= 140 or diastolic_bp >= 90:
        hypertension_risk = True
        print("Diagnosis: High blood pressure detected.")
        if chest_pain == "yes":
            print("Chest pain + high BP = emergency warning.")
        if headache == 'yes':
            print("Frequent headaches may indicate stress or hypertension.")
        print("Suggestion: Reduce salt, monitor BP, consult cardiologist.\n")
    elif 120 <= systolic_bp < 140 or 80 <= diastolic_bp < 90:
        hypertension_risk = True
        print("Diagnosis: Pre-hypertension.")
        print("Suggestion: Lifestyle change needed to avoid progression.\n")
    else:
        print("Blood pressure is normal.\n")

    # Mild Warnings & General Suggestions
    if not diabetes_risk and not hypertension_risk:
        if(frequent_thirst == "yes" or frequent_urination == "yes" or fatigue == "yes"):
            mild_warning = True
            print("Warning: Symptoms noted but levels are normal.")
            print("Suggestion: Repeat tests in 2 weeks. Monitor symptoms.\n")
        if(chest_pain == "yes" or headache == "yes"):
            mild_warning = True
            print("Mild Concern: Chest pain/headache without high BP.")
            print("Suggestion: Possible stress. Consider ECG and check-up.\n")

    if not diabetes_risk and not hypertension_risk and not mild_warning and not bmi_warning:
        print("You are in good health based on provided data.")
        if age > 45:
            print("Note: Regular checkups advised due to age.\n")
        else:
            print("Keep exercising and eating healthy!\n")

if __name__ == "__main__":
    main()