## find
find . -name "secret.txt"           # exact name
find . -iname "*secret*"            # ignore case, partial name
find . -type f                      # files only
find . -type d                      # dirs only
find / -name "x.txt" 2>/dev/null    # whole system, hide errors

find . -type f -exec grep -l "picoCTF" {} \;   # find + grep combo
