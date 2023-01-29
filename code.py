
def readfile(): # return symbols amount
    f = open("destextes/1.txt", "r",encoding="utf8")
    UkrLetterD = {"а": 0,"б": 0,"в": 0,"г": 0,"ґ": 0,"д": 0,"е": 0,"є": 0,"ж": 0,"з": 0,"и": 0,"і": 0,"ї": 0,"й": 0,"к": 0,"л": 0,"м": 0,"н": 0,"о": 0,"п": 0,
                  "р": 0,"с": 0,"т": 0,"у": 0,"ф": 0,"х": 0,"ц": 0,"ч": 0,"ш": 0,"щ": 0,"ь": 0,"ю": 0,"я": 0,".": 0,",": 0,"!": 0,"?": 0," ": 0,"-": 0}
    for i in f.read():
        #print(i)
        try:
            UkrLetterD[i] += 1
        except:
            UkrLetterD.update({i: 0})
    return UkrLetterD
    #text = open("1.txt", 'r', encoding="cp1251").read()
    #text
print(readfile())