def search(products: list, criterion: callable):
    eligible_products = []
    for product in products:
        if criterion(product):
            eligible_products.append(product)
    return eligible_products


def price_under_4_euros(product):
    return product[1] < 4
