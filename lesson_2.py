def sunny():
    print("On a sunny day, sandals are appropriate footwear.")

def rainy():
    print("On a rainy day, galoshes are appropriate footwear.")

def snowy():
    print("On a snowy day, boots are appropriate footwear.")

def input():
    weather = input("What is the weather? (sunny, rainy, snowy) ")
    if weather == "sunny":
        sunny()
    elif weather == "rainy":
        rainy()
    elif weather == "snowy":
        snowy()
    else:
        print("Invalid option.")
        main()



def main(name="John",color="yellow"):
    print(f"{name.title()} the fierce, {color.lower()} eyed warrior")

def blackjack(a,b,c):
    if 1>a or a>12 or 1>b or b>12 or 1>c or c>12:
        print("ERROR")
    else:
        if a+b+c <= 21:
            print(str(a+b+c))
        elif a+b+c > 21 and a==11 or b==11 or c==11:
            print(str(a+b+c-10))
        elif a+b+c > 21 and not a==11 or b==11 or c==11:
            print("BUST")

if __name__ == "__main__":
    blackjack(11,10,3)
