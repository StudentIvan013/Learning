import math

def y(x):
 if (x == -2 or x == 0 or x == 1):
     print("No")
 elif (x <= -1):
     print(calculateFromula1(x))
 elif (x > 0.5):
     print(calculateFromula2(x))
 else:
     print(calculateFromula3(x))


def calculateFromula1(x):
  return x/(x**2 - 4)


def calculateFromula2(x):
  return math.cos(math.pi/x)/math.sin(math.pi/x)


def calculateFromula3(x):
  return math.log10(x+7*math.sqrt(x))
