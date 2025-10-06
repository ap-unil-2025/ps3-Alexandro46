def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    Formula: F = (C × 9/5) + 32
    """
    return round((celsius * 9 / 5) + 32, 2)


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    Formula: C = (F - 32) × 5/9
    """
    return round((fahrenheit - 32) * 5 / 9, 2)


def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    try:
        value = float(input("Enter temperature value: "))
        unit = input("Enter current unit (C/F): ").strip().lower()

        if unit == "c":
            result = celsius_to_fahrenheit(value)
            print(f"{value}°C = {result}°F")
        elif unit == "f":
            result = fahrenheit_to_celsius(value)
            print(f"{value}°F = {result}°C")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid input. Please enter a numeric temperature.")


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    print("All tests passed!")

    # Run interactive converter
    temperature_converter()