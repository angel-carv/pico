# picoCTF – Enhance!

**Category:** Forensics
**File:** `drawing.flag.svg`
**Flag:** `academy{3nh4nc3d_9f31c04b}`

## Summary
The flag is hidden as text inside an SVG image. The text is too small to see when the image is rendered normally, and it is split into many small `<tspan>` elements.

## Steps

### 1. Check the metadata
```sh
exiftool drawing.flag.svg
```
- File type: **SVG**, an XML-based vector image (plain text, not pixels)
- Created in **Inkscape 0.92.5**, A4 page (210×297mm)
- Metadata is all Inkscape defaults → **no clue here**, so look inside the file

### 2. Open it in a vector editor and zoom in
```sh
brew install --cask inkscape
open -a Inkscape drawing.flag.svg   # -a = open with a specific app
```
- Vectors stay sharp at any zoom level, so tiny hidden text becomes readable
- Useful Inkscape tools:
  - **Edit → Select All in All Layers** (⌘⌥A): highlights invisible or tiny objects
  - **Edit → XML Editor** (⌘⇧X): browse the raw elements (`svg:text` / `svg:tspan`)
  - **Object → Layers and Objects** (⌘⇧L): list every object

### 3. Extract the text
The text came out one character per piece:
```
a c a d e m y { 3 n h 4 n c 3 d _ 9 f 3 1 c 0 4 b }
```
Remove the spaces and newlines to get the flag.

### Faster alternative (no GUI)
SVG is plain text, so the text can be pulled out directly:
```sh
grep -o '>[^<]*</tspan>' drawing.flag.svg | sed 's/<[^>]*>//g; s/>//' | tr -d ' \n'; echo
```

## Takeaways
- **SVG = text.** Always try `cat`, `strings` or `grep` on it before reaching for image tools.
- Watch for **tiny font sizes**, white-on-white text, objects outside the `viewBox`, and text split across many `<tspan>`s.
- When metadata turns up nothing, it's just a red herring. Move on to the file's contents.
- The challenge name ("Enhance") hints at the method: zoom in.

## Tools used
`exiftool`, `inkscape`, `open -a`, `tldr`
