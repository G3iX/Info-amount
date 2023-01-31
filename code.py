from math import log2

# from collections import Counter

def get_file_size(filename):
    size = 0
    with open(filename, "rb") as f:
        while True:
            block = f.read(4096)
            if not block:
                break
            size += len(block)
    return size


def entropy(inmputdict):
    sigma_m_i = 0
    for i in inmputdict: # m = 33
        try:
            # print(i)
            # print(log2(1/inmputdict[i]))
            sigma_m_i += inmputdict[i] * log2(1/inmputdict[i])
        except:
            continue
    #print("H =", round(sigma_m_i, 5))
    return sigma_m_i

def Letterprobability(inmputdict, totallen):
    # print("Total file len:", totallen)
    UkrLetterP = {}
    for i in inmputdict:
        temp = round(inmputdict[i]/totallen, 8)
        # print("letter '", i, "' show up", inmputdict[i], "times. Probability:",temp)
        UkrLetterP.update({i: temp})
    # print(UkrLetterP)
    return UkrLetterP


def zipsizeNotes(num): # size of file archivated in zip
    from zipfile import ZipFile
    zp = ZipFile("destextes/"+str(num)+".zip")
    size = sum([info.file_size for info in zp.filelist])
    # zip_kb = float(size) / 1000  # kB
    # print(zip_kb)
    zip_bytes = float(size)
    # print(zip_bytes)
    # zip_bits = float(size)*8 # bits
    with ZipFile('destextes/'+str(num)+'.zip') as myzip:
        with myzip.open('1.txt') as myfile:
            for i in myfile:
                print([i])
    return zip_bytes

# def Base64encode(filename):


def readfileprobability (num, boolean_if_trueUkr):
    if boolean_if_trueUkr:
        file = open("destextes/"+str(num)+".txt", "r", encoding="utf8")
        UkrLetterD = {"А": 0, "Б": 0, "В": 0, "Г": 0, "Ґ": 0, "Д": 0, "Е": 0, "Є": 0, "Ж": 0, "З": 0, "И": 0, "І": 0,
                      "Ї": 0, "Й": 0, "К": 0, "Л": 0, "М": 0, "Н": 0, "О": 0, "П": 0,
                      "Р": 0, "С": 0, "Т": 0, "У": 0, "Ф": 0, "Х": 0, "Ц": 0, "Ч": 0, "Ш": 0, "Щ": 0, "Ь": 0, "Ю": 0,
                      "Я": 0,"а": 0, "б": 0, "в": 0, "г": 0, "ґ": 0, "д": 0, "е": 0, "є": 0, "ж": 0, "з": 0, "и": 0, "і": 0,
                      "ї": 0, "й": 0, "к": 0, "л": 0, "м": 0, "н": 0, "о": 0, "п": 0,
                      "р": 0, "с": 0, "т": 0, "у": 0, "ф": 0, "х": 0, "ц": 0, "ч": 0, "ш": 0, "щ": 0, "ь": 0, "ю": 0,
                      "я": 0}  # "A":0, ,".": 0,",": 0,"!": 0,"?": 0,"-": 0 - do we even need it?
    else:
        file = open("destextes/" + str(num) + "_base64.txt", "r", encoding="utf8")
        UkrLetterD = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0,
                         "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
                         "Y": 0, "Z": 0,"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                         "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                         "y": 0, "z": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0,
                         "+": 0, "/": 0, "=": 0} # Base64LetterD
    # total alp len 33
    totlen = 0
    for i in file.read(): # why it read only as lovercase letters?
        #print(i)
        totlen += 1
        try:
            UkrLetterD[i] += 1
        except:
            UkrLetterD.update({i: 1}) # continue
    alphabetPwr = len(UkrLetterD)
    return UkrLetterD, totlen, alphabetPwr

    # entropy(Letterprobability(UkrLetterD, totlen))
    # with open('destextes/1.txt', 'r', encoding="utf8") as file:
    #     text = file.read().replace('\n', '')
    # frequency = Counter(text)
    # print("-------by counter-------")
    # Letterprobability(frequency,totlen)
    #
    # return UkrLetterD # return symbols amount
    # text = open("1.txt", 'r', encoding="cp1251").read()
    # text
def execute(LetterprobabilityAmount, totallen, power, filenum):

    filetype = ["txt","zip", "rar", "xz", "gz", "bz2"]


    print("total char len:",totallen)
    print("alphabet power:", power)
    print("letter amount:\n",LetterprobabilityAmount)
    LetterprobabilityDict = Letterprobability(LetterprobabilityAmount, totallen)
    print("letter probability:\n", LetterprobabilityDict)
    test3 = entropy(LetterprobabilityDict)
    H_f = round(test3,5)
    print("H =",H_f)
    infomount = (H_f * totallen)*0.125 # /8
    print("Information:",round(infomount, 3), "bytes")
    filesize = get_file_size("destextes/"+str(filenum)+"."+filetype[0])
    print("file size:",filesize, "bytes")
    zipsize = get_file_size("destextes/"+str(filenum)+'.'+filetype[1])
    print("zipped size:", zipsize, "bytes")
    rarsize = get_file_size("destextes/" + str(filenum) + '.' + filetype[2])
    print("rared size:", rarsize, "bytes")
    xzsize = get_file_size("destextes/" + str(filenum) + '.' + filetype[3])
    print("xzed size:", xzsize, "bytes")
    gzipsize = get_file_size("destextes/" + str(filenum) + '.' + filetype[4])
    print("gzipped size:", gzipsize, "bytes")
    bzipsize = get_file_size("destextes/" + str(filenum) + '.' + filetype[5])
    print("bzipped size:", bzipsize, "bytes")
    base64fz = get_file_size("destextes/" + str(filenum) + '_base64.' + filetype[0])
    print("based64 size:", base64fz, "bytes")
    return LetterprobabilityAmount, LetterprobabilityDict, H_f, infomount, filesize, zipsize, rarsize, xzsize, gzipsize, bzipsize, base64fz

def preettyoutput(LetterprobabilityAmount, LetterprobabilityDict, H_f, infomount, filesize, zipsize, rarsize, xzsize, gzipsize, bzipsize, base64fsz):
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["Letter", "Amount", "Probability"]
    for i in LetterprobabilityDict:
        table.add_row(["'"+i+"'", LetterprobabilityAmount[i], LetterprobabilityDict[i]])
        # print(i,"-",test1[i], "-", test2[i])
    table2 = PrettyTable()
    table2.field_names = ["Variable name","Value", "dT"]
    table2.add_row(["Average UKR entropy",H_f, ''])
    table2.add_row(["---------", 5.51, ' -----'])
    table2.add_row(["Information Amount", (round(infomount, 3))," bytes"])
    table2.add_row(["Actual File size", (filesize) ," bytes"])
    table2.add_row(["Zipped File size", (round(zipsize, 4))," bytes"])
    table2.add_row(["Rared File size", (round(rarsize, 4))," bytes"])
    table2.add_row(["Xzed File size", (round(xzsize, 4))," bytes"])
    table2.add_row(["Gzipped File size", round(gzipsize, 4)," bytes"])
    table2.add_row(["Bzipped File size", round(bzipsize, 4)," bytes"])
    table2.add_row(["Based64 File size", round(base64fsz, 4), " bytes"])
    table2.sortby = 'Value'
    table2.reversesort = True
    print(table)
    print(table2)
filenum = 2
LetterprobabilityAmount, totallen, power = readfileprobability(filenum, True)
test1, test2, H_f, infomount, filesize,zipsize, rarsize, xzsize, gzipsize, bzipsize, base64fsz = execute(LetterprobabilityAmount, totallen, power, filenum)
preettyoutput(test1, test2, H_f, infomount, filesize,zipsize, rarsize, xzsize, gzipsize, bzipsize, base64fsz)
# print(bin("к"), "к")
# s = input("-----")
# if s != "asd":
#    print("end")
# else:
#    print("sad")