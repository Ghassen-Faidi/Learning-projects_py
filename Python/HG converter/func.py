# Functions
# Gregorian to Hijri
def GreToHij():
  Greg = int(input("Enter a Gregorin(Miladi) year: \n>>>"))
  # Calculation
  Hij = (Greg-622)/0.97
  # Get rid of the fraction
  frac = Hij - int(Hij)
  if frac > 0.5:
    Hij = int(Hij)+1
  else:
    Hij= int(Hij)
  # final result
  print("The gregorin(Miladi) year", Greg, "is the year", "||",Hij,"||", "in hijri")
  
  
# Hijri to gregorian
def HijToGre():

  Hij = int(input("Enter a hijri year: \n>>>"))

  # Calculation
  gre = 622 + Hij*0.97

  # Get rid of the fraction
  frac = gre - int(gre)
  if frac > 0.5:
    gre = int(gre)+1
  else:
    gre = int(gre)
  # final result 
  print("The hejri year ", Hij, "is the year ","||",gre,"||", "Gregorian(Miladi)")

