
def toString (array):
    string:str = ""
    for digit in array:
        string = string + str(digit)
    return string

def fromDecimal (integer:int):
    remainder:int
    binary:int[32] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    hex = [0,0,0,0,0,0,0,0]
    i:int=31
    isNeg:bool = False
    absinteger:integer = abs(integer)
    if(integer < 0):
        isNeg = True
    while absinteger>0:
        remainder = absinteger%2
        if (remainder != 0):
            binary[i] += 1
        if (binary[i]>=2):
            binary[i] = 0
            binary[i-1] +=1
        i -= 1
        absinteger = absinteger//2
    if (isNeg == True):
        k:int = 0
        for digit in binary:
            if (digit == 0):
                binary[k] = 1
            else:
                binary[k] = 0
            k += 1
        binary[31] += 1
        j:int = 31
        while (j>=0):
            if (binary[j]>=2):
                binary[j] = 0
                binary[j-1] +=1
            j-=1
        
    hex[7] = binary[31]*1 + binary[30]*2 + binary[29]*4 + binary[28]*8
    hex[6] = binary[27]*1 + binary[26]*2 + binary[25]*4 + binary[24]*8
    hex[5] = binary[23]*1 + binary[22]*2 + binary[21]*4 + binary[20]*8
    hex[4] = binary[19]*1 + binary[18]*2 + binary[17]*4 + binary[16]*8
    hex[3] = binary[15]*1 + binary[14]*2 + binary[13]*4 + binary[12]*8
    hex[2] = binary[11]*1 + binary[10]*2 + binary[9]*4 + binary[8]*8
    hex[1] = binary[7]*1 + binary[6]*2 + binary[5]*4 + binary[4]*8
    hex[0] = binary[3]*1 + binary[2]*2 + binary[1]*4 + binary[0]*8

    h:int = 0
    while (h<=7):
        if hex[h] == 10:
            hex[h] = "A"
        if hex[h] == 11:
            hex[h] = "B"
        if hex[h] == 12:
            hex[h] = "C"
        if hex[h] == 13:
            hex[h] = "D"
        if hex[h] == 14:
            hex[h] = "E"
        if hex[h] == 15:
            hex[h] = "F"
        if hex[h] == 16:
            hex[h] = "0"
        h += 1

    return "This integer in base 2 is " + toString(binary) + "\nThis integer in base 16 is " +toString(hex)

decimal = input("Enter an integer, either positive or negative, in base 10: ")
print(fromDecimal(int(decimal)))

# example print statemtent: print(fromDecimal(266166237))

def fromHex(hexNum:str):
    hex = list(hexNum)
    decimal:int = 0
    h:int = 0
    while (h<=7):
        if hex[h] == "1":
            hex[h] = 1
        if hex[h] == "2":
            hex[h] = 2
        if hex[h] == "3":
            hex[h] = 3
        if hex[h] == "4":
            hex[h] = 4
        if hex[h] == "5":
            hex[h] = 5
        if hex[h] == "6":
            hex[h] = 6
        if hex[h] == "7":
            hex[h] = 7
        if hex[h] == "8":
            hex[h] = 8
        if hex[h] == "9":
            hex[h] = 9
        if hex[h] == "A":
            hex[h] = 10
        if hex[h] == "B":
            hex[h] = 11
        if hex[h] == "C":
            hex[h] = 12
        if hex[h] == "D":
            hex[h] = 13
        if hex[h] == "E":
            hex[h] = 14
        if hex[h] == "F":
            hex[h] = 15
        if hex[h] == "0":
            hex[h] = 0
        h += 1
    decimal = hex[7]*1 + hex[6]*16 + hex[5]*256 + hex[4]*4096 + hex[3]*65536 + hex[2]*1048576 + hex[1]*16777216 + hex[0]*268435456
    return "This integer in base 10 is " + str(decimal)

hex = input("Enter a positive integer in base 16: ")
print(fromHex(hex))
#example print statement: print(fromHex("0FDD5FDD"))


