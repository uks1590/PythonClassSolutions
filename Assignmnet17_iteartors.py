# Exploring the custom iterators
# Author: Siva Jasthi
# CS4 Python @ SILC
#
#
# Create a Book class
class Book:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return "Name: " + self.name + " color: " + self.color
    
    def __repr__(self):
        return "Name: " + self.name + " color: " + self.color


#Create a Backpack class
# This holds is a collection (list) of students
# we will also implement the internal iterator
class Backpack:
    def __init__(self, Book):
        self.Book = Book

    def ___(self):        return Book.__str()

    def __repr__(self):
        return Book.__str()

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if (self.x <  len(self.Book)):
            current_Book = self.Book[self.x]
            self.x = self.x+1
            return current_Book
        else:
            raise StopIteration


# Create some Books
b1 = Book("Math", "Blue")
b2 = Book("Science", "Black")
b3 = Book("Spanish", "Brown")
b4 = Book("Language", "Light Yellow")
#create a list of students
Books = [b1, b2, b3, b4]

# Create cs_python object
backpack_object = Backpack(Books)

# Simply call the for loop on backpack_object
# Because we implemented our own iterator,
#"for" loop works like a charm
print("--> Calling internal iterator")
for x in backpack_object:
    print(x)


# We can also create an iterator object explictly
iterator_x = iter(backpack_object)
print("--> Calling explit iterator")
print(next(iterator_x))
print(next(iterator_x))
print(next(iterator_x))
print(next(iterator_x))
