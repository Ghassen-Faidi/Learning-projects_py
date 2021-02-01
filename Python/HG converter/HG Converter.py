# call functions from func.py
from func import GreToHij, HijToGre

msg = """
please typing a number(1/2)
1/ Gregorian to Hijri
2/ Hijri to Gregorian
>>> """

# Ask again if the user didn't write correctly
while True:
  answer = input(msg)
  if answer != "1" and answer!= "2":
    continue # Jump back to the start of the loop
  else:
    break # leave the loop

if answer == "1":
  GreToHij()
elif answer == "2":
  HijToGre()

input("")