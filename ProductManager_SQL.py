from tabulate import tabulate

class ProductManager():

    total_num_of_products=0

    def __init__(self,products):
        self.products=products
        ProductManager.total_num_of_products+=len(products)
    
    # return the total number of products
    @classmethod
    def get_total_num_of_products(cls):
        print(f"\nTotal Number of Products: {cls.total_num_of_products}")

    # Adding a product
    def add_product(self,db):
        sku = input("Enter Product SKU: ")
        name = input("Enter Product Name: ")
        brand = input("Enter Brand: ")
        quantity = int(input("Enter Quantity: "))

        # Check if SKU already exists
        if any(product["Product SKU"] == sku for product in self.products) :
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
        self.products.append(new_product)
        db.insert_value("products", (sku,name,brand,quantity))
        ProductManager.total_num_of_products+=1

    # Reading all products
    def read_products(self,db):
        products=db.fetch_all("products")
        table = [[p["Product SKU"], p["Product Name"], p["Brand"], p["Quantity"]] for p in products]
        headers = ["Product SKU", "Product Name", "Brand", "Quantity"]
        print("\nAll Products:")
        print(tabulate(table, headers=headers, tablefmt="grid"))

    # Upadate Product with SKU
    def update_product(self,db):
        sku = input("Enter Product SKU to update: ")
        for product in self.products:
            if product["Product SKU"] == sku:
                name = input("Enter new Product Name: ")
                brand = input("Enter new Brand: ")
                quantity = int(input("Enter new Quantity: "))
                db.update_value("products", sku, "Product Name", name)
                db.update_value("products", sku, "Brand", brand)
                db.update_value("products", sku, "Quantity", quantity)
                print("Product updated successfully.")
                return
        print("Product not found.")

    #Delete a poduct with SKU
    def delete_product(self,db):
        sku = input("Enter Product SKU to delete: ")
        original_length = len(self.products)
        self.products[:] = [product for product in self.products if product["Product SKU"] != sku]
        db.delete_value("products", sku)
        # if len(self.products) < original_length:
        #     file.save_product_data(self.products)
        #     ProductManager.total_num_of_products-=1
        #     print("Product deleted successfully.")
        # else:
        #     print("Product not found.")

    #Search the product using Product Name or Brand
    def search_product(self,db):
        user_input=input("Enter the Product Name or Brand to search: ")
        searched_products = db.search_products("products", , "Apple")
        self.read_products(searched_products)

    # Helper Sort function
    def sort_func(self,key,reverse=False):
        return sorted(self.products, key=lambda p: p[key],reverse=reverse)

    # Sort the products with SKU , Product Name and Quantity(ASC/DESC)
    def sort_products(self):
        print("\n1. Sort by Product SKU\n2. Sort by Product Name\n3. Sort by Produc Quantity (ASC)\n4. Sort by Produc Quantity (DESC)\n5. Exit")
        try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    res=self.sort_func("Product SKU")
                elif choice == 2:
                    res=self.sort_func("Product Name")
                elif choice == 3:
                    res=self.sort_func("Quantity")
                elif choice == 4:
                    res=self.sort_func("Quantity",True)
                elif choice == 5:
                    return
                else:
                    raise ValueError("Invalid choice")
                self.read_products(res)
                
        except ValueError as e:
                print(f"Invalid Entry: {e}")
        