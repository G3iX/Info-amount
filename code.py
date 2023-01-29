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


def readfileprobability (num):
    file = open("destextes/"+str(num)+".txt", "r", encoding="utf8")
    UkrLetterD = {"а": 0,"б": 0,"в": 0,"г": 0,"ґ": 0,"д": 0,"е": 0,"є": 0,"ж": 0,"з": 0,"и": 0,"і": 0,"ї": 0,"й": 0,"к": 0,"л": 0,"м": 0,"н": 0,"о": 0,"п": 0,
                  "р": 0,"с": 0,"т": 0,"у": 0,"ф": 0,"х": 0,"ц": 0,"ч": 0,"ш": 0,"щ": 0,"ь": 0,"ю": 0,"я": 0} # ,".": 0,",": 0,"!": 0,"?": 0,"-": 0 - do we even need it?
    # total alp len 33
    totlen = 0
    for i in file.read():
        #print(i)
        totlen += 1
        try:
            UkrLetterD[i] += 1
        except:
            continue # UkrLetterD.update({i: 1})
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
filenum = 2
test1, totallen, power = readfileprobability(filenum)
print("total char len:",totallen)
print("alphabet power:", power)
print("letter amount:\n",test1)
test2 = Letterprobability(test1, totallen)
print("letter probability:\n", test2)
test3 = entropy(test2)
H_f = round(test3,5)
print("H =",H_f)
infomount = (H_f * totallen)*0.125 # /8
print("Information:",round(infomount, 3), "bytes")
filesize = get_file_size("destextes/"+str(filenum)+".txt")
print("file size:",filesize, "bytes")

def preettyoutput():
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["Letter", "Amount", "Probability"]
    for i in test2:
        table.add_row([i, test1[i], test2[i]])
        # print(i,"-",test1[i], "-", test2[i])
    table2 = PrettyTable()
    table2.field_names = ["Variable name","Value"]
    table2.add_row(["Average entropy",H_f])
    table2.add_row(["Information Amount", str(round(infomount, 5)) + " bytes"])
    table2.add_row(["File size", str(filesize) + " bytes"])
    # table.sortby = 'Probability'
    print(table)
    print(table2)

# preettyoutput()