books = {}
members = []
GENRES = ("Fiction", "Non-Fiction", "Sci-Fi")

def add_book(isbn, title, author, genre, total_copies):
    if isbn in books or genre not in GENRES:
        return False
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies
    }
    return True

def add_member(member_id, name, email):
    for member in members:
        if member["member_id"] == member_id:
            return False
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return True

def search_books(query, by="title"):
    query = query.lower()
    results = []
    for book in books.values():
        if query in book[by].lower():
            results.append(book)
    return results

def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return False
    if genre and genre not in GENRES:
        return False
    if title: books[isbn]["title"] = title
    if author: books[isbn]["author"] = author
    if genre: books[isbn]["genre"] = genre
    if total_copies is not None: books[isbn]["total_copies"] = total_copies
    return True

def update_member(member_id, name=None, email=None):
    for member in members:
        if member["member_id"] == member_id:
            if name: member["name"] = name
            if email: member["email"] = email
            return True
    return False

def delete_book(isbn):
    if isbn not in books:
        return False
    for member in members:
        if isbn in member["borrowed_books"]:
            return False
    del books[isbn]
    return True

def delete_member(member_id):
    for member in members:
        if member["member_id"] == member_id:
            if member["borrowed_books"]:
                return False
            members.remove(member)
            return True
    return False

def borrow_book(isbn, member_id):
    if isbn not in books or books[isbn]["total_copies"] <= 0:
        return False
    for member in members:
        if member["member_id"] == member_id:
            if len(member["borrowed_books"]) >= 3:
                return False
            member["borrowed_books"].append(isbn)
            books[isbn]["total_copies"] -= 1
            return True
    return False

def return_book(isbn, member_id):
    if isbn not in books:
        return False
    for member in members:
        if member["member_id"] == member_id and isbn in member["borrowed_books"]:
            member["borrowed_books"].remove(isbn)
            books[isbn]["total_copies"] += 1
            return True
    return False

