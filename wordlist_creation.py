import pathlib, sys
from string import ascii_letters

in_path = pathlib.Path(sys.argv[1])
out_path = pathlib.Path(sys.argv[2])

words = sorted(
    {
    word.lower()
    for word in in_path.read_text(encoding="utf-8").split()
    if len(word) == 5 and all(letter in ascii_letters for letter in word)
    }, 
    key=lambda word: (len(word), word),  
)
out_path.write_text("\n".join(words))