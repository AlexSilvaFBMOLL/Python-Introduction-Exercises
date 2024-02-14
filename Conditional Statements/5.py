def multipleOf5And7(integer):
  if (integer % 5 == 0) & (integer % 7 == 0):
    print("Es múltiplo de 5 y 7")
  elif (integer % 5 == 0):
    print("Sólo es múltiplo de 5")
  elif (integer % 7 == 0):
    print("Sólo es múltiplo de 7")
  else:
    print("No es múltiplo de 5 o 7")

multipleOf5And7(35)