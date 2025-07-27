from book import Book 
class Library:
    library = []
    def __init__(self):
        pass

    @classmethod
    def show_lib(cls):
        if not cls.library:
            return f"Your Library is currently empty"
        result = ""
        #b là abject đang lặp thì nên dùng 
        for i,b in enumerate(cls.library,start=1):
            result +=  f"""
{i}.{b.title}
Author: {b.author}
Published Year: {b.year}
=========================== 
"""
        return result

    @classmethod
    def add_book(cls,book):
        return cls.library.append(book)
    

    


