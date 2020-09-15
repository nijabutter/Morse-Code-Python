# Python Morse Code Translator

Usage
***
## Encoding
`python morsecode.py "hello world"`
> .... . .-.. .-.. --- / .-- --- .-. .-.. -..

## Decoding
`python morsecode.py -d ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."`
> HELLO WORLD

## Using Files
It will open the file and attempt to translate any text it can.
New lines will be added.

**Decoding from files is buggy.**

`python morsecode.py encode_me.txt`
```
- . -..- -
--- -. / .- / -. . .-- / .-.. .. -. .
```

Params
***

`-i` will replace all unrecognised characters with the following character
Ommitting this will default to `?`

`python morsecode.py -i# "h@llo"`
> .... # .-.. .-.. ---

Adding no following character will remove them entirely

`python morsecode.py -i "h@llo`
> ....  .-.. .-.. ---
