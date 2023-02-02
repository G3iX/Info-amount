def read_letter_in_file_probability (file_name_input_num):
    with open("destextes/" + str(file_name_input_num) + ".txt", "r", encoding="utf8") as file:
        total_text = ""
        # LetterD = {}
        LetterD = {"А": 0, "Б": 0, "В": 0, "Г": 0, "Ґ": 0, "Д": 0, "Е": 0, "Є": 0, "Ж": 0, "З": 0, "И": 0, "І": 0,
                   "Ї": 0, "Й": 0, "К": 0, "Л": 0, "М": 0, "Н": 0, "О": 0, "П": 0, "Р": 0, "С": 0, "Т": 0, "У": 0,
                   "Ф": 0, "Х": 0, "Ц": 0, "Ч": 0, "Ш": 0, "Щ": 0, "Ь": 0, "Ю": 0, "Я": 0, "а": 0, "б": 0, "в": 0,
                   "г": 0, "ґ": 0, "д": 0, "е": 0, "є": 0, "ж": 0, "з": 0, "и": 0, "і": 0, "ї": 0, "й": 0, "к": 0,
                   "л": 0, "м": 0, "н": 0, "о": 0, "п": 0, "р": 0, "с": 0, "т": 0, "у": 0, "ф": 0, "х": 0, "ц": 0,
                   "ч": 0, "ш": 0, "щ": 0, "ь": 0, "ю": 0, "я": 0}
        totlen = 0
        middle_text = ""
        for line in file:
            line = line.rstrip()
            middle_text += line

        for i in middle_text:
            # print(i)
            if i not in LetterD:
                continue
            else:  ### HERE WE GO!!!!!!!!!!!!!!!!!!!
                total_text += i
                totlen += 1
                try:
                    LetterD[i] += 1
                except:
                    continue  # LetterD.update({i: 1})  # continue
    binary_read = ''
    with open("destextes/" + str(file_name_input_num) + ".txt", "rb") as file:
        for i in file:
            binary_read += str(i)

    alphabetPwr = len(LetterD)
    return total_text, LetterD, totlen, alphabetPwr, binary_read

total_text, LetterD, totlen, alphabetPwr, binary_read = read_letter_in_file_probability(8)
print(total_text)
print(binary_read)