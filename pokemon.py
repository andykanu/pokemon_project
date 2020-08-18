#declare variables
letters = "abcdefghijklmnopqrstuvwxyz"
#decode caeser cipher with offset 
def decode_message(original_message, offset):
    my_str = ""
    for i in range(len(original_message)):
        if original_message[i] in letters:
            my_char = letters.index(original_message[i]) + offset
            if my_char > len(letters)-1:
                my_str = my_str + letters[my_char % 26]
            else:
                my_str += letters[my_char]
        else: 
            my_str = my_str + original_message[i]
    return my_str
#encode caesar cipher with offset
def encode_message(original_message, offset):
    my_str = ""
    for i in range(len(original_message)):
        if original_message[i] in letters:
            my_char = letters.index(original_message[i]) - offset
            if my_char < 0:
                my_str = my_str + letters[my_char +26]
            else:
                my_str += letters[my_char]
        else: 
            my_str = my_str + original_message[i]
    return my_str
#decode vigniere cipher 
def decode_vigniere(message, keyword):
    #create keyword phrase
    k_phrase = ""
    plaintext = ""
    my_count = 0
    for i in range(len(message)):
        if message[i] in letters:
            k_phrase += keyword[my_count]
            my_count+=1
            if my_count == len(keyword):
                my_count = 0
            my_pos = letters.index(message[i]) - letters.index(k_phrase[i])
            if my_pos <0:
                my_pos +=26
            plaintext +=letters[my_pos]

        else: 
            k_phrase += message[i]
            plaintext+=message[i]
    #translate keyword phrase back:
    return plaintext
#encode vigniere cipher 
def encode_vigniere(plaintext, keyword):
    k_phrase = ""
    message = ""
    my_count = 0
    for i in range(len(plaintext)):
        if plaintext[i] in letters:
            k_phrase += keyword[my_count]
            my_count+=1
            if my_count == len(keyword):
                my_count = 0
            my_pos = letters.index(plaintext[i]) + letters.index(k_phrase[i])
            if my_pos > len(letters) - 1:
                my_pos = my_pos % 26
            message +=letters[my_pos]
        else: 
            k_phrase += plaintext[i]
            message+=plaintext[i]
    #translate keyword phrase back:
    return message

