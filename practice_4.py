product_info = {
"name": "Smartphone",
"brand": "Apple",
"price": 999.99,
"in_stock": True
}
# Print product information
print("Product information:")
print(f" Name: {product_info['name']}")
print(f" Brand: {product_info['brand']}")
print(f" Price: ${product_info['price']}")
print(f" In Stock: {'Yes' if product_info['in_stock'] else 'No'}")
# Print type of product_info
print(f"Type of product_info: {type(product_info)}")

word = input("Enter a word:  ")

length = len(word)
input_words = word.split(" ")
total_words = len(word.split())
print(f"User input words: {input_words}")
print(f"The length of the word is {length}")
print(f"Total number of words: {total_words}")


dob = input("Enter your date of birth (yyyy-mm-dd): ")
age = 2025 - int(dob[:4])
print(f"You are {age} years old.")
