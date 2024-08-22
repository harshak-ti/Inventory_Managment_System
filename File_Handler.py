import json
class File_Handler():
    def __init__(self,file):
        self.file=file
        
    def load_product_data(self):
        try:
            with open(self.file, 'r') as f:
                data = json.load(f)
                print("Product Data Loaded Successfully:")
                return data
        except FileNotFoundError:
            print("Error: The file does not exist.")
            return []
        except json.JSONDecodeError:
            print("Error: The file is not a valid JSON file.")
            return []
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return []

    def save_product_data(self,data):
        try:
            with open(self.file, 'w') as f:
                json.dump(data, f, indent=4)
                print("Product Data Saved Successfully.")
        except Exception as e:
            print(f"An unexpected error occurred while saving data: {e}")