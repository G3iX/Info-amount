# from code import get_file_size


BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

def readfile(num, type, bool): # false if base64encoded text
    if bool:
        file = open("destextes/" + str(num) + "." + str(type), "r", encoding="utf8")
        total_text = ""
        #LetterD = {}
        LetterD = {"А": 0, "Б": 0, "В": 0, "Г": 0, "Ґ": 0, "Д": 0, "Е": 0, "Є": 0, "Ж": 0, "З": 0, "И": 0, "І": 0,
                      "Ї": 0, "Й": 0, "К": 0, "Л": 0, "М": 0, "Н": 0, "О": 0, "П": 0,
                      "Р": 0, "С": 0, "Т": 0, "У": 0, "Ф": 0, "Х": 0, "Ц": 0, "Ч": 0, "Ш": 0, "Щ": 0, "Ь": 0, "Ю": 0,
                      "Я": 0,"а": 0, "б": 0, "в": 0, "г": 0, "ґ": 0, "д": 0, "е": 0, "є": 0, "ж": 0, "з": 0, "и": 0, "і": 0,
                      "ї": 0, "й": 0, "к": 0, "л": 0, "м": 0, "н": 0, "о": 0, "п": 0,
                      "р": 0, "с": 0, "т": 0, "у": 0, "ф": 0, "х": 0, "ц": 0, "ч": 0, "ш": 0, "щ": 0, "ь": 0, "ю": 0,
                      "я": 0}
        totlen = 0
        for i in file.read():
            # print(i)
            total_text += i
            totlen += 1
            try:
                LetterD[i] += 1
            except:
                continue # LetterD.update({i: 1}) # continue
        file.close()
        alphabetPwr = len(LetterD)
        #total_text = file.read()
    else:
        file = open("destextes/" + str(num) + "_base64." + str(type), "r", encoding="utf8")
        total_text = ""
        # LetterD = {}
        LetterD = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0,
                         "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
                         "Y": 0, "Z": 0,"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                         "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                         "y": 0, "z": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0,
                         "+": 0, "/": 0, "=": 0}
        totlen = 0
        for i in file.read():
            # print(i)
            total_text += i
            totlen += 1
            try:
                LetterD[i] += 1
            except:
                continue # LetterD.update({i: 1})  # continue
        file.close()
        alphabetPwr = len(LetterD)
        # total_text = file.read()
    return total_text,LetterD, totlen, alphabetPwr


def textbase64(data):
    result = ""
    padding = 0

    dataencoded = data.encode("utf-8")
    binary_data = ("".join(format(byte, 'b') for byte in dataencoded))
    print(dataencoded)
    print(binary_data)
    chunks = [binary_data[i:i + 24] for i in range(0, len(binary_data), 24)]
    print(chunks)
    result = ""
    return result

filenum = 2
data,UkrLetterD, Ukrtotallen, UkrAlphabet_power = readfile(filenum,"txt", True)
print(data)
print("----")
#print(UkrLetterD)


base64_text = textbase64(data)
print("Base64 encoded text:", base64_text)
try:
    f = open("destextes/"+str(filenum)+"_base64.txt", "w")
    f.writelines(base64_text)
    f.close()
except:
    print("error")

# dataBase,UkrLetterBase, UkrtotallenBase, BaseAlphabet_power = readfile(filenum,"txt", False)

