def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.
    """
    numbers = []
    while True:
        user_input = input("Enter a number: ").strip().lower()
        if user_input == "done":
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers
    """
    if not numbers:
        return None

    analysis = {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": round(sum(numbers) / len(numbers), 2),
        "minimum": min(numbers),
        "maximum": max(numbers),
        "even_count": sum(1 for n in numbers if n % 2 == 0),
        "odd_count": sum(1 for n in numbers if n % 2 != 0),
    }
    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.
    """
    print("\nAnalysis Results:")
    print("-----------------")
    print(f"Count: {analysis['count']}")
    print(f"Sum: {analysis['sum']}")
    print(f"Average: {analysis['average']:.2f}")
    print(f"Minimum: {analysis['minimum']}")
    print(f"Maximum: {analysis['maximum']}")
    print(f"Even numbers: {analysis['even_count']}")
    print(f"Odd numbers: {analysis['odd_count']}")


def main():
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")

    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    analysis = analyze_numbers(numbers)
    display_analysis(analysis)


if __name__ == "__main__":
    main()
