def show_menu():
    print("\n=== DHBBA MENU (Different Dishes) ===")
    print("1. Classic Burger")
    print("2. Pepperoni Pizza")
    print("3. Veg Fried Rice")
    print("4. Spaghetti Aglio e Olio")
    print("5. Butter Chicken")
    print("6. Caesar Salad")
    print("7. Chocolate Milkshake")


def take_order():
    prices = {
        1: 180,
        2: 320,
        3: 140,
        4: 260,
        5: 290,
        6: 160,
        7: 120,
    }

    selected = []
    while True:
        show_menu()
        choice = input("Select dish number (or type 'done'): ").strip().lower()

        if choice == "done":
            break

        if not choice.isdigit():
            print("Invalid input. Enter a number or 'done'.")
            continue

        dish = int(choice)
        if dish not in prices:
            print("Dish not available. Try again.")
            continue

        selected.append(dish)
        print(f"Added: Dish {dish} | Price = {prices[dish]}")

    if not selected:
        print("\nNo items ordered.")
        return

    total = sum(prices[d] for d in selected)
    print("\n--- ORDER SUMMARY ---")
    for d in selected:
        print(f"Dish {d}: {prices[d]}")
    print(f"Total Bill: {total}")


if __name__ == "__main__":
    take_order()

