coefficientList = []
derivativeList = []

def getCoefficients():
  
  degree = int(input("Degree of polynomial: "))

  for i in range(degree + 1):
    coefficientList.append(int(input("Coefficient of x^" + str(degree-i) + ": ")))

# Derivative Taker

def derivative():

  for i in range(len(coefficientList)-1):
    derivativeList.append(coefficientList[i] * (len(coefficientList)-(i+1)))


getCoefficients()
derivative()


# Note that Newton's Method progresses as follows

# Take initial seed x0
# Evaluate f(x0) and f'(x0)
# deltax = f(x0)/f'(x0)
# x1 = x0 - deltax

def f(x):

  result = 0
  
  for i in range(len(coefficientList)):
    result += coefficientList[i] * (x**(len(coefficientList)-(i+1)))
  
  return result

def fPrime(x):

  result = 0

  for i in range(len(derivativeList)):
    result += derivativeList[i] * (x**(len(derivativeList)-(i+1)))

  return result

def newtonsMethod(x, precision):
  
  for i in range(precision):
    x = x - (f(x)/fPrime(x))

    print("Guess " + str(i+1) + ": " + str(x))

  return x

print("Final Guess: " + str(newtonsMethod(int(input("What do you want your initial guess to be?")), int(input("How many iterations do you want to run?")))))