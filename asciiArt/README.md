#ASCII Art
A 6 point coding challenge from https://ringzer0team.com/challenges/119

Once a player logs in and load the page they are greeted with the following message and a seriers of ASCII art numbers of the following form.

```
You have 2 seconds to send the number you see 
Send the answer back using https://ringzer0team.com/challenges/119/[number]

----- BEGIN MESSAGE -----

 xxx 
x   x 
  xx 
 x   
xxxxx

 x   x
x    x
 xxxxx
     x
    x
...
----- END MESSAGE -----
```

Each time you refresh the page a different series of 10 numbers will appear.

There's nothing fancy going on here in terms of exploitability, the challenge is simply to write a program which can parse the numbers out of the page and submit them back in the form described in the problem's outline.

The first step then was getting the webpage into the program. Fortunatly there's a great number of python libraries for all sorts of web based activities. I went with requests as it was a very simple ans stright forward way to get started.
