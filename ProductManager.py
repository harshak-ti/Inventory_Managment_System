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
    def add_product(self,file):
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
        file.save_product_data(self.products)
        ProductManager.total_num_of_products+=1

    # Reading all products
    def read_products(self):
        table = [[p["Product SKU"], p["Product Name"], p["Brand"], p["Quantity"]] for p in self.products]
        headers = ["Product SKU", "Product Name", "Brand", "Quantity"]
        print("\nAll Products:")
        print(tabulate(table, headers=headers, tablefmt="grid"))

    # Upadate Product with SKU
    def update_product(self,file):
        sku = input("Enter Product SKU to update: ")
        for product in self.products:
            if product["Product SKU"] == sku:
                product["Product Name"] = input("Enter new Product Name: ")
                product["Brand"] = input("Enter new Brand: ")
                product["Quantity"] = int(input("Enter new Quantity: "))
                file.save_product_data(self.products)
                print("Product updated successfully.")
                return
        print("Product not found.")

    #Delete a poduct with SKU
    def delete_product(self,file):
        sku = input("Enter Product SKU to delete: ")
        original_length = len(self.products)
        self.products[:] = [product for product in self.products if product["Product SKU"] != sku]
        if len(self.products) < original_length:
            file.save_product_data(self.products)
            ProductManager.total_num_of_products-=1
            print("Product deleted successfully.")
        else:
            print("Product not found.")

    #Search the product using Product Name or Brand
    def search_product(self):
        user_input=input("Enter the Product Name or Brand to search: ")
        res=[]
        res[:]=[product for product in self.products if product["Product Name"].lower()==user_input.lower() or product["Brand"].lower()==user_input.lower()]
        self.read_products(res)

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
        