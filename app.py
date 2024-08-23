from Database_Handler import Database_Handler


# User Input handler function
def user_input_func(product_manager,file):
    while True:
        print("\n1. Add a Product\n2. Read all Products\n3. Update a Product\n4. Delete a Product\n5. Search the Product by Name or Brand\n6. Sort the Products\n7. Total Products\n8. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                product_manager.add_product(file)
            elif choice == 2:
                product_manager.read_products()
            elif choice == 3:
                product_manager.update_product(file)
            elif choice == 4:
                product_manager.delete_product(file)
            elif choice == 5:
                product_manager.search_product()
            elif choice == 6:
                product_manager.sort_products()
            elif choice == 7:
                product_manager.get_total_num_of_products()
            elif choice == 8:
                print("Exiting...")
                break
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print(f"Invalid Entry: {e}")

if __name__ == "__main__":
    db=Database_Handler("inventory.db")

    fields = [
        "Product_SKU TEXT PRIMARY KEY",
        "Product_Name TEXT NOT NULL",
        "Brand TEXT NOT NULL",
        "Quantity INTEGER NOT NULL"
    ]

    db.create_table('products',fields)
    
    product_data = file.load_product_data()
    product_manager=ProductManager(product_data)
    user_input_func(product_manager,db)
