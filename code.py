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

def readfileprobability (num, type):
    file = open("destextes/"+str(num)+"."+ str(type), "r", encoding="utf8")
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
def execute():
    filenum = 2
    filetype = ["txt","zip", "rar", "xz", "gz", "bz2"]
    globfiletype = filetype[0]

    test1, totallen, power = readfileprobability(filenum, globfiletype)
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
    filesize = get_file_size("destextes/"+str(filenum)+"."+globfiletype)
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
    return test1, test2, H_f, infomount, filesize, zipsize, rarsize, xzsize, gzipsize, bzipsize

def preettyoutput(test1, test2, H_f, infomount, filesize, zipsize, rarsize, xzsize, gzipsize, bzipsize):
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["Letter", "Amount", "Probability"]
    for i in test2:
        table.add_row([i, test1[i], test2[i]])
        # print(i,"-",test1[i], "-", test2[i])
    table2 = PrettyTable()
    table2.field_names = ["Variable name","Value", "dT"]
    table2.add_row(["Average entropy",H_f, ''])
    table2.add_row(["---------", 5.01, ' -----'])
    table2.add_row(["Information Amount", (round(infomount, 3))," bytes"])
    table2.add_row(["Actual File size", (filesize) ," bytes"])
    table2.add_row(["Zipped File size", (round(zipsize, 4))," bytes"])
    table2.add_row(["Rared File size", (round(rarsize, 4))," bytes"])
    table2.add_row(["Xzed File size", (round(xzsize, 4))," bytes"])
    table2.add_row(["Gzipped File size", round(gzipsize, 4)," bytes"])
    table2.add_row(["Bzipped File size", round(bzipsize, 4)," bytes"])
    table2.sortby = 'Value'
    table2.reversesort = True
    print(table)
    print(table2)


test1, test2, H_f, infomount, filesize,zipsize, rarsize, xzsize, gzipsize, bzipsize= execute()
preettyoutput(test1, test2, H_f, infomount, filesize,zipsize, rarsize, xzsize, gzipsize, bzipsize)
