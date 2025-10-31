import random
import time

# ANSI color codes for exciting output
colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'blue': '\033[94m',
    'magenta': '\033[95m',
    'cyan': '\033[96m',
    'white': '\033[97m',
    'bold': '\033[1m',
    'end': '\033[0m'
}

# Exciting emojis
emojis = ['🎉', '🚀', '⭐', '🌟', '✨', '🎊', '🔥', '💫', '🎈', '🌈']

def print_exciting_hello():
    # Clear screen effect
    print("\n" * 3)

    # Animated countdown
    print(f"{colors['bold']}{colors['yellow']}🚀 LAUNCHING EXCITEMENT IN... {colors['end']}")
    for i in range(3, 0, -1):
        print(f"{colors['bold']}{colors['red']}{i}...{colors['end']}")
        time.sleep(0.5)

    # Big exciting hello
    print(f"\n{colors['bold']}{colors['magenta']}{'='*50}{colors['end']}")
    print(f"{colors['bold']}{colors['cyan']}🎉 HELLO, AMAZING WORLD! 🎉{colors['end']}")
    print(f"{colors['bold']}{colors['magenta']}{'='*50}{colors['end']}")

    # Random exciting messages
    exciting_messages = [
        "🌟 You're absolutely fantastic! 🌟",
        "🚀 Ready to conquer the day! 🚀",
        "✨ Magic is happening right now! ✨",
        "🔥 You're on fire today! 🔥",
        "🌈 Spreading joy and colors! 🌈",
        "💫 Dreams are coming true! 💫"
    ]

    selected_message = random.choice(exciting_messages)
    print(f"\n{colors['bold']}{colors['green']}{selected_message}{colors['end']}")

    # Animated emoji celebration
    print(f"\n{colors['yellow']}Celebration time: {colors['end']}", end="")
    for _ in range(10):
        emoji = random.choice(emojis)
        print(f"{emoji}", end=" ")
        time.sleep(0.1)

    print(f"\n\n{colors['bold']}{colors['blue']}Have an INCREDIBLE day ahead! 🎊{colors['end']}")
    print(f"{colors['cyan']}{'~' * 40}{colors['end']}\n")

if __name__ == "__main__":
    print_exciting_hello()
