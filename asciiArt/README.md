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

The first step then was getting the webpage into the program. Fortunately there's a great number of python libraries for all sorts of web based activities. I went with requests as it was a very simple ans straight forward way to get started. Working our way down in <a href="asciiArt.py">asciiArt.py</a> we see the import for requests, the base url of the challenge, then a dictionary associating the ascii art numbers to their integer equivalents. This was the slowest part of the challenge as it required refreshing the page multiple times to ensure I had got examples of each number then had to copy and paste the html responsible for displaying them to my script. There are certainly other ways to do this part, but I fiddled with this for a bit and am very pleased with how my solution turned out.

The next few lines of code were responsible for fetching the web page, and parsing out the raw message data. This data was then run through a loop comparing it to the dictionary setup previously, with a special case for the number 5. The issue with 5 was that unlike the rest of the numbers it was missing a bordering return character. I can't say for certain that the problem's creator did this on purpose, but it added a little extra challenge to the problem.

Following the number parsing I printed out the number my code had found before appending it on to the url and loading the new page. I had to solve this problem a few times before I actually got the flag, the first few tries I was printing all the request data to the console, which was far too hard to read. That's why the last couple lines write the webpage containing the flag to a file for easy reading.

I usually enjoy these coding problems and this one was no different. It's not very hard or complex, but it's a great exercise in scripting and I was proud of myself at the end. To add a little extra fun I was racing against two of my co-workers to see who could finish first, and although I didn't win (I came in last by 5 seconds), I felt that I had written the best script of the three of us and mine was a good deal shorter to boot!
