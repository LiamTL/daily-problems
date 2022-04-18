def bmi(weight, height):
    if weight * height * height <= 18.5:
        return "Underweight"
    elif weight * height * height <= 25.0:
        return "Normal"
    elif weight * height * height <= 30.0:
        return "Overweight"
    return "Obese"