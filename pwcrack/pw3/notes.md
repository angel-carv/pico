how I solved. 

I looked at the python file and saw all the possible answers at the end

I wanted to learn how to script but I couldn't do it with my current knowledge
so I asked claude

PicoCTF pw3 — notes

Setup: level3.py reads a password, MD5-hashes it, compares to level3.hash.bin. If it matches, it XORs level3.flag.txt.enc with the password to reveal the flag. 7 candidate passwords are listed at the bottom of the script (pos_pw_list), only 1 is correct.

Method 1 — reimplement the check:
import hashlib
correct_hash = open('level3.hash.bin', 'rb').read()
for pw in pwlist:
    if hashlib.md5(pw.encode()).digest() == correct_hash:
        print("Found it:", pw)
Hash each candidate the same way the script does, compare to the stored hash directly.

Method 2 — automate the actual program:
import subprocess
for pw in pwlist:
    result = subprocess.run(["python3", "level3.py"], input=pw, capture_output=True, text=True)
    print(pw, "->", result.stdout.strip())
Runs level3.py for real, 7 times, feeding each candidate as if typed at the prompt, and captures the output.

Answer found: 87ab → matches hash → flag: picoCTF{m45h_fl1ng1ng_cd6ed2eb}

Takeaway: two valid strategies for "try N candidates against a check" — reimplement the logic in a loop (faster, no subprocess), or automate the real program via subprocess (useful when you can't/don't want to reimplement the logic yourself).
