import sys
import time
import random

def colorful_animation(text):
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    
    for char in text:
        sys.stdout.write(random.choice(colors) + char)
        sys.stdout.flush()
        time.sleep(0.1)
    print('\033[0m') 

if __name__ == "__main__":
    message = "Happy Friendship Day!"
    colorful_animation(message)
