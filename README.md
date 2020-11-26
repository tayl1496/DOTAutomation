# DOT Program automation

## What Is This

The DOT program is a method that I use in retail to mark items that are missing to look into them. This includes ordering them in or finding them where they are missplaced. I wrote this program for my current work setting that uses the S2K POS system. The IT team was not allowing for a solution to increase workflow so here is my Hack solution. It uses PyQt5 for the Frontend, Selenium to scrape S2K, and then openpyxl to display it in an Excel File because that is what we are currently using. There are many places for improvements I am sure.

### Steps to start

1. place chrome driver in folder C:\Users\$USER_NAME$\webdriver
2. Ensure Requirements are met if building from source this includes
    * PyQt5
    * Selenium
    * openpyxl
