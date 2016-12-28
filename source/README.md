##Source code

I came up with two different ways of extracting the company names and links from the event pages.

###fetch.js

I first started off with this script that I'd run in my browser's Javascript console when I was on the event page, and I'd copy the console's output to a local text file. This method was used for the [fall 2016 fairs.](../2016-fall)

###process-html.py

I decided to move towards Markdown format and I wanted to automate the process more. I wanted a Python script that would make a GET request to download the html with all the companies shown (250 at a time), but the Career Center website used some generated URL query parameter to indicate the number of companies shown and I was unable to figure out how it was generated; it was likely generated from server-side code. So, I stuck to saving the html with all of the companies and then running my Python script process on that local file. My script outputted the companies' names and links in Markdown format, and I could easily redirect that output to a new file, which was much more convenient than copying and pasting a large chunk of text from my browser's Javascript console. This method was used for the [winter 2017 fairs.](../2017-winter)
