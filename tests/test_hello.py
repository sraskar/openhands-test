import unittest
import sys
import os
from io import StringIO
from unittest.mock import patch

# Add the parent directory to the path so we can import hello
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import hello

class TestExcitingHello(unittest.TestCase):

    def test_print_exciting_hello_runs_without_error(self):
        """Test that the exciting hello function runs without throwing any exceptions"""
        try:
            # Capture stdout to avoid cluttering test output
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                # Mock time.sleep to make tests run faster
                with patch('time.sleep'):
                    hello.print_exciting_hello()

            # Get the captured output
            output = mock_stdout.getvalue()

            # Verify that some expected content is in the output
            self.assertIn("HELLO, AMAZING WORLD!", output)
            self.assertIn("🎉", output)
            self.assertIn("Have an INCREDIBLE day ahead!", output)

        except Exception as e:
            self.fail(f"print_exciting_hello() raised an exception: {e}")

    def test_exciting_messages_are_present(self):
        """Test that exciting messages are defined and accessible"""
        # We'll test this by running the function multiple times and checking
        # that we get different messages (due to randomness)
        messages_seen = set()

        for _ in range(10):  # Run multiple times to catch different random messages
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                with patch('time.sleep'):
                    hello.print_exciting_hello()

                output = mock_stdout.getvalue()

                # Check for any of the exciting messages
                exciting_phrases = [
                    "You're absolutely fantastic!",
                    "Ready to conquer the day!",
                    "Magic is happening right now!",
                    "You're on fire today!",
                    "Spreading joy and colors!",
                    "Dreams are coming true!"
                ]

                for phrase in exciting_phrases:
                    if phrase in output:
                        messages_seen.add(phrase)

        # We should have seen at least one exciting message
        self.assertGreater(len(messages_seen), 0, "No exciting messages found in output")

    def test_emojis_are_present(self):
        """Test that emojis are included in the output"""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('time.sleep'):
                hello.print_exciting_hello()

        output = mock_stdout.getvalue()

        # Check for presence of various emojis
        expected_emojis = ['🎉', '🚀', '⭐', '🌟', '✨', '🎊', '🔥', '💫', '🎈', '🌈']
        emoji_found = False

        for emoji in expected_emojis:
            if emoji in output:
                emoji_found = True
                break

        self.assertTrue(emoji_found, "No emojis found in the output")

    def test_colors_dictionary_exists(self):
        """Test that the colors dictionary is properly defined"""
        self.assertTrue(hasattr(hello, 'colors'))
        self.assertIsInstance(hello.colors, dict)

        # Check for essential color codes
        essential_colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'bold', 'end']
        for color in essential_colors:
            self.assertIn(color, hello.colors, f"Color '{color}' not found in colors dictionary")

    def test_emojis_list_exists(self):
        """Test that the emojis list is properly defined"""
        self.assertTrue(hasattr(hello, 'emojis'))
        self.assertIsInstance(hello.emojis, list)
        self.assertGreater(len(hello.emojis), 0, "Emojis list should not be empty")

if __name__ == '__main__':
    unittest.main()
