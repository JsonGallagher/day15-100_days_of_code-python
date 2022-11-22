exit = ""
while exit != "yes":
  animal = input("What animal do you want? ")
  if animal.lower() == 'cow':
    print(f"The {animal} goes mooo. 🐮")
  elif animal.lower() == 'sheep':
    print(f"The {animal} goes baaa. 🐑 ")
  elif animal.lower() == 'duck':
    print(f"The {animal} goes quack. 🦆")
  else:
    print('Hmm. I dont know that animal yet, I should probably get out more.')
  exit = input("Exit?: ")
print("Program exited. Goodbye!")