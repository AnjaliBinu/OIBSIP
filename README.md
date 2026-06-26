# 🌟 Python Mini Projects Collection

A collection of beginner-friendly Python projects designed to strengthen programming fundamentals through practical applications. These projects focus on user input handling, validation, API integration, randomization, and mathematical calculations.

---

# 📌 Projects Included

1. BMI Calculator
2. Random Password Generator
3. Basic Weather App

---

# 1. BMI Calculator

## 📖 Description

The BMI (Body Mass Index) Calculator is a command-line application that calculates a user's BMI using their weight and height. Based on the calculated BMI, the program classifies the user into standard health categories such as Underweight, Normal Weight, Overweight, or Obese.

This project introduces beginners to mathematical calculations, conditional statements, and user input validation.

---

## ✨ Features

- Accepts weight in kilograms
- Accepts height in meters
- Calculates BMI using the standard formula
- Displays BMI up to two decimal places
- Categorizes BMI into health ranges
- Handles invalid or unrealistic user inputs gracefully

---

## 🧮 BMI Formula

BMI = Weight (kg) / Height² (m²)

---

## 📊 BMI Categories

| BMI Range | Category |
|-----------|----------|
| Less than 18.5 | Underweight |
| 18.5 – 24.9 | Normal Weight |
| 25.0 – 29.9 | Overweight |
| 30.0 and above | Obese |

---

## 💡 Concepts Used

- Variables
- Input and Output
- Arithmetic Operations
- Conditional Statements
- Exception Handling
- Input Validation

---

# 2. Random Password Generator

## 📖 Description

The Random Password Generator is a command-line application that creates strong and customizable passwords based on user preferences. Users can specify the password length and choose whether to include letters, numbers, and special characters.

This project helps beginners understand randomization, string manipulation, and user-driven program customization.

---

## ✨ Features

- Generate passwords of custom length
- Include uppercase and lowercase letters
- Include numbers
- Include special characters
- Randomly generate secure passwords
- Validate user inputs

---

## ⚙️ User Options

Users can choose:

- Password length
- Include alphabets
- Include numbers
- Include symbols

Example:

```
Password Length: 12

Include Letters? Yes
Include Numbers? Yes
Include Symbols? Yes
```

Generated Password:

```
Q8@kLm!2r#Px
```

---

## 💡 Concepts Used

- Random Module
- String Module
- Loops
- Lists
- Conditional Statements
- Input Validation
- String Manipulation

---

# 3. Basic Weather App

## 📖 Description

The Basic Weather App is a command-line application that fetches real-time weather information using a Weather API. Users enter a city name (or ZIP code), and the application displays current weather details such as temperature, humidity, and weather conditions.

This project introduces beginners to working with APIs and JSON data.

---

## ✨ Features

- Search weather by city
- Fetch live weather data
- Display:
  - Temperature
  - Humidity
  - Weather Condition
- Handle invalid city names
- Display API error messages gracefully

---

## 🌍 Example Output

```
City: Kochi

Temperature: 30°C

Humidity: 82%

Condition: Clouds
```

---

## 💡 Concepts Used

- API Integration
- HTTP Requests
- JSON Parsing
- Dictionaries
- User Input Validation
- Exception Handling

---

# 🛠 Technologies Used

- Python 3.14
- Command Line Interface (CLI)

Libraries Used:

- random
- string
- requests
- json

---

# 📂 Project Structure

```
Python-Mini-Projects/
│
├── BMI_Calculator/
│   ├── bmi_calculator.py
│   └── README.md
│
├── Password_Generator/
│   ├── password_generator.py
│   └── README.md
│
├── Weather_App/
│   ├── weather_app.py
│   ├── config.py
│   └── README.md
│
└── README.md
```

---

# 🚀 Getting Started

## Clone the Repository

```bash
git clone https://github.com/your-username/python-mini-projects.git
```

Navigate into the project directory:

```bash
cd python-mini-projects
```

Run any project using:

```bash
python filename.py
```

---

# 📚 Learning Outcomes

These projects help beginners gain hands-on experience with:

- Python fundamentals
- User input and validation
- Functions
- Conditional logic
- Loops
- Random number generation
- API consumption
- JSON data handling
- Error handling
- Writing clean and modular code

---

# 🎯 Future Improvements

### BMI Calculator

- GUI version using Tkinter
- Store BMI history
- Metric and Imperial unit support

### Password Generator

- Password strength checker
- Copy password to clipboard
- Save generated passwords securely

### Weather App

- 5-day weather forecast
- Display wind speed and pressure
- Search by GPS coordinates
- Weather icons
- GUI version

---

# 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

If you have ideas for new beginner-friendly Python projects or enhancements to existing ones, feel free to fork the repository and submit a pull request.

---

# ⭐ Support

If you found these projects helpful, consider giving the repository a ⭐ on GitHub. It helps others discover the project and motivates future improvements.

Happy Coding! 🚀
