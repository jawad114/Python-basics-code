
def dec1(fun1):
    def exefun1():
        print("Executing Now")
        fun1()
        print("Executed Sucesfully ")
    return exefun1

@dec1
def jawad():
    print("Jawad Shah is the student of uet mardan")


# jawad= dec1(jawad)
jawad()