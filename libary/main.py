from random import choice 
class Idhash:
    def __init__(self,number):
        self.number = number
    def __str__(self):
        return f"H{self.number:03}"
class Idnum:
    def __init__(self,number):
        self.number = number 
    def __str__(self):
        return f"-N{self.number:03}"
class Idtag:
    def __init__(self,number):
        self.number = number 
    def __str__(self):
        return f"-B{self.number:03}"

id_hash = choice([Idhash(i) for i in range(0,1000)])
id_num  = choice([Idnum(i) for i in range(0,1000)])
id_tag = choice([Idtag(i) for i in range(0,1000)])

customer_id = f"{id_hash}{id_num}{id_tag}"
class Customer:
    def __init__(self,name):
        self.name = name 
        self.id = customer_id 
    def get_id(self):
        return f"Customer's id: {self.id}" 
    def get_name(self):
        return f"Customer's name: {self.name}"
    def get_info(self):
        return f"""
Customer's name: {self.name}
Customer's id: {self.id}
""" 


class Book:
    def __init__(self,title,author,year):
        self.title = title 
        self.author = author 
        self.year = year 
    
class Manager:
    def __init__(self):
        self.lib = []


    def update_lib(self,book: Book):
       self.lib.append({
           "title": book.title,
           "author": book.author ,
           "year": book.year ,
       }
           
       )
    
    def show_lib(self):
        print("📚 LIBRARY:")
        for i,b in enumerate(self.lib,start=1):
            print(f"""
{i}
    "Title": {b["title"]}
    "Author": {b["author"]}
    "Year": {b["year"]}

""")

books = [
    Book("Life of Pi", "Yann Martel", 2001),
    Book("1984", "George Orwell", 1949),
    Book("The Alchemist", "Paulo Coelho", 1988),
    Book("To Kill a Mockingbird", "Harper Lee", 1960),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    Book("Pride and Prejudice", "Jane Austen", 1813),
    Book("The Catcher in the Rye", "J.D. Salinger", 1951),
    Book("Brave New World", "Aldous Huxley", 1932),
    Book("The Hobbit", "J.R.R. Tolkien", 1937),
    Book("Fahrenheit 451", "Ray Bradbury", 1953),
    Book("Jane Eyre", "Charlotte Brontë", 1847),
    Book("Animal Farm", "George Orwell", 1945),
    Book("Wuthering Heights", "Emily Brontë", 1847),
    Book("Moby-Dick", "Herman Melville", 1851),
    Book("The Lord of the Rings", "J.R.R. Tolkien", 1954),
    Book("The Kite Runner", "Khaled Hosseini", 2003),
    Book("The Book Thief", "Markus Zusak", 2005),
    Book("Slaughterhouse-Five", "Kurt Vonnegut", 1969),
    Book("Norwegian Wood", "Haruki Murakami", 1987),
    Book("The Shining", "Stephen King", 1977),
    Book("Dracula", "Bram Stoker", 1897),
    Book("Frankenstein", "Mary Shelley", 1818),
    Book("A Tale of Two Cities", "Charles Dickens", 1859),
    Book("The Picture of Dorian Gray", "Oscar Wilde", 1890),
    Book("Crime and Punishment", "Fyodor Dostoevsky", 1866),
    Book("The Little Prince", "Antoine de Saint-Exupéry", 1943),
    Book("The Giver", "Lois Lowry", 1993),
    Book("A Clockwork Orange", "Anthony Burgess", 1962),
    Book("The Old Man and the Sea", "Ernest Hemingway", 1952),
    Book("The Road", "Cormac McCarthy", 2006),
    Book("Memoirs of a Geisha", "Arthur Golden", 1997),
    Book("The Time Traveler's Wife", "Audrey Niffenegger", 2003),
    Book("The Hunger Games", "Suzanne Collins", 2008),
    Book("The Fault in Our Stars", "John Green", 2012),
    Book("Divergent", "Veronica Roth", 2011),
    Book("Gone Girl", "Gillian Flynn", 2012),
    Book("The Maze Runner", "James Dashner", 2009),
    Book("Twilight", "Stephenie Meyer", 2005),
    Book("The Da Vinci Code", "Dan Brown", 2003),
    Book("Angels & Demons", "Dan Brown", 2000),
    Book("The Girl on the Train", "Paula Hawkins", 2015),
    Book("It", "Stephen King", 1986),
    Book("Misery", "Stephen King", 1987),
    Book("Pet Sematary", "Stephen King", 1983),
    Book("The Stand", "Stephen King", 1978),
    Book("Carrie", "Stephen King", 1974),
    Book("The Outsiders", "S.E. Hinton", 1967),
    Book("Speak", "Laurie Halse Anderson", 1999),
    Book("Looking for Alaska", "John Green", 2005),
    Book("Paper Towns", "John Green", 2008),
    Book("Turtles All the Way Down", "John Green", 2017),
    Book("Eleanor & Park", "Rainbow Rowell", 2012),
    Book("Fangirl", "Rainbow Rowell", 2013),
    Book("The Perks of Being a Wallflower", "Stephen Chbosky", 1999),
    Book("Thirteen Reasons Why", "Jay Asher", 2007),
    Book("Red Queen", "Victoria Aveyard", 2015),
    Book("Shadow and Bone", "Leigh Bardugo", 2012),
    Book("Six of Crows", "Leigh Bardugo", 2015),
    Book("Crooked Kingdom", "Leigh Bardugo", 2016),
    Book("Cinder", "Marissa Meyer", 2012),
    Book("Scarlet", "Marissa Meyer", 2013),
    Book("Cress", "Marissa Meyer", 2014),
    Book("Winter", "Marissa Meyer", 2015),
    Book("The Selection", "Kiera Cass", 2012),
    Book("The Elite", "Kiera Cass", 2013),
    Book("The One", "Kiera Cass", 2014),
    Book("Legend", "Marie Lu", 2011),
    Book("Prodigy", "Marie Lu", 2013),
    Book("Champion", "Marie Lu", 2013),
    Book("The Young Elites", "Marie Lu", 2014),
    Book("The Rose Society", "Marie Lu", 2015),
    Book("The Midnight Library", "Matt Haig", 2020),
    Book("Project Hail Mary", "Andy Weir", 2021),
    Book("The Martian", "Andy Weir", 2011),
    Book("Artemis", "Andy Weir", 2017),
    Book("Educated", "Tara Westover", 2018),
    Book("Becoming", "Michelle Obama", 2018),
    Book("Sapiens", "Yuval Noah Harari", 2011),
    Book("Homo Deus", "Yuval Noah Harari", 2015),
    Book("Atomic Habits", "James Clear", 2018),
    Book("The Subtle Art of Not Giving a F*ck", "Mark Manson", 2016),
    Book("Can't Hurt Me", "David Goggins", 2018),
    Book("The 5 AM Club", "Robin Sharma", 2018),
    Book("Deep Work", "Cal Newport", 2016),
    Book("Digital Minimalism", "Cal Newport", 2019),
    Book("Show Your Work!", "Austin Kleon", 2014),
    Book("Steal Like an Artist", "Austin Kleon", 2012),
    Book("Rich Dad Poor Dad", "Robert Kiyosaki", 1997),
    Book("Think and Grow Rich", "Napoleon Hill", 1937),
    Book("The Millionaire Fastlane", "MJ DeMarco", 2011),
    Book("The Lean Startup", "Eric Ries", 2011),
    Book("Rework", "Jason Fried", 2010),
    Book("Zero to One", "Peter Thiel", 2014),
    Book("Hooked", "Nir Eyal", 2014),
    Book("Start With Why", "Simon Sinek", 2009),
    Book("Leaders Eat Last", "Simon Sinek", 2014),
    Book("Drive", "Daniel H. Pink", 2009),
    Book("Grit", "Angela Duckworth", 2016),
    Book("Outliers", "Malcolm Gladwell", 2008),
    Book("Blink", "Malcolm Gladwell", 2005),
    Book("The Tipping Point", "Malcolm Gladwell", 2000)
]

man1 = Manager()
for book in books:
    man1.update_lib(book)


man1.show_lib()