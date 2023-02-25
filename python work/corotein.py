# import time
def sercher():
    import time
    book = "my name is jawad shah i am form charsadda, and am the student of uetm"
    time.sleep(3)
    while True:
        text = (yield )
        if text in book:
            print("Exist")
        else:
            print("Sorry Doesnt exist")

serch =  sercher()
next(serch)
serch.send(("jawad shah"))

