def calculate_total_cost(meal,tip):
    total = meal * (1 + (tip/100))
    return round(total,2)

def main():
    try:
        meal = float(input("Enter the meal cost: "))
        tip = int(input("Enter the tip percentage: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for the meal cost and tip percentage.")
        main()
    if tip < 0:
        print("Invalid tip percentage! Using default value of 15%.")
        tip = 15
    total = calculate_total_cost(meal,tip)
    print(f"The total cost of the meal is: ${total:.2f}")

if __name__ == '__main__':
    main()