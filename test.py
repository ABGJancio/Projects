import csv

store_items = {}
sold_items = []


def import_sales_from_csv():
    """Import database for sold items."""
    with open('sold_items.csv', newline='') as csvfile:
        sold_reader = csv.reader(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        global sold_items
        sold_items = list(sold_reader)
#        for row in sold_reader:
#            sold_items.append(row)
    return #sold_items


def import_items_from_csv():
    """Import database for current items in the stock."""
    with open('current_items.csv', newline='') as csvfile:
        items_reader = csv.DictReader(csvfile)
        for row in items_reader:
            store_items[row['name']] = [float(row['quantity']), row['unit'], float(row['p_price'])]
    return


def export_sales_to_csv():
    """Export database for sold items."""
    with open('sold_items.csv', 'w', newline='') as csvfile:
        sold_writer = csv.writer(
            csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for item in sold_items:
            sold_writer.writerow(item)
    return


def export_items_to_csv():
    """Export database for current items in the stock."""
    with open('current_items.csv', mode='w', newline='') as csvfile:
        fieldnames = ['name', 'quantity', 'unit', 'p_price']
        item_writer = csv.DictWriter(csvfile, fieldnames=fieldnames, )
        item_writer.writeheader()
        for item, content in store_items.items():
            item_writer.writerow({'name': item, 'quantity': content[0], 'unit': content[1], 'p_price': content[2]})
    return


def inventory():
    """."""
    products = len([a for a in store_items])
    stock_value = sum(a*c for a, b, c in store_items.values())
    print(f'There are {products} products in the stock.\nTotal value of products in the stock: {stock_value:.2f} (PLN).\n')
    return


def get_income():
    """."""
    revenues = sum([float(b)*float(e) for a, b, c, d, e in sold_items])
    costs = sum([float(b)*float(d) for a, b, c, d, e in sold_items])
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


#import_items_from_csv()
#inventory()

import_sales_from_csv()
show_profit()
print(sold_items)
