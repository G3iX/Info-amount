from math import log2
# from collections import Counter


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


def readfileprobability ():
    file = open("destextes/2.txt", "r", encoding="utf8")
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
    return UkrLetterD, totlen

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

test1, totallen = readfileprobability()
print("letter amount:\n",test1)
print("total char len:",totallen)
test2 = Letterprobability(test1, totallen)
print("letter probability\n",test2)
test3 = entropy(test2)
print("H =",round(test3,5))