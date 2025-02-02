import sys
def original_text(encoded_text):
    encodings = ["KOI8-R", "CP1251", "MACCYRILLIC", "CP866", "ISO-8859-5", "CP855"]

    for i in encodings:
        for j in encodings:
            for k in encodings:
                try:
                    decoded_text = encoded_text.decode(i, errors='ignore').encode(j, errors='ignore').decode(k, errors='ignore')

                    if "Зимбабве" in decoded_text:
                        print(decoded_text)
                        exit()
                except Exception as e:
                    pass  

encoded_text = sys.stdin.buffer.read()
original_text(encoded_text)