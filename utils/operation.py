from tabulate import tabulate

# Adding a product
def add_product(file,data):
    sku = input("Enter Product SKU: ")
    name = input("Enter Product Name: ")
    brand = input("Enter Brand: ")
    quantity = int(input("Enter Quantity: "))

    # Check if SKU already exists
    if any(product["Product SKU"] == sku for product in data) :
        print(f"Error: Product with SKU '{sku}' already exists.")
        return
    if quantity<0 :
        print(f"Error: Product qunatity cannot be negative")
        return
        

    new_product = {
        "Product SKU": sku,
        "Product Name": name,
        "Brand": brand,
        "Quantity": quantity
    }
    data.append(new_product)
    file.save_product_data(data)

# Reading all products
def read_products(data):
    table = [[p["Product SKU"], p["Product Name"], p["Brand"], p["Quantity"]] for p in data]
    headers = ["Product SKU", "Product Name", "Brand", "Quantity"]
    print("\nAll Products:")
    print(tabulate(table, headers=headers, tablefmt="grid"))

# Upadate Product with SKU
def update_product(file,data):
    sku = input("Enter Product SKU to update: ")
    for product in data:
        if product["Product SKU"] == sku:
            product["Product Name"] = input("Enter new Product Name: ")
            product["Brand"] = input("Enter new Brand: ")
            product["Quantity"] = int(input("Enter new Quantity: "))
            file.save_product_data(data)
            print("Product updated successfully.")
            return
    print("Product not found.")

#Delete a poduct with SKU
def delete_product(file,data):
    sku = input("Enter Product SKU to delete: ")
    original_length = len(data)
    data[:] = [product for product in data if product["Product SKU"] != sku]
    if len(data) < original_length:
        file.save_product_data(data)
        print("Product deleted successfully.")
    else:
        print("Product not found.")

#Search the product using Product Name or Brand
def search_product(data):
    user_input=input("Enter the Product Name or Brand to search: ")
    res=[]
    res[:]=[product for product in data if product["Product Name"].lower()==user_input.lower() or product["Brand"].lower()==user_input.lower()]
    read_products(res)

# Helper Sort function
def sort_func(products,key,reverse=False):
    return sorted(products, key=lambda p: p[key],reverse=reverse)

# Sort the products with SKU , Product Name and Quantity(ASC/DESC)
def sort_products(data):
    print("\n1. Sort by Product SKU\n2. Sort by Product Name\n3. Sort by Produc Quantity (ASC)\n4. Sort by Produc Quantity (DESC)\n5. Exit")
    try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                res=sort_func(data,"Product SKU")
            elif choice == 2:
                res=sort_func(data,"Product Name")
            elif choice == 3:
                res=sort_func(data,"Quantity")
            elif choice == 4:
                res=sort_func(data,"Quantity",True)
            elif choice == 5:
                return
            else:
                raise ValueError("Invalid choice")
            read_products(res)
            
    except ValueError as e:
            print(f"Invalid Entry: {e}")
    