from django.shortcuts import render

def bmi_calculator(request):
    bmi = None
    status = ""
    
    if request.method == "POST":
        weight = float(request.POST.get('weight', 0))
        height = float(request.POST.get('height', 0))
        
        if weight > 0 and height > 0:
            if height > 3:
                height = height / 100
                
            bmi = round(weight / (height ** 2), 2)
            
            if bmi < 18.5:
                status = "Underweight"
            elif 18.5 <= bmi < 24.9:
                status = "Normal weight"
            elif 25 <= bmi < 29.9:
                status = "Overweight"
            else:
                status = "Obese"
                
    return render(request, 'calculator/index.html', {'bmi': bmi, 'status': status})