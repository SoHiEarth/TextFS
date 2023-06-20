class keys:
    def A():
        import random
        Code = random.choice(["01","001","99","999"])
        return Code
    def a():
        import random
        Code = random.choice(["11","011","89","989"])
        return Code
    def B():
        import random
        Code = random.choice(["02","002","98","998"])
        return Code
    def b():
        import random
        Code = random.choice(["12","012","88","988"])
        return Code
def Encrypt(call):
    masterCode = ""
    for Letter in call:
        if Letter == "A":
            masterCode = masterCode + keys.A()+"|"
        if Letter == "a":
            masterCode = masterCode + keys.a()+"|"
        if Letter == "B":
            masterCode = masterCode + keys.B()+"|"
        if Letter == "b":
            masterCode = masterCode + keys.b()+"|"
    return masterCode
def DeCrypt(Code):
    masterCall = ""
    currentCode = ""
    for l in Code:
        if l == "|":
            if currentCode == "11" or currentCode == "011" or currentCode == "89" or currentCode == "989":
                masterCall += "A"
            elif currentCode == keys.a():
                masterCall += "a"
            elif currentCode == keys.B():
                masterCall += "B"
            elif currentCode == keys.b():
                masterCall += "b"
            currentCode = ""
        else:
            currentCode += l
    return masterCall