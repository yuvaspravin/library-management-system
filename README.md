# Library Management System

## Project Description

This is a Python-based Library Management System that manages books, magazines, DVDs and library members.

The system allows members to borrow and return items, calculates late fees based on item type, and handles invalid operations using exception handling.

## Project Structure

```text
library_manager/
│
├── main.py
├── models.py
├── README.md
└── output.txt
```

## Technologies Used

- Python 3.12+
- Object-Oriented Programming (OOP)
- Python ABC module

## Features

- Manages Books, Magazines and DVDs.
- Uses inheritance to share common functionality.
- Calculates different late fees for each item type.
- Allows members to borrow and return items.
- Maintains private item availability and borrowed-item lists.
- Handles invalid operations using ValueError.
- Demonstrates abstraction, encapsulation, inheritance and polymorphism.

## Late Fee Structure

Book Rs 2
Magazine Rs 1
DVD Rs 5

## How to Run

1. Open the project folder in the terminal.
2. Run the following command:

```bash
python main.py
```

## OOP Concepts – Reflection

### 1. Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?

LibraryItem is abstract because it provides common properties and methods for all library items, while requiring each child class to implement its own late_fee() method. If DVD does not implement the abstract late_fee() method, Python raises a TypeError when we try to create a DVD object.

### 2. What happens when you read item.\_\_available from outside the class, and why do we use is_available() instead?

When we try to access item.\_\_available from outside the class, Python raises an AttributeError because the attribute uses double underscores and undergoes name mangling. We use is_available() to check the item's availability through a public method without directly accessing its private attribute.

### 3. What is the difference between LibraryItem.total_items and self.title?

LibraryItem.total_items is a class attribute shared by all instances of the LibraryItem subclasses, and it stores the total number of items created. self.title is an instance attribute, meaning each library item object has its own title.

## Conclusion

This project helped me understand Python Object-Oriented Programming concepts, including abstraction, encapsulation, inheritance, polymorphism and exception handling through a practical Library Management System.
