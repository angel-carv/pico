# picoCTF – vault-door-training

**Category:** Reverse Engineering
**File:** `VaultDoorTraining.java`
**Flag:** `academy{w4rm1ng_Up_w1tH_jAv4_69bd4dc7adf}`

## Core idea
The password is **hardcoded in the source code**. Read `checkPassword()`, then wrap the string in the flag format the program expects.

```java
String input = userInput.substring("academy{".length(), userInput.length()-1);
...
return password.equals("w4rm1ng_Up_w1tH_jAv4_69bd4dc7adf");
```
- `main` cuts off the first 8 characters (`academy{`) and the last character (`}`), then compares what's left.
- So the input has to be `academy{` + password + `}`.

## How the tools work

### `javac` vs `java`
| Command | What it does |
|---|---|
| `javac File.java` | **Compiles** source code into bytecode, creating `File.class`. Prints nothing if it succeeds |
| `java ClassName` | **Runs** a compiled class. Use the class name only, with **no extension** |
| `java File.java` | Compiles and runs a single file in one step (Java 11+) |

Mistakes I made:
- `./File.java` → `permission denied`: a `.java` file is source code, not an executable
- `javac File.class` → `invalid flag`: javac only accepts `.java` files
- `java VaultDoorTraining.class` or `java VaultDoorTraining.` → `ClassNotFoundException`: Java treats everything you type as part of the class name, so the extension or a stray `.` breaks it

### `substring(begin, end)`
- Returns the characters from index `begin` up to, **but not including**, `end`
- If `begin > end` or the indexes are out of range, it throws `StringIndexOutOfBoundsException`
- Entering `passwerd` (8 chars) produced `substring(8, 7)` and crashed, because the program never checks the input length first

Why entering just the password gave **Access denied**: the program still cut off 8 characters from the front and 1 from the end, so what it compared was no longer the password.

### `.class` files leak strings
`cat VaultDoorTraining.class` showed the password in readable text. Compiled bytecode keeps string literals in its **constant pool** as plain text, so you don't need the source code:
```sh
strings VaultDoorTraining.class     # cleaner than cat: prints only readable text
javap -c -p VaultDoorTraining.class # disassemble the bytecode (comes with the JDK)
```
For a full decompile back to Java source, you can use tools like **CFR**, **JD-GUI** or **jadx**.

## Takeaways
- Hardcoded secrets in source code **or** compiled binaries can be recovered. Try `strings` first.
- Read how the program **processes input** before the check runs. The format matters, not just the secret.
- This CTF's flag format is `academy{...}`.

## Setup
```sh
brew install --cask temurin   # Java (OpenJDK); macOS finds it automatically
java -version
```
