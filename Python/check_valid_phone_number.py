#format of phone number is three numbers, a hyphen, three numbers, a hyphen, and four numbers.

def IsPhoneNumber(text):
    if len(str(text)) == 12:
        if text[3] == "-":
            if text[:3].isdecimal():
                if text[4:7].isdecimal():
                    if text[7] == "-":
                        if text[8:].isdecimal():
                            return True
                        else: return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

phonenumber = input()
print (IsPhoneNumber(phonenumber))