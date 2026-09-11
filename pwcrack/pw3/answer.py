import subprocess

pwlist = ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]

for pw in pwlist:
    result = subprocess.run(
        ["python3", "level3.py"],
        input=pw,
        capture_output=True,
        text=True
    )
    print(pw, "->", result.stdout.strip())	
