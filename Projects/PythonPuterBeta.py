from time import sleep
import sys
import random
hi = "0"
# Start Computer

print("Do you want to start the computer?")
startcomputer = input("[y]/[n]:")
if startcomputer == "y":
  text = "Loading ..........."
  for character in text:
    sys.stdout.write(character)
    sleep(0.2)
  login = 1
if startcomputer == "n":
  print("Shutting Down")
# Login
if login == 1:
  print("\n" * 1)
  print("Starting Computer")
  Username = input("Username: ")
  Password = input("Password: ")
  
# Login Check
attempts = 1
while Username != "ADMIN" or Password !="ADMIN":
  if attempts <3:
    print("Wrong Username or Password")
    attempts += 1
    Username = input("Username:")
    Password = input("Password:")
  else:
    if hi == "0":
      print("Allowed attempts exceeded")
      hi = hi + "1"
      quit()
    
    
