from decimal import Decimal, getcontext

# Set precision to handle up to 20 digits
getcontext().prec = 20


def calculate(a: str, operator: str, b: str) -> Decimal:
    """Perform basic arithmetic operations with Decimal numbers.

    Args:
        a: The first operand as a string.
        operator: A string representing the operator (+, -, *, /).
        b: The second operand as a string.

    Returns:
        Decimal: The result of the operation.
    """
    num1 = Decimal(a)
    num2 = Decimal(b)

    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2
    raise ValueError("Unsupported operator: %s" % operator)


def format_result(result: Decimal) -> str:
    """Format Decimal result to a string with up to 20 digits."""
    s = format(result, "f")
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return s


def main() -> None:
    print("Basic Calculator (supports up to 20-digit precision)")
    first = input("First number: ")
    op = input("Operator (+, -, *, /): ")
    second = input("Second number: ")

    try:
        result = calculate(first, op, second)
    except Exception as exc:  # broad catch to provide user-friendly output
        print(f"Error: {exc}")
        return

    print("Result:", format_result(result))


if __name__ == "__main__":
    main()
