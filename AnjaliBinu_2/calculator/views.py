from django.shortcuts import render
 
def bmi_calculator(request):
    bmi = None
    category = ""
    if request.method == "POST":
        try:
            weight = float(request.POST.get("weight"))
            height = float(request.POST.get("height"))
            # BMI formula: weight (kg) / (height (m))^2
            bmi = round(weight / (height ** 2), 2)
            # categorizing based on BMI value
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obesity"
        except (ValueError, TypeError):
            category = "Please enter valid numbers for weight and height"
    return render(request, "template/index.html", {"bmi": bmi, "category": category})