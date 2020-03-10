# QR Puzzle
A 314 point reversing challenge from <a href="https://https://www.zer0pts.com/">zer0pts CTF 2020</a>

`"This puzzle is a puzzling puzzle."`

The download for this challenge had 3 files, encrypted.qr, key, and chall.

encrypted.qr is a text file that only contains 1s and 0s in a 25x25 grid, and given the name of the challenge and of the file I think assuming this is a QR code is a safe bet, Unfortunately, if we try translating the binary to black and white squares doesn't make a valid code. <b>Big guess here</b>, but it's probably encrypted and has something to do with the key file we've been given.
```
1111111100000100110011111
1010000011100011100101010
1010010111010110011010100
0011101001100100010111111
1011101001111011110101111
...
```

The key file contains 625 lines, each starting with a number between 0 and 3, followed by the coordinate pair. Understanding what these numbers mean and how they are applied to the puzzle is the key to solving this problem.
```
1#(13,7)
3#(19,21)
2#(6,1)
0#(6,12)
1#(0,7)
1#(12,21)
...
```

If we try and run chall we get the following help message telling us how to use the software.
```
> ./chall
Usage: ./chall [qr] [key] [output]
```

When we fulfill the file requirements that it asks for we can see some stuff happening and when it finishes we have a new file. out.txt how exists and contains another 25x25 QR code.
```
> ./chall encrypted.qr key, out.txt
[+] Loading QR...
[+] Done!
[+] Loading key...
[+] Done!
[+] Encrypting...
[+] Done!
[+] Saving encrypted QR...
[+] Done!
```

So now that we've taken a look at all the files, we can outline what we need to do to get the flag.
chall takes in a qr code, encrypts it with a key, and then write the encrypted code to the specified output file.
Given that we have a key and garbage QR code suspiciously name *encrypted*.qr we probably want to decrypt it to get the flag. 

BUT WAIT! chall doesn't have a decrypt option! 

Well then, I guess we'll have to reverse engineer the encryption function to build our own decryption function.

Cracking chall open in Ghidra I was able to locate the main function and do a little function renaming based on the text being printed.

<img src=main.png>

Poking around in load_puzzle and load_key can help us understand the format of the two input files and how they are represented in memory, but I'm going to skip ahead to the fun stuff in encrypt_puzzle. This function took a while to get my head around and I was reguarly switching back and forth between the disassembly and decompiled views to make sure I truly understanding it.

<img src=encrypt_decomp.png>

At the end of the day the encryption is actually fairly simple, each coordinate pair in the key selects a cell in the QR code and the other number specifies whether to add or subtract that cell with one of the others surrounding it. I've recreated the encryption in the python function below.
```python
def encrypt(key, qr):
    for line in key:
        mode = int(line[0])
        x = int(line[3:line.find(',')])
        y = int(line[line.find(',')+1:-2])
        
        if mode == 0:
            x2 = x-1
            y2 = y
        elif mode == 1:
            x2 = x+1
            y2 = y
        elif mode == 2:
            x2 = x
            y2 = y-1
        elif mode == 3:
            x2 = x
            y2 = y+1

        qr[y*25+x]   = str(int(qr[y*25+x]) + int(qr[y2*25+x2]))
        qr[y2*25+x2] = str(int(qr[y*25+x]) - int(qr[y2*25+x2]))
        qr[y*25+x]   = str(int(qr[y*25+x]) - int(qr[y2*25+x2]))
    return qr
```

Thankfully, this encryption scheme turns out to be fully reversible and the only change we have to make to turn the encryption function into a decryption function is to reverse the order of the key. Running encrypted.qr through the decryption algorithm gives us a valid QR code that when scanned, prints out the flag.

<img src=qr.jpg>