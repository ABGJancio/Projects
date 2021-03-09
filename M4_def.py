"""def name(positional_only_parameters, 
            /, 
            positional_or_keyword_parameters,
            *, 
            keyword_only_parameters): ."""

# Tak więc slash (/) rozdziela nam argumenty tylko pozycyjne od standardowych, 
# a gwiazdka (*) rozdziela standardowe od nazwanych.

shopping_items = [
        "jajka",
        "bułka",
        "ser feta",
        "masło",
        "pomidor"
    ]
    
def shopper(items, payment='card', shop='local'):
    shopping_cart = "Koszyk zawiera: "
    for item in items:
        shopping_cart += item + '\n'
    return shopping_cart

basket = shopper(shopping_items)
#print(basket)

def shopping(items, payment='card', shop='local'):
    result = ""
    result = result + "Idę na zakupy do %s.\n" % shop
    result = result + "Kupię następujące rzeczy:\n"
    for item in items:
        result = result + " - %s\n" % item
    result = result + "By zapłacić, używam %s." % payment
    return result


if __name__ == "__main__":
    items_text = input("Podaj proszę produkty rozdzielone przecinkiem: ")
    items = items_text.split(',')
    shopping_result = shopping(items)
    print(shopping_result)

#items = ["cola", "whiskey", "lód"]
#text = shopping(items, 'card', 'small local shop')
#print(text)

