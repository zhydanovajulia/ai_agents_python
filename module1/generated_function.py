def factorial(n):
    """
    Calculates the factorial of a non-negative integer n.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the number n.

    Raises:
    ValueError: If n is a negative integer.

    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def test_factorial():
    """
    Tests the factorial function with different test cases and edge cases
    to ensure correctness.

    Raises:
    AssertionError: If any test case fails.

    """
    # Test cases for the factorial function
    assert factorial(0) == 1, "Test case 0! failed"
    assert factorial(1) == 1, "Test case 1! failed"
    assert factorial(2) == 2, "Test case 2! failed"
    assert factorial(3) == 6, "Test case 3! failed"
    assert factorial(4) == 24, "Test case 4! failed"
    assert factorial(5) == 120, "Test case 5! failed"

    # Handling large number cases
    assert factorial(10) == 3628800, "Test case 10! failed"
    
    # Handling negative inputs
    try:
        factorial(-1)
    except ValueError as e:
        assert str(e) == "Factorial is not defined for negative numbers"

if __name__ == "__main__":
    test_factorial()
    print("All tests passed.")
