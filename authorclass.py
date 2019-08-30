class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def __str__(self):
        return f'Name: {self.name}, {self.books}'

    def publish(self, title):
        self.books.append(title)


def main():
    tom = Author('Tom')
    tom.publish('The American Novel')
    tina = Author('Tina')
    tina.publish('A Good Book')
    tina.publish('An Even Better Book: A Sequel')
    hank = Author('Hank')

    print(tom)
    print(tina)
    print(hank)

main()
