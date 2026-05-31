# Healthcare Patient Risk Predictor

name = input("Enter patient name: ")
age = int(input("Enter age: "))
blood_pressure = int(input("Enter blood pressure: "))
blood_sugar = int(input("Enter blood sugar level: "))

risk_score = 0

if age > 60:
    risk_score += 1

if blood_pressure > 140:
    risk_score += 1

if blood_sugar > 180:
    risk_score += 1

print("\nPatient Name:", name)

if risk_score == 0:
    print("Risk Level: Low")
elif risk_score == 1:
    print("Risk Level: Moderate")
elif risk_score == 2:
    print("Risk Level: High")
else:
    print("Risk Level: Critical")
