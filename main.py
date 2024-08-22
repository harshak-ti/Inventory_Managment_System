from File_Handler import File_Handler
from utils.operation import *

# User Input handler function
def user_input_func(file,data):
    while True:
        print("\n1. Add a Product\n2. Read all Products\n3. Update a Product\n4. Delete a Product\n5. Search the Product by Name or Brand\n6. Sort the Products\n7. Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_product(file,data)
            elif choice == 2:
                read_products(data)
            elif choice == 3:
                update_product(file,data)
            elif choice == 4:
                delete_product(file,data)
            elif choice == 5:
                search_product(data)
            elif choice == 6:
                sort_products(data)
            elif choice == 7:
                print("Exiting...")
                break
            else:
                raise ValueError("Invalid choice")
        except ValueError as e:
            print(f"Invalid Entry: {e}")

if __name__ == "__main__":
    file=File_Handler("Productdata.json")
    product_data = file.load_product_data()
    user_input_func(file,product_data)
