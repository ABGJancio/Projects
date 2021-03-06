"""Doing business with Python."""

store_items = {'Milk': [40, 'litr', 1.99],
               'Sugar': [29, 'kg', 2.49],
               'Tee': [12, 'pcs', 4.69]}

sold_items = []
profit = 0


def get_items():
    """Check the stockpile."""
    print('Name\t\tQuantity\tUnit\t\tUnit Price (PLN)')
    print('----\t\t--------\t----\t\t----------')
    for prod, stock in store_items.items():
        print(f'{prod} \t\t {stock[0]} \t\t {stock[1]} \t\t {stock[2]}')
    print(inventory())
    return


def add_item():
    """Add new product to the stock."""
    print('Adding new product ...')
    name = input('Product name: ')
    quantity = int(input('Product quantity: '))
    unit = input('Product unit of measure: ')
    p_price = float(input('Product purchase price: '))
    if not name in store_items:
        store_items[name] = [quantity, unit, p_price]
    print('Successfully added to warehause. Current status:')
    return store_items


def sell_item():
    """Sell product from the stock."""
    print('What would you like to sell?')
    p_sell = input('Product name: ')
    if not p_sell in store_items:
        print('No such a product in warehouse. Try again.')
        p_sell = input('Product name: ')
   #else:
   #    pass
    q_sell = int(input('Quantity to sell: '))
    s_price = float(input('Sell price: '))
    u_sell = store_items.get(p_sell)[1]
    p_price = store_items.get(p_sell)[2]
    store_items.get(p_sell)[0] -= q_sell
    sold_items.append([p_sell, q_sell, u_sell, p_price, s_price])
    print(
        f'Successfully sold {q_sell} {u_sell} of {p_sell}. Current status:')
    return store_items, sold_items


def inventory():
    """."""
    products = len([a for a in store_items])
    stock_value = sum(a*c for a, b, c in store_items.values())
    return f'There are {products} products in the stock.\nTotal value of products in the stock: {stock_value:.2f} (PLN).\n'


def get_income():
    """."""
    revenues = sum([b*e for a, b, c, d, e in sold_items])
    costs = sum([b*d for a, b, c, d, e in sold_items])
    profit = revenues - costs
    return revenues, costs, profit


def show_profit():
    """."""
    print('Business evaluation (PLN):')
    r, c, p = get_income()
    print(f'Income: {r:.2f}')
    print(f'Cost of purchase: {c:.2f}')
    print(f'Operational profit: {p:.2f} \n')
    return


def start():
    """Prompt."""
    choice = input(
        "\nWhat would you like to do?\nChoose: show, add, sell, profit or exit.\n")
    if choice == "exit":
        print("Exiting... Bye!")
        exit(1)
    elif choice == "show":
        get_items()
        start()
    elif choice == "inventory":
        print(inventory())
        start()
    elif choice == "add":
        add_item()
        get_items()
        start()
    elif choice == "sell":
        sell_item()
        get_items()
        start()
    elif choice == "profit":
        show_profit()
        inventory()
        start()
    elif choice == "check":
        print(round(get_income()[2]), 2)
        start()
    else:
        start()


start()
