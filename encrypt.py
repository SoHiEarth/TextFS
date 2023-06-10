class keys:
    def A():
        import random
        Code = random.choice(["01","001","99","999"])
        return Code
    def a():
        Code = "11"
        return Code
    def B():
        Code = "02"
        return Code
    def b():
        Code = "12"
        return Code
def Encrypt(call):
    masterCode = ""
    for Letter in call:
        if Letter == A:
            masterCode = masterCode + keys.A()
        if Letter == a:
            masterCode = masterCode + keys.a()
        if Letter == B:
            masterCode = masterCode + keys.B()
        if Letter == b:
            masterCode = masterCode + keys.b()
    return masterCode