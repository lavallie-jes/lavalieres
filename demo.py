from operations import *

GENRES = ("Fiction", "Non-Fiction", "Sci-Fi")

# Add books
add_book("111", "The Hobbit", "J.R.R. Tolkien", "Fiction", 3)
add_book("222", "A Brief History of Time", "Stephen Hawking", "Non-Fiction", 2)
add_book("333", "Dune", "Frank Herbert", "Sci-Fi", 4)
add_book("444", "1984", "George Orwell", "Fiction", 5)
add_book("555", "Clean Code", "Robert C. Martin", "Non-Fiction", 1)

# Add members
add_member("M001", "Alice Smith", "alice@example.com")
add_member("M002", "Bob Jones", "bob@example.com")
add_member("M003", "Charlie Brown", "charlie@example.com")

# Operations
print("Search by author 'George':", search_books("George", by="author"))
update_member("M002", email="bob.jones@example.com")
borrow_book("111", "M001")
borrow_book("222", "M001")
borrow_book("333", "M001")
borrow_book("444", "M001")  # Should fail
return_book("222", "M001")
delete_book("555")  # Should succeed
delete_member("M003")  # Should succeed

# Final state
print(f"\nBooks:\n{books}")
print(f"\nMembers:\n{members}")