## grep
grep "text" file          # lines containing text
grep -i "text" file       # ignore case
grep -o "pattern" file    # print only the match
grep -r "text" dir/       # search directory recursively
grep -a "text" file       # search binary as text
grep -c "text" file       # count matches

grep -o "picoCTF{[^}]*}" file   # pull a flag
[] to show like a shopping list of stuff
^} to say NOT }, just find anything not including }
* to say keep going until you find }
