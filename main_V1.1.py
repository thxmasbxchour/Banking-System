"""

Banking System - Created by Thomas

"""

import random
from datetime import datetime
from dateutil.relativedelta import relativedelta
import csv
import pandas as pd
import os
import time
import shutil
from tempfile import NamedTemporaryFile
import colorama
from colorama import Fore

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
reset = Fore.RESET


class Form():

  def __init__(self):
    pass

  def login_register(self):
    print(f"""
        
        {blue}Welcome to Aced Bank! How can we assist you today?{reset}
        
        """)
    q = input("Do you want to register/login > ")
    if q.lower() == "register".lower():

      mycustomers = Register("sortcode", "name", "valid_from", "valid_end",
                             "account_num", "card_num", "cvv")
      mycustomers.do_tasks_and_add_data_to_file()

    elif q.lower() == "login".lower():

      #print("Login Page in working stages")
      mylogin = Login("username", "password")
      mylogin.check_user_pass()
    else:
      print("Incorrect Input!")
      self.register()


class Login():

  def __init__(self, user, pswrd):
    super().__init__()
    self.user = input("What is your username > ").lower()
    self.pswrd = input("What is your password > ")

  def check_user_pass(self):
    #user = input("What is your username > ")
    #pswrd = input("What is your password > ")
    dataset = pd.read_csv("info.csv")
    data = dataset.iloc[:, 7].values
    data1 = dataset.iloc[:, 8].values
    if self.user in data:

      if self.pswrd in data1:
        print(f"{green}Access Granted{reset}")
        time.sleep(1)
        os.system("cls")
        print("Loading you in now.")
        time.sleep(1)
        os.system("cls")
        print("Loading you in now..")
        time.sleep(1)
        os.system("cls")
        print("Loading you in now...")
        time.sleep(1)
        os.system("cls")
        myhomepage = HomePage(self.user, self.pswrd)
        myhomepage.balance()

    else:
      print("Can't find either username or password! Try again!")
      mylogin = Login(self.user, self.pswrd)


class Register():

  nums = "1234567890"

  def __init__(self, sortcode, name, valid_from, valid_end, account_num,
               card_num, cvv):  # Defines everything
    super().__init__()
    self.sortcode = sortcode
    self.name = name
    self.valid_from = valid_from
    self.valid_end = valid_end
    self.account_num = account_num
    self.card_num = card_num
    self.cvv = cvv

  def username(self):
    username1 = input("What do you want your username to be > ")
    username1 = username1.lower()
    dataset = pd.read_csv("info.csv")
    data = dataset.iloc[:, 7].values
    if username1 in data:
      print("Useranme Unavailable. Please try another username.")
      quit()
    elif username1 not in data:
      print("Username Available. Adding you to DB now.")
    return username1

  def password(self):
    password1 = input("What do you want your password to be: ")
    dataset = pd.read_csv("info.csv")
    data = dataset.iloc[:, 8].values
    print("Nice Job. Adding your account to Database. Please bare with us.")
    return password1

  def get_name(self):
    name1 = input("What is the name that you want to be on your card > "
                  )  # Gets your name to be displayed and added to DB
    print(f"The name on your card will be : {name1}")
    return name1

  def sort_code(self):
    mylist = []
    for i in range(0, 6):
      sort_number = random.choice(
        self.nums
      )  # Randomly selects your digits from the previously defined variable
      mylist.append(sort_number)
    mylist.insert(
      2, "-"
    )  # Puts spaces between the certain numbers so it looks like a sort code
    mylist.insert(5, "-")
    sort_code_num = ''.join(mylist)

    print(f"Your sort code is: {sort_code_num}")
    return sort_code_num

  def account_number(self):
    mylist = []
    for i in range(0, 8):
      acct_num = random.choice(
        self.nums)  # Selects random choice of numbers for account number
      mylist.append(acct_num)

    strings_acct_num = ''.join(mylist)
    dataset = pd.read_csv("info.csv")
    data = dataset.iloc[:, 3].values.astype(str)
    if strings_acct_num in data:  # Checks if Account Number taken
      self.account_number()

    else:
      print(f"Your account number is: {str(strings_acct_num)}")
      return strings_acct_num

  def cvv_num(self):
    mylist = []
    for i in range(0, 3):
      cvv_num = random.choice(
        self.nums)  # Selects random choice of numbers for CVV (only 3)
      mylist.append(cvv_num)

    string_cvv_num = ''.join(mylist)
    print(f"Your CVV is: {string_cvv_num}")
    return string_cvv_num

  def card_number(self):
    mylist = []
    for i in range(0, 16):
      card_number = random.choice(
        self.nums)  # Selects random choice of numbers for card number
      mylist.append(card_number)
    mylist.insert(4, " ")
    mylist.insert(9, " ")
    mylist.insert(14, " ")
    card_num_string = ''.join(mylist)  # Combines the numbers
    dataset = pd.read_csv("info.csv")
    data = dataset.iloc[:, 1].values.astype(str)

    if card_num_string in data:  # Checks if Account Number taken
      print("Test")
      self.card_number()

    else:
      print(f"Your card number is: {card_num_string}")
      return card_num_string

  def ValidFrom(self):

    currentMonth = datetime.now().month
    currentYear = datetime.now().year

    print("Valid From: " + str(currentMonth) + "/" +
          str(currentYear))  # Puts year and month together
    return str(currentMonth) + "/" + str(currentYear)

  def ValidEnd(self):

    fiveyears = datetime.now() + relativedelta(
      months=60)  # Gets 5 years into future
    month = fiveyears.month
    year = fiveyears.year

    print("Valid Till: " + str(month) + "/" +
          str(year))  # Puts year and month together
    return str(month) + "/" + str(year)

  def __str__(self):
    return f"{self.username}"

  def do_tasks_and_add_data_to_file(self):
    data_to_append = [[
      self.get_name(),
      self.card_number(),
      self.sort_code(),
      self.account_number(),
      self.cvv_num(),
      self.ValidFrom(),
      self.ValidEnd(),
      self.username(),
      self.password(), '0'
    ]]

    file = open("info.csv", "a", newline="")
    writer = csv.writer(file)

    writer.writerows(data_to_append)
    file.close()
    input("Press enter when you're ready to login!")
    os.system("cls")
    mylogin = Login("username", "password")
    mylogin.check_user_pass()

  #def do_tasks(self): # Does all methods at once
  #self.get_name()
  #self.card_number()
  #self.sort_code()
  #self.account_number()
  #self.cvv_num()
  #self.ValidFrom()
  #self.ValidEnd()
  #self.username()
  #self.password()
  #self.add_data_to_file()


class HomePage(Login):

  def __init__(self, user, pswrd):
    self.user = user
    self.pswrd = pswrd

  def view_card_details(self):
    with open('info.csv', newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        if row[8] == self.pswrd:
          if row[7] == self.user:
            info = row
            os.system("cls")
            print(f"Name: {row[0]}")
            print(f"Card Number: {row[1]}")
            print(f"Sort Code: {row[2]}")
            print(f"Account Number: {row[3]}")
            print(f"CVV: {row[4]}")
            print(f"Valid From: {row[5]}")
            print(f"Expiry Date: {row[6]}")
            print(f"Username: {row[7]}")
            print(f"Password: {row[8]}")

  def balance(self):

    with open('info.csv', newline='') as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        if row[8] == self.pswrd:
          if row[7] == self.user:
            Balance = row[9]
            print(f"Your available balance is: £{row[9]}")
            self.to_do()
            return Balance

  def to_do(self):
    print("Would you like to either:")
    print("1. Transfer Money")
    print("2. Change Username")
    print("3. Change Password")
    print("4. View Card Details/Bank Information")
    print("5. Exit Bank Account")
    q = input("")  # Asks user if they want to send money

    if q == "1":  # Checks if "1" was written
      os.system("cls")
      print(f"""
            
            {blue}Money Transferring{reset}
            
            
            """)
      sort = input(
        "What is the sort code of the person you would like to send money to > "
      )  # Asks the user the sort code of the reciever
      acct_num = int(
        input(
          "What is the account number of the person you would like to send money to > "
        ))  # Asks the user the account number of the reciever
      amount = float(input("How much money would you like to send to them > ")
                     )  # Asks the user how much money they would like to send
      df = pd.read_csv("info.csv")  # Opens and reads info.csv
      mask = (df['sortcode'] == sort) & (
        df['accountnum'] == acct_num
      )  # Checks if the sort code and account number in the file = the one provided by the user
      if mask.any(
      ):  # Checks if the mask variable is True with the .any() command
        with open(
            'info.csv',
            newline='') as csvfile:  # Basically does the method balance()
          reader = csv.reader(csvfile)
          for row in reader:
            if row[8] == self.pswrd:
              if row[7] == self.user:
                Balance = float(row[9])  # Basically does the method balance()

        if (Balance >= amount):
          df.loc[mask,
                 'balance'] += amount  # Adds the amount the balance section
          df.to_csv('info.csv',
                    index=False)  # Replaces temp file with original one

          df = pd.read_csv("info.csv")  # Opens file
          mask1 = df['username'] == self.user  # Looks for users name in DB
          if mask1.any():  # Checks if mask1 is True
            df.loc[
              mask1,
              'balance'] -= amount  # Minuses the amount specified by the user from senders account
            df.to_csv("info.csv",
                      index=False)  # Replaces temp file with original one

            with open("info.csv",
                      newline="") as csvfile:  # Opens the csv file again
              reader = csv.reader(
                csvfile)  # Creates variable to read the csv file
              for row in reader:  # Iterates through all the rows in the csv file
                if str(acct_num) in row[
                    3]:  # Checks if the account number is in the correct row
                  reciever = row[
                    7]  # Makes the username of the reciever into a variable

                  date = datetime.now().strftime(
                    '%Y-%m-%d %H:%M:%S')  # Gets the exact date and time
                  append_info = [
                    self.user, reciever, amount, date
                  ]  # Gets the information we are going to add to our file
                  with open(
                      'transactions.csv', 'a', newline=""
                  ) as csvfile:  # Opens the csv file we are storing our data in
                    writer_object = csv.writer(
                      csvfile
                    )  # Makes a writer object so we can write into the file
                    writer_object.writerow(
                      append_info
                    )  # Writes the information to a new row in the file
                    csvfile.close(
                    )  # Closes the file so no data breaches can occur

          done = input(
            "Succesfully Completed Transaction. Press Enter to see balance or 'exit' to quit > "
          )
          if done == "":
            self.balance()
          elif done.lower() == "exit".lower():
            print("Thanks for using Aced Bank!")
            quit()
          else:
            self.balance()
        elif (Balance
              < amount):  # Checks if your balance is bigger than amount
          input("Insufficent Funds. Press enter to try again.")
          os.system("cls")
          self.balance()

      else:
        print("Person not found in our database! Please try again!")
        self.to_do()

    elif q == "2":
      os.system("cls")
      mychangeinfo = ChangeInformation(self.user, self.pswrd)
      mychangeinfo.change_username()

    elif q == "3":
      os.system("cls")
      mychangeinfo = ChangeInformation(self.user, self.pswrd)
      mychangeinfo.change_password()

    elif q == "4":
      os.system("cls")
      self.view_card_details()

    elif q == "5":
      print("Thanks for using Aced Bank")
      quit()

    else:
      print("Incorrect Input")
      self.to_do()


class ChangeInformation(Login, Form):

  def __init__(self, user, pswrd):
    self.user = user
    self.pswrd = pswrd

  def change_username(self):
    new_username = input("What do you want your new username to be > ")
    dataset = pd.read_csv("info.csv")
    data = dataset.iloc[:, 7].values
    if new_username.lower() in data:
      print("Useranme Unavailable. Please try another username.")
      self.change_username()
    elif new_username.lower() not in data:
      df = pd.read_csv("info.csv")
      mask = (df['username'] == self.user) & (
        df['password'] == self.pswrd
      )  # Checks if the username and pswrd in the file = the one provided by the user
      if mask.any():
        with open(
            'info.csv',
            newline='') as csvfile:  # Basically does the method balance()
          reader = csv.reader(csvfile)
          for row in reader:
            if row[8] == self.pswrd:
              if row[7] == self.user:
                print("Succesfully Changed your information!")

          df.loc[
            mask,
            'username'] = new_username  # Adds the amount the balance section
          df.to_csv('info.csv',
                    index=False)  # Replaces temp file with original one

    else:
      print("Couldnt find")

  def change_password(self):
    new_pswrd = input("What do you want your new password to be > ")
    df = pd.read_csv("info.csv")
    print(self.user)
    mask = (df['username'] == self.user) & (
      df['password'] == self.pswrd
    )  # Checks if the username and pswrd in the file = the one provided by the user
    if mask.any():
      with open('info.csv',
                newline='') as csvfile:  # Basically does the method balance()
        reader = csv.reader(csvfile)
        for row in reader:
          if row[8] == self.pswrd:
            if row[7] == self.user:
              print("Succesfully Changed your information!")

        df.loc[mask,
               'password'] = new_pswrd  # Adds the amount the balance section
        df.to_csv('info.csv',
                  index=False)  # Replaces temp file with original one
        self.login_register()

    else:
      print("Couldnt find")


myregister = Form()
myregister.login_register()
