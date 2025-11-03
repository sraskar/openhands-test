#!/usr/bin/env python3
"""
Test file for hello.py functions
"""
import sys
from io import StringIO
import hello


def test_hello_openhands():
    """Test that hello_openhands prints the correct message"""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the function
    hello.hello_openhands()

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Check the output
    output = captured_output.getvalue().strip()
    expected = "Hello from OpenHands!"
    assert output == expected, f"Expected '{expected}', but got '{output}'"
    print(f"✓ hello_openhands() test passed: '{output}'")


def test_hello_bedrock():
    """Test that hello_bedrock prints the correct message"""
    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    # Call the function
    hello.hello_bedrock()

    # Reset stdout
    sys.stdout = sys.__stdout__

    # Check the output
    output = captured_output.getvalue().strip()
    expected = "Hello from Bedrock!"
    assert output == expected, f"Expected '{expected}', but got '{output}'"
    print(f"✓ hello_bedrock() test passed: '{output}'")


if __name__ == "__main__":
    print("Running tests for hello.py functions...")
    test_hello_openhands()
    test_hello_bedrock()
    print("All tests passed!")
