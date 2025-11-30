import time

def twpw(text, delay=0.075):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()