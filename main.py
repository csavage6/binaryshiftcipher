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
    return binaryCharacters[letterCharacters.index(inputChar.lower())]


def convertToLetter(inputChar):
    return letterCharacters[binaryCharacters.index(inputChar)]


def shiftMessage(inputText):
    outputText = inputText
    shiftAmount = randint(1,6)

    displacedChars = outputText[:shiftAmount]
    outputText = outputText[shiftAmount:] + displacedChars

    return outputText, shiftAmount


def unshiftMessage(inputText, shiftAmount):
    outputText = inputText

    displacedChars = outputText[-shiftAmount:]
    outputText = displacedChars + outputText[:-shiftAmount]

    return outputText


def encryptText(inputText):
    pass


def decryptText(inputText):
    textToDecrypt = inputText[:-1]
    shiftAmount = int(inputText[-1])
    pass


def menu():
    pass


if __name__ == "__main__":
    menu()
