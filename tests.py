from operations import *

GENRES = ("Fiction", "Non-Fiction", "Sci-Fi")

# Setup
add_book("123456", "Python Basics", "John Doe", "Non-Fiction", 5)
add_member("M001", "Alice Smith", "alice@example.com")

# Tests
assert add_book("123456", "Duplicate Book", "Jane Doe", "Fiction", 3) == False
assert update_member("M001", name="Alice Johnson") == True
assert borrow_book("123456", "M001") == True
assert borrow_book("123456", "M001") == True
assert borrow_book("123456", "M001") == True
assert borrow_book("123456", "M001") == False  # Exceeds limit
assert return_book("123456", "M001") == True
assert delete_member("M001") == False  # Still has borrowed books