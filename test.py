def welcome(fx):
    def mfx():
        print("Welcome!")
        fx()
        print("Good Luck..")
    return mfx

@welcome
def hello():
    print(" hey i was welcomed")
hello()  