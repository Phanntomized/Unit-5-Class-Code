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

def blackjack():
    card = 0
    eleven = False
    num = 0
    import random
    for i in range(3):
        num = random.randint(1,11)
        if num == 11:
            eleven = True
        card = card + num
    if card <= 21:
        print(str(card))
    elif card > 21 and eleven:
        print(str(card-10))
    elif card > 21 and not eleven:
        print("BUST")
    else:
        print("ERROR")

if __name__ == "__main__":
    blackjack()
