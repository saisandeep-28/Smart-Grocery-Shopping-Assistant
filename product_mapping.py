
# product_mapping.py

from supermarket_map import locations

# Product name : Supermarket section

products = {
    "milk": "Dairy",
    "cheese": "Dairy",
    "butter": "Dairy",

    "bread": "Bakery",
    "cake": "Bakery",
    "biscuits": "Bakery",

    "rice": "Grains",
    "wheat": "Grains",
    "pasta": "Grains",

    "apple": "Fruits",
    "banana": "Fruits",
    "orange": "Fruits",

    "soap": "Personal Care",
    "shampoo": "Personal Care",
    "toothpaste": "Personal Care"
}


# Convert product names into section coordinates

def get_shopping_sections(shopping_list):

    selected_sections = []
    invalid_products = []

    for item in shopping_list:

        item = item.lower().strip()

        if not item:
            continue

        if item not in products:
            invalid_products.append(item)
            continue

        section = products[item]
        position = locations[section]

        if position not in selected_sections:
            selected_sections.append(position)

    if invalid_products:
        print("\nInvalid products:", ", ".join(invalid_products))
        return None

    return selected_sections



# Display available products
def display_products():

    print("\nAvailable Products:")

    for item, section in products.items():
        print(f"{item.title():15} -> {section}")


# Test the product database
if __name__ == "__main__":

    display_products()

    shopping_list = ["Bread", "Apple", "Banana",]
    sections = get_shopping_sections(shopping_list)

    print("\nShopping List:", shopping_list)
    print("Sections to visit:", sections)
