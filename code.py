from math import log2

def get_file_size(filename):
    size = 0
    with open(filename, "rb") as f:
        while True:
            block = f.read(4096)
            if not block:
                break
            size += len(block)
    return size

def find_entropy_from(inmput_dict):
    sigma_m_i = 0
    for i in inmput_dict: # m = 33+
        try:
            sigma_m_i += inmput_dict[i] * log2(1/inmput_dict[i])
        except:
            continue
    # print("H = ", round(sigma_m_i, 5))
    return sigma_m_i

def probability_of_letter_to_appear(inmput_dict, total_number_of_char_in_text):
    ukr_letter_probability_dict = {}
    for i in inmput_dict:
        temp = round(inmput_dict[i]/total_number_of_char_in_text, 8)
        ukr_letter_probability_dict.update({i: temp})
    return ukr_letter_probability_dict


def zip_size_notes(input_num): # size of file archivated in zip
    from zipfile import ZipFile
    zp = ZipFile("destextes/"+str(input_num)+".zip")
    size = sum([info.file_size for info in zp.filelist])
    # zip_kb = float(size) / 1000  # kB
    zip_bytes = float(size)
    # zip_bits = float(size) * 8 # bits
    with ZipFile('destextes/'+str(input_num)+'.zip') as myzip:
        with myzip.open('1.txt') as myfile:
            for i in myfile:
                print([i])
    return zip_bytes

# def Base64encode(filename): # will do from encode.py

def read_letter_in_file_probability (file_name_input_num, if_ukr_set_boolean_true):
    if if_ukr_set_boolean_true:
        file = open("destextes/"+str(file_name_input_num)+".txt", "r", encoding="utf8")
        ukr_letter_amount_in_text_dict = {"А": 0, "Б": 0, "В": 0, "Г": 0, "Ґ": 0, "Д": 0, "Е": 0, "Є": 0, "Ж": 0, "З": 0, "И": 0, "І": 0,
                      "Ї": 0, "Й": 0, "К": 0, "Л": 0, "М": 0, "Н": 0, "О": 0, "П": 0,
                      "Р": 0, "С": 0, "Т": 0, "У": 0, "Ф": 0, "Х": 0, "Ц": 0, "Ч": 0, "Ш": 0, "Щ": 0, "Ь": 0, "Ю": 0,
                      "Я": 0,"а": 0, "б": 0, "в": 0, "г": 0, "ґ": 0, "д": 0, "е": 0, "є": 0, "ж": 0, "з": 0, "и": 0, "і": 0,
                      "ї": 0, "й": 0, "к": 0, "л": 0, "м": 0, "н": 0, "о": 0, "п": 0,
                      "р": 0, "с": 0, "т": 0, "у": 0, "ф": 0, "х": 0, "ц": 0, "ч": 0, "ш": 0, "щ": 0, "ь": 0, "ю": 0,
                      "я": 0}  # 66
    else:
        file = open("destextes/" + str(file_name_input_num) + "_base64.txt", "r", encoding="utf8")
        ukr_letter_amount_in_text_dict = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, "L": 0,
                         "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0, "W": 0, "X": 0,
                         "Y": 0, "Z": 0,"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0,
                         "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0,
                         "y": 0, "z": 0, "0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0,
                         "+": 0, "/": 0, "=": 0} #  65

    total_chars_in_text_amount_length_in_func = 0
    for i in file.read():
        total_chars_in_text_amount_length_in_func += 1
        try:
            ukr_letter_amount_in_text_dict[i] += 1
        except:
            continue
            # ukr_letter_amount_in_text_dict.update({i: 1}) # continue
    alphabet_power = len(ukr_letter_amount_in_text_dict)
    return ukr_letter_amount_in_text_dict, total_chars_in_text_amount_length_in_func, alphabet_power

def execute(amount_letters_to_appear, total_number_of_char_in_text, power, file_name_input_num, if_ukr_set_boolean_true):
    file_type_list = ["txt","zip", "rar", "xz", "gz", "bz2"]
    if if_ukr_set_boolean_true:
        print("U.t total char len:",total_number_of_char_in_text)
        print("Ukr alphabet power:", power)
        print("Ukr letter amount:\n",amount_letters_to_appear)
        probability_of_letter_to_appear_dict = probability_of_letter_to_appear(amount_letters_to_appear, total_number_of_char_in_text)
        print("Ukr letter probability:\n", probability_of_letter_to_appear_dict)
        entropy_no_round = find_entropy_from(probability_of_letter_to_appear_dict)
        entropy_rounded_h_f = round(entropy_no_round,5)
        print("H =",entropy_rounded_h_f)
        amount_of_information_in_the_text = (entropy_rounded_h_f * total_number_of_char_in_text)*0.125 # /8
        print("Information:",round(amount_of_information_in_the_text, 3), "bytes")
        file_size = get_file_size("destextes/"+str(file_name_input_num)+'.'+file_type_list[0])
        print("file size:",file_size, "bytes")
        zip_size = get_file_size("destextes/"+str(file_name_input_num)+'.'+file_type_list[1])
        print("zipped size:", zip_size, "bytes")
        rar_size = get_file_size("destextes/" + str(file_name_input_num) + '.' + file_type_list[2])
        print("rared size:", rar_size, "bytes")
        xz_size = get_file_size("destextes/" + str(file_name_input_num) + '.' + file_type_list[3])
        print("xzed size:", xz_size, "bytes")
        gzip_size = get_file_size("destextes/" + str(file_name_input_num) + '.' + file_type_list[4])
        print("gzipped size:", gzip_size, "bytes")
        bzip_size = get_file_size("destextes/" + str(file_name_input_num) + '.' + file_type_list[5])
        print("bzipped size:", bzip_size, "bytes")
        base64_file_size = get_file_size("destextes/" + str(file_name_input_num) + '_base64.' + file_type_list[0])
        print("based64 size:", base64_file_size, "bytes")
    else:
        print('---------------------------------------')
        print("total b64 char len:",total_number_of_char_in_text)
        print("b64 alphabet power:", power)
        print("b64 letter amount:\n",amount_letters_to_appear)
        probability_of_letter_to_appear_dict = probability_of_letter_to_appear(amount_letters_to_appear, total_number_of_char_in_text)
        print("b64 letter probability:\n", probability_of_letter_to_appear_dict)
        entropy_no_round = find_entropy_from(probability_of_letter_to_appear_dict)
        entropy_rounded_h_f = round(entropy_no_round,5)
        print("b64 H =",entropy_rounded_h_f)
        amount_of_information_in_the_text = (entropy_rounded_h_f * total_number_of_char_in_text)*0.125 # /8
        print("b64 Information:",round(amount_of_information_in_the_text, 3), "bytes")
        file_size = get_file_size("destextes/"+str(file_name_input_num)+'_base64.'+file_type_list[0])
        print("b64 file size:",file_size, "bytes")
        zip_size = get_file_size("destextes/"+str(file_name_input_num)+'_base64.'+file_type_list[1])
        print("b64 zipped size:", zip_size, "bytes")
        rar_size = get_file_size("destextes/" + str(file_name_input_num) + '_base64.' + file_type_list[2])
        print("b64 rared size:", rar_size, "bytes")
        xz_size = get_file_size("destextes/" + str(file_name_input_num) + '_base64.' + file_type_list[3])
        print("b64 xzed size:", xz_size, "bytes")
        gzip_size = get_file_size("destextes/" + str(file_name_input_num) + '_base64.' + file_type_list[4])
        print("b64 gzipped size:", gzip_size, "bytes")
        bzip_size = get_file_size("destextes/" + str(file_name_input_num) + '_base64.' + file_type_list[5])
        print("b64 bzipped size:", bzip_size, "bytes")
        base64_file_size = get_file_size("destextes/" + str(file_name_input_num) + '_base64.' + file_type_list[0])
        print("b64 based64 size:", base64_file_size, "bytes")
    return probability_of_letter_to_appear_dict, entropy_rounded_h_f, amount_of_information_in_the_text, file_size, zip_size, rar_size, xz_size, gzip_size, bzip_size, base64_file_size

def preetty_output(amount_letters_to_appear, probability_of_letter_to_appear_dict, entropy_rounded_h_f, amount_of_information_in_the_text, file_size, zip_size,
                   rar_size, xz_size, gzip_size, bzip_size, base64fsz, entropy_rounded_base64_h_f,amount_of_information_in_the_base64_text, base64_zip_size, base64_rar_size,
                   base64_xz_size, base64_gzip_size, base64_bzip_size): # 18
    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["Letter", "Amount", "Probability"]
    for i in probability_of_letter_to_appear_dict:
        table.add_row(["'"+i+"'", amount_letters_to_appear[i], probability_of_letter_to_appear_dict[i]])
        # print(i,"-",test1[i], "-", test2[i])
    table2 = PrettyTable()
    table2.field_names = ["Variable name","Value", "dT"]
    table2.add_row(["Average UKR entropy",entropy_rounded_h_f, ''])
    table2.add_row(["Average B64 entropy", entropy_rounded_base64_h_f, ''])
    table2.add_row(["---------", 5.51, ' -----'])
    table2.add_row(["UkrT. Information Amount", (round(amount_of_information_in_the_text, 3))," bytes"])
    table2.add_row(["B64T. Information Amount", (round(amount_of_information_in_the_base64_text, 3)), " bytes"])
    table2.add_row(["Actual File size", (file_size) ," bytes"])
    table2.add_row(["Zipped File size", (round(zip_size, 4))," bytes"])
    table2.add_row(["B64 Zipped File size", (round(base64_zip_size, 4)), " bytes"])
    table2.add_row(["Rared File size", (round(rar_size, 4))," bytes"])
    table2.add_row(["B64 Rared File size", (round(base64_rar_size, 4)), " bytes"])
    table2.add_row(["Xzed File size", (round(xz_size, 4))," bytes"])
    table2.add_row(["B64 Xzed File size", (round(base64_xz_size, 4)), " bytes"])
    table2.add_row(["Gzipped File size", round(gzip_size, 4)," bytes"])
    table2.add_row(["B64 Gzipped File size", round(base64_gzip_size, 4), " bytes"])
    table2.add_row(["Bzipped File size", round(bzip_size, 4)," bytes"])
    table2.add_row(["B64 Bzipped File size", round(base64_bzip_size, 4), " bytes"])
    table2.add_row(["Based64 File size", round(base64fsz, 4), " bytes"])
    # table2.sortby = 'Value'
    # table2.reversesort = True
    print(table)
    print(table2)

file_name_input_num = 2
amount_letters_to_appear, total_number_of_char_in_text, alph_power = read_letter_in_file_probability(file_name_input_num, True)
probability_of_letter_to_appear_dict, entropy_rounded_h_f, amount_of_information_in_the_text, file_size,zip_size, rar_size, xz_size, gzip_size, bzip_size, base64_file_size = execute(amount_letters_to_appear, total_number_of_char_in_text, alph_power, file_name_input_num, True)
# preetty_output(amount_letters_to_appear, probability_of_letter_to_appear_dict, entropy_rounded_h_f, amount_of_information_in_the_text, file_size,zip_size, rar_size, xz_size, gzip_size, bzip_size, base64_file_size)

amount_letters_to_appear_base64, total_number_of_char_in_text_base64, base64_alph_power = read_letter_in_file_probability(file_name_input_num, False)
#print(amount_letters_to_appear_base64)
probability_of_letter_to_appear_base64_dict, entropy_rounded_base64_h_f, amount_of_information_in_the_base64_text, base64_file_size,base64_zip_size, base64_rar_size, base64_xz_size, base64_gzip_size, base64_bzip_size, base64_file_size2 = execute(amount_letters_to_appear_base64, total_number_of_char_in_text_base64, base64_alph_power, file_name_input_num, False)
preetty_output(amount_letters_to_appear, probability_of_letter_to_appear_dict, entropy_rounded_h_f, amount_of_information_in_the_text,
               file_size,zip_size, rar_size, xz_size, gzip_size, bzip_size, base64_file_size,
               entropy_rounded_base64_h_f, amount_of_information_in_the_base64_text,
               base64_zip_size, base64_rar_size, base64_xz_size, base64_gzip_size,base64_bzip_size) # 20