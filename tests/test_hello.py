import unittest
import subprocess
import sys
import os

class TestColorfulHello(unittest.TestCase):

    def test_hello_script_runs_successfully(self):
        """Test that the hello.py script runs without errors"""
        result = subprocess.run([sys.executable, 'hello.py'],
                              cwd='/workspace',
                              capture_output=True,
                              text=True)
        self.assertEqual(result.returncode, 0, "Script should run without errors")

    def test_hello_script_produces_output(self):
        """Test that the hello.py script produces output"""
        result = subprocess.run([sys.executable, 'hello.py'],
                              cwd='/workspace',
                              capture_output=True,
                              text=True)
        self.assertGreater(len(result.stdout.strip()), 0, "Script should produce output")

    def test_hello_script_contains_hello_world(self):
        """Test that the output contains 'Hello, world!' text"""
        result = subprocess.run([sys.executable, 'hello.py'],
                              cwd='/workspace',
                              capture_output=True,
                              text=True)
        # Remove ANSI color codes to check for plain text
        import re
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        clean_output = ansi_escape.sub('', result.stdout)

        # Check that "Hello, world!" appears in the cleaned output
        output_lines = clean_output.strip().split('\n')
        hello_world_found = any('Hello, world!' in line for line in output_lines)
        self.assertTrue(hello_world_found, f"Output should contain 'Hello, world!'. Got: {output_lines}")

    def test_hello_script_contains_ansi_codes(self):
        """Test that the script contains ANSI color codes"""
        with open('/workspace/hello.py', 'r') as f:
            content = f.read()

        # Check for ANSI escape sequences
        self.assertIn('\\033[', content, "Script should contain ANSI color codes")
        self.assertIn('RED =', content, "Script should define RED color")
        self.assertIn('GREEN =', content, "Script should define GREEN color")
        self.assertIn('RESET =', content, "Script should define RESET color")

    def test_multiple_colored_outputs(self):
        """Test that the script produces multiple lines of output"""
        result = subprocess.run([sys.executable, 'hello.py'],
                              cwd='/workspace',
                              capture_output=True,
                              text=True)
        output_lines = result.stdout.strip().split('\n')
        self.assertGreaterEqual(len(output_lines), 4, "Script should produce at least 4 lines of output")

if __name__ == '__main__':
    unittest.main()
