from random import randint

letterCharacters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+[{]}|;:\'\",./? "
binaryCharacters = ["000000", "000001", "000010", "000011", "000100", "000101", "000110", "000111",
                    "001000", "001001", "001010", "001011", "001100", "001101", "001110", "001111",
                    "010000", "010001", "010010", "010011", "010100", "010101", "010110", "010111",
                    "011000", "011001", "011010", "011011", "011100", "011101", "011110", "011111",
                    "100000", "100001", "100010", "100011", "100100", "100101", "100110", "100111",
                    "101000", "101001", "101010", "101011", "101100", "101101", "101110", "101111",
                    "110000", "110001", "110010", "110011", "110100", "110101", "110110", "110111",
                    "111000", "111001", "111010", "111011", "111100", "111101", "111110", "111111"]


def convertToBinary(inputChar):
    if inputChar.lower() in letterCharacters:
        return binaryCharacters[letterCharacters.index(inputChar.lower())]

    return binaryCharacters[letterCharacters.index("*")]


def convertToLetter(inputChar):
    return letterCharacters[binaryCharacters.index(inputChar)]


def shiftMessage(inputText):
    shiftAmount = randint(1,6)
    displacedChars = inputText[:shiftAmount]
    outputText = inputText[shiftAmount:] + displacedChars

    return outputText, shiftAmount


def unshiftMessage(inputText, shiftAmount):
    displacedChars = inputText[-shiftAmount:]
    outputText = displacedChars + inputText[:-shiftAmount]

    return outputText


def cipherText(inputText):
    intermediateText = ""

    for i in inputText:
        intermediateText += convertToBinary(i)

    intermediateText, shiftAmount = shiftMessage(intermediateText)
    outputText = ""

    for i in range(0,len(intermediateText), 6):
        sixDigitChar = intermediateText[i:i+6]
        outputText += convertToLetter(sixDigitChar)

    outputText += str(shiftAmount)
    return outputText


def decipherText(inputText):
    textToDecrypt = inputText[:-1]
    shiftAmount = int(inputText[-1])
    intermediateText = ""

    for i in textToDecrypt:
        intermediateText += convertToBinary(i)

    intermediateText = unshiftMessage(intermediateText, shiftAmount)
    outputText = ""

    for i in range(0, len(intermediateText), 6):
        sixDigitChar = intermediateText[i:i+6]
        outputText += convertToLetter(sixDigitChar)

    return outputText


def menu():
    choice = "0"

    while choice != "q":
        print("What would you like to do?")
        print("1. Cipher")
        print("2. Decipher")
        print("q. Quit")
        choice = str(input())

        if choice == "1":
            outputText = cipherText(input("What would you like to cipher?\n"))
            print()
            print(f"Ciphered Text:\t{outputText}")
            print()

        elif choice == "2":
            outputText = decipherText(input("What would you like to decipher?\n"))
            print()
            print(f"Deciphered Text:\t{outputText}")
            print()

    print("Bye!")


if __name__ == "__main__":
    menu()
