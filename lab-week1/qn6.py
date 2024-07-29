def describe_noise_level(decibel):
    if decibel == 130:
        return "Noise is JackHammer"
    if decibel == 106:
        return "Noise is Gas Lawnmower"
    if decibel == 70:
        return "Noise is Alarm Clock"
    if decibel == 40:
        return "Noise is Quiet room"
    if 106 < decibel < 130:
        return "Noise is between the level Jack Hammer and Gas Lawnmower"
    if 70 < decibel < 106:
        return "Noise is between the level Alarm Clock and Gas Lawnmower"
    if 40 < decibel < 70:
        return "Noise is between the level Quiet Room and Alarm Clock"
    if decibel > 130:
        return "Noise level is larger than 130 [JackHammer]"
    else:
        return "Noise level is smaller than 40 [Quiet room]"

# Example usage:
noise_description = describe_noise_level(int(input("Enter the decibel :")))
print(noise_description)
