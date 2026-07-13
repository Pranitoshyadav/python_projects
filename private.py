class book:
    def __init__(self, name, writer, pages):
        self.name = name
        self.writer = writer
        self.pages = pages

    def __len__(self):
        return int(self.pages)
    
b = book("Hary Potter", "J. K. Rowling", "387")

print(len(b))