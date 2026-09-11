import subprocess

with open("dictionary.txt", "r") as passwords:
    for pw in passwords:
        result = subprocess.run(["python3", "level5.py"], input=pw, capture_output=True, text=True)
        print(pw, "->", result.stdout.strip())
