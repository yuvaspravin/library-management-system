from models import LibraryItem, Book, Magazine, DVD, Member

# Creating Library Items

book = Book("Python 101", 1, "A. Rao")
magazine = Magazine("Tech Today", 2, 5)
dvd = DVD("Python Tutorial", 3, 120)

# Creating a Member

alice = Member("Alice", 101)
bob = Member("Bob", 102, max_items=1)

# Borrowing Items

print("\n--- Borrowing Items ---")

try:
    alice.borrow(book) # Alice borrows a book
    print("Alice borrowed:", book.describe())
    bob.borrow(book) 

except ValueError as e:
    print("Could not borrow:", e) 


# Testing Borrowing Limit

print("\n--- Borrowing Limit Test ---")

try:
    bob.borrow(magazine)  # Bob tries to borrow another item
    print("Bob borrowed:", magazine.describe())
    bob.borrow(dvd)  # Bob tries to borrow a third item

except ValueError as e:
    print("Could not borrow:", e)

# Returning Items

print("\n--- Returning Items ---")

try:
    fee = alice.return_item(book, 3) # Alice returns the book 3 days late
    print("Alice returned:", book.describe())
    print("Late fee: Rs.", fee)

except ValueError as e:
    print("Could not return:", e)

# Testing invalid return

print("\n--- Invalid Return Test ---")

try:
    bob.return_item(book,2)  # Bob tries to return a book he didn't borrow

except ValueError as e:
    print("Could not return:", e)

# Displaying Borrowed Items

print("\n--- Borrowed Items ---")

print("Alice's borrowed items:", alice.borrowed_titles())
print("Bob's borrowed items:", bob.borrowed_titles())

# Polymorphism Test

print("\n--- Polymorphism Test ---")

items = [book, magazine, dvd]
for item in items:
    print(item.describe(), "Late fee for 3 days: Rs", item.late_fee(3))

# Encapsulation Test

print("\n--- Encapsulation Test ---")

try:
    print(book.__available)  # Trying to access private attribute directly
    
except AttributeError as e:
    print("Private attribute access error:", e)

print("Book availability:", book.is_available())  # Accessing via public method

# Class attribute test

print("\n--- Class Attribute Test ---")

print("Total items created:", LibraryItem.total_items)



