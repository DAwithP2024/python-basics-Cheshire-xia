# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    pass


def display_products(products_list):
    pass


def display_categories():
    pass


def add_to_cart(cart, product, quantity):
    pass

def display_cart(cart):
    pass


def generate_receipt(name, email, cart, total_cost, address):
    pass


def validate_name(name):
    pass

def validate_email(email):
    pass


def main():
    pass
    

""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main()

# 假设的products字典，实际应从其他地方获取  
products = {  
    "IT products": [  
        {"name": "Laptop", "price": 999.99},  
        {"name": "Mouse", "price": 29.99},  
    ],  
    "Electronics": [  
        {"name": "Smartphone", "price": 699.99},  
        {"name": "Headphones", "price": 149.99},  
    ],  
    # 可以根据需要添加更多产品和类别  
}  
  
# 辅助函数实现  
  
def validate_name(name):  
    # 实现名称验证逻辑  
    parts = name.split()  
    if len(parts) == 2 and all(char.isalpha() for char in name):  
        return True  
    return False  
  
def validate_email(email):  
    # 实现邮箱验证逻辑  
    return "@" in email  
  
def display_categories():  
    # 显示产品类别  
    for index, category in enumerate(products.keys(), start=1):  
        print(f"{index}. {category}")  
  
def display_products(products_list):  
    # 显示产品列表  
    for index, product in enumerate(products_list, start=1):  
        print(f"{index}. {product['name']} - ${product['price']:.2f}")  
  
def display_sorted_products(products_list, sort_order):  
    # 根据价格排序产品  
    if sort_order == 1:  # 升序  
        sorted_products = sorted(products_list, key=lambda x: x['price'])  
    else:  # 默认为降序  
        sorted_products = sorted(products_list, key=lambda x: x['price'], reverse=True)  
    display_products(sorted_products)  
    return sorted_products  
  
def add_to_cart(cart, product, quantity):  
    # 将产品添加到购物车  
    cart.append((product, quantity))  
  
def calculate_total_cost(cart):  
    # 计算购物车中的总费用  
    total_cost = sum(product['price'] * quantity for product, quantity in cart)  
    return total_cost  
  
def generate_receipt(name, email, cart, total_cost, address):  
    # 生成收据  
    print(f"Name: {name}")  
    print(f"Email: {email}")  
    for product, quantity in cart:  
        print(f"{product['name']} x {quantity} - ${product['price']:.2f}")  
    print(f"Total Cost: ${total_cost:.2f}")  
    print(f"Delivery Address: {address}")  
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")  
  
def main():  
    # 主函数实现  
    name = input("Enter your name: ")  
    while not validate_name(name):  
        print("Invalid name. Please enter your first and last name with only alphabets.")  
        name = input("Enter your name: ")  
  
    email = input("Enter your email address: ")  
    while not validate_email(email):  
        print("Invalid email. Please enter a valid email address.")  
        email = input("Enter your email address: ")  
  
    display_categories()  
  
if __name__ == "__main__":  
    main()