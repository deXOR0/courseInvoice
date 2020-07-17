# courseInvoice
A small program to calculate my course pricing and generate invoice, written in Python

# version 0.2.1
- Added arguments feature to use the program without interactive mode
- Minor bug fixes
  - Delete redudant checking for interactive mode
  - Fixed hours option shows when user inputted begin and end time in interactive mode

# Why?
I've been tutoring for almost a year now, and it's tiring to have to calculate how much the students have to pay me everytime I tutored them (I got paid by the hour)
So, I developed a very simple program to do the calculation, as well as generate a small message that contains all of the necessary information, that I later can send
to the student or the student's parent.

# The Price Calculation Algorithm
The algorithm I use to calculate the price is a very simple implementation of the Greedy Algorithm, you can read more about it [here](https://www.geeksforgeeks.org/greedy-algorithms/)

# How to use
Download the source code and run it using python 3, if you want to use interactive mode (i.e. there's a console-based user interface), you can type 
python {name_of_the_file.py} interactive, if you want to use it without the interactive mode, just type python {name_of_the_file.py} args [-h] -r  -s  [-b] [-e] [-t]
Use -h argument to see all of the tags functionality
