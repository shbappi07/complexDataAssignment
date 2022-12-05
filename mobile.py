mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here

exchnage_rate = mobile_data.get('exchnage_rate')
# function to convert usd price to bdt
def USD_to_BDT(usd):
    priceInBDT = float(usd)*exchnage_rate
    return priceInBDT

# getting data from the dictionary
mobile_names = mobile_data.get('data')
for mobile_name in mobile_names:
    name =mobile_name.get('name')
    price = mobile_name.get('price')
    if 'USD' in price:
        intprice = price.replace('USD', '')
        bdtPrice = USD_to_BDT(intprice)
    made = mobile_name.get('made')

    mobileDataTemplete = f'{name} is made in {made}. The price of {name} is {price} which is almost equal to {bdtPrice} BDT in Bangladesh.'

    print(mobileDataTemplete)
