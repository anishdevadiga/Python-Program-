decibel = float(input("Enter the decibel level : "))
if decibel == 130:
    print("Noise is JackHammer")
elif decibel == 106 :
    print("Noise is Gas Lawnmower")
elif decibel==70:
    print("Noise is Alarm Clock")
elif decibel==40:
    print("Noise is Quiet room")
elif decibel >106 and  decibel < 130 :
     print("Noise is between the level Jack Hammer and Gas Lawnmower ")
elif decibel >70 and  decibel < 106 :
     print("Noise is between the level Alarm Clock and Gas Lawnmower ")
elif decibel >40 and  decibel < 70 :
     print("Noise is between the level Quiet Room  and Alarm Rock")
elif decibel >130 :
    print("Noise level is larger than 130[JackHammer]")
else:
    print("Noise level is smaller than 40[Quiet room]")

