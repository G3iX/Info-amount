def read_bz2_file (file_name_input_num):
    binary_read = ''
    with open("destextes/" + str(file_name_input_num) + ".bz2", "rb") as file:
        for i in file:
            binary_read += str(i)
    return binary_read

binary_read = read_bz2_file(8)
#print(binary_read)

BASE64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
def text_base_64(data):
    result = ""
    # data_encoded = data.encode("utf-8", errors='replace') # encoding='unicode_escape' # hexadecimal codes
    #print(data)
    binary_data = ("".join(format(byte, 'b') for byte in bytes(data, 'ASCII')))
    #print(binary_data)
    chunks = [binary_data[i:i + 24] for i in range(0, len(binary_data), 24)]
    #print(chunks)

    # for chunk in chunks:
    #     if chunk != chunks[len(chunks)-1]: # last chunk
    #         index = int(chunk[0:6], 2)
    #         index2 = int(chunk[6:12], 2)
    #         index3 = int(chunk[12:18], 2)
    #         index4 = int(chunk[18:24], 2)
    #         result += BASE64_CHARS[index]
    #         result += BASE64_CHARS[index2]
    #         result += BASE64_CHARS[index3]
    #         result += BASE64_CHARS[index4]
    #     else:
    #         if len(chunks[len(chunks) - 1]) == 24:
    #             index = int(chunk[0:6], 2)
    #             index2 = int(chunk[6:12], 2)
    #             index3 = int(chunk[12:18], 2)
    #             index4 = int(chunk[18:24], 2)
    #             result += BASE64_CHARS[index]
    #             result += BASE64_CHARS[index2]
    #             result += BASE64_CHARS[index3]
    #             result += BASE64_CHARS[index4]
    #         if len(chunks[len(chunks) - 1]) < 24:
    #             if len(chunks[len(chunks) - 1]) >= 18: # index - index2 - index3
    #                 index = int(chunk[0:6], 2)
    #                 index2 = int(chunk[6:12], 2)
    #                 index3 = int(chunk[12:18], 2)
    #                 result += BASE64_CHARS[index]
    #                 result += BASE64_CHARS[index2]
    #                 result += BASE64_CHARS[index3]
    #                 result += '='
    #             else:
    #                 if len(chunks[len(chunks) - 1]) >= 12: # index - index2
    #                     index = int(chunk[0:6], 2)
    #                     index2 = int(chunk[6:12], 2)
    #                     result += BASE64_CHARS[index]
    #                     result += BASE64_CHARS[index2]
    #                     result += '='
    #                     result += '='
    #                 else:
    #                     try:
    #                         index = int(chunk[0:6], 2)
    #                         result += BASE64_CHARS[index]
    #                     except:
    #                         print("error")
    return result

def encode_py_executer(filenum):
    # filenum = 4
    data = read_bz2_file(filenum)
    base64_text = text_base_64(data)
    # import base64
    # bnotmine = base64.b64encode(bytes(data, 'utf-8'))
    # print(bnotmine) # "Base64 encoded text:",

    f = open("destextes/"+str(filenum)+"_bz2_base64.txt", "w")
    f.writelines(base64_text)
    f.close()


encode_py_executer(8)