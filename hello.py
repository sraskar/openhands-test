# ANSI color codes
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = '\033[0m'  # Reset to default color

# Print colorful "Hello, world!" message
print(f"{RED}H{GREEN}e{YELLOW}l{BLUE}l{MAGENTA}o{CYAN},{WHITE} {RED}w{GREEN}o{YELLOW}r{BLUE}l{MAGENTA}d{CYAN}!{RESET}")

# Alternative: Print with different color combinations
print(f"{CYAN}Hello, {MAGENTA}world!{RESET}")
print(f"{GREEN}Hello, {BLUE}world!{RESET}")
print(f"{YELLOW}Hello, {RED}world!{RESET}")
