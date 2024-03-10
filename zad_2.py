from zad_2.Book import Book
from zad_2.Employee import Employee
from zad_2.Library import Library
from zad_2.Order import Order

l1 = Library("Gliwice", "Wajdy", "44-212", "8-16", "123456789")
l2 = Library("Katowice", "Graniczna", "40-014", "8-18", "123456798")

b1 = Book(l1, "17/04/2001", "Jan", "Nowak", 120)
b2 = Book(l2, "01/05/1994", "Andrzej", "Kowalski", 73)
b3 = Book(l1, "22/01/2023", "Halina", "Klementynowicz", 362)
b4 = Book(l2, "16/12/1987", "Franciszek", "Szpak", 17)
b5 = Book(l1, "02/03/1993", "Cezary", "Krótki", 241)

e1 = Employee("Kamil", "Smolarek", "20/08/2019", "10/02/1968",
              "Gorzów Wielopolski", "Biskupińska", "22-012", "654234765")
e2 = Employee("Stanisław", "Lato", "20/08/2019", "12/03/1985",
              "Poznań", "Biskupińska", "22-012", "686534765")
e3 = Employee("Zofia", "Zima", "20/08/2019", "24/11/1998",
              "Ruda Śląska", "Wolności", "22-012", "654234235")

o1 = Order(e1, "Radosław Żółk", [b1, b2], "09/08/2010")
print(o1)
o2 = Order(e3, "Przemysław Gęś", [b3, b2], "14/03/2013")
print(o2)
