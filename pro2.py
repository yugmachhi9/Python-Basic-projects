# robospeaker

import os
y = 0
if y == 0:
    print("wel come ")
    while True:
      x = input("enter what u want me to speak:")
      if x== "q":
        break
      command = f"say {x}"
      os.system(command)    

      





