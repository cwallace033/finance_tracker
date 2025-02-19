# Overview

This is a finance tracker. It keeps things pretty basic by putting everything in either income or expense. It uses Python and Google Firebase. All of the information is stored in the cloud database so that it exists longer than just the duration of the program runtime. 

I wrote this program to gain experience in using cloud databases in programming. It helped me to see how I can use databases in my coding to easily save information and make it more accessible in the code for later use. 


[Software Demo Video](https://youtu.be/QlWPmHQfN5s)

# Cloud Database

The Database that I chose to use was through Google's Firebase. 

This database has a collection for users. This is where basic user information is stored as well as the balance total. There is another collection that keeps track of all the transactions made including the transaction ID, amount, type, and description. 
# Development Environment

For creating this program I used several libraries in Python. Since there is an env in this I had to use the dotenv so that private information can be used but remain private. I also used the datetime library to give all of the transactions timestamps. 

# Useful Websites

- [Web Site Name](https://firebase.google.com/docs/firestore)
- [Web Site Name](https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/)

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- There are some input validation items that I would like to put in place here. Currently the program could crash if the user entered in incorrect information when adding transactions. 
- I also want to add user validation to the project so that when a user id is selected a password must be entered in order to modify anything on the account. 
