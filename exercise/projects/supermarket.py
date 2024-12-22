# The first step will be to accept the name of the product puchased
# by the consumer and the quantitiy fo the purchased product

# The above process has to be done repeatedly until all the products are entered

# Once we have accepted the products and the quantity, we will accept the consumer's supermarket membership.
# Depending on the type of membership, we will give a discount

# We will have three memebrships namely Gold, Silver and Bronze with a discount of 20%,10% and 5%

# Finally we will calculate the total bill amount depending upon the price of the products and print the detailed
#bill to the output screen.

# Accept products: the core and the most basic functionality of our cashier software is to accept
# the product and the quantity of the product purchased by the consumer
# therefore, we gonne use a simple function enterProducts(), which will accept two things from the user
# which is the name of the product and the quantit#y of the product
#We gonna have this all in a While loop

def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input("Press A to add product and Q to quit: ")
        if details == 'A':
            product = input('Enter Product: ')
            quantity = int(input('Enter quantity: '))
            buyingData.update({product: quantity})
        elif details == 'Q':
            enterDetails = False
        else:
            print('Please select a correct option')
    
    return buyingData

    # A simple function getPrice() which will have two parameters, the product, and the quantity
    
    def getPrice(product, quantity):
     priceData = {
        'Biscuit': 3,
        'Chicken': 5,
        'Egg': 1,
        'Fish': 3,
        'Coke': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 3  
    }

    if product not in priceData:
        print(f"Sorry, {product} is not available.")
        return 0

    subtotal = priceData[product] * quantity
    print(f"{product}: ${priceData[product]} x {quantity} = ${subtotal}")
    return subtotal

    