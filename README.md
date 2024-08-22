

# Product Inventory Management

This project provides a simple inventory management system for handling product data. It supports CRUD operations and offers options to sort and display products in various formats.



## Documentation

[Documentation](https://linktodocumentation)

## Features

- **Load and Save Product Data**: Read product data from a JSON file and save updates back to the file.
- **CRUD Operations**: Add, update, and delete products.
- **Sorting**: Sort products by SKU, name, or quantity.
- **Search**: Search the product by name or brand.


## Prerequisites

Ensure you have Python 3.x installed on your system. You can download Python from [python.org](https://www.python.org/).

### Setting Up a Virtual Environment

1. **Install `python3-venv` (if not already installed)**:

    ```bash
    sudo apt install python3-venv
    ```

2. **Create a Virtual Environment**:

    ```bash
    python3 -m venv myenv
    ```

3. **Activate the Virtual Environment**:

    ```bash
    source myenv/bin/activate
    ```
## Installation


### Dependencies

You need to install the following Python libraries:

- `tabulate` (for displaying data in a table format)


You can install these libraries using pip:

```bash
pip install tabulate

```

## Usage

### Load Product Data

To load and display product data from Productdata.json, run:

```bash
python3 main.py
```
