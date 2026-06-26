# 🌤️ Command-Line Weather App

A lightweight, beginner-friendly Python console application that connects to the live OpenWeatherMap API to retrieve and display current real-time weather details for any user-specified city or ZIP code.

## 🚀 Features

- **Live API Integration:** Fetches real-world data dynamically using the Python `requests` library.
- **Fail-Safe Parsing:** Safely processes nested JSON data structures using dictionaries.
- **Robust Error Handling:** Detects network errors or misspelled locations without crashing.
- **Secure Key Management:** Uses environment variables (`.env`) to keep private API keys protected.

## 📋 Prerequisites & Installation

Before running the application, make sure you have Python installed, then install the required dependencies:

```bash
pip install requests python-dotenv