class book:
        def __init__(self, title, author, publications, year, price):
                        self.title = title
                        self.author = author
                        self.publications = publications
                        self.year = year
                        self.price = price

n = int(input("Enter the number of books: "))
l = []
count = 0

for i in range(n):
    title = input("Enter title: ")
    author = input("Enter author: ")
    publications = input("Enter publication: ")
    year = int(input("Enter year: "))
    price = int(input("Enter price: "))
    obj = book(title, author, publications, year, price)
    l.append(obj)

for i in l:
    if i.price < 500:
        count += 1

print("Number of books with price less than 500:", count)
