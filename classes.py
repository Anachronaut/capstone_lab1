class Student:
    def __init__(self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa

    def __str__(self):
        return f'Name: {self.name}, id: {self.college_id}, GPA: {self.gpa}'

def main():
    alice = Student('Alice', 'aa1234aa', 4.0)
    bob = Student('Bob', 'bb1234bb', 3.5)
    jim = Student('Jim', 'cc1234cc', 3.0)

    print (alice.name)
    print(bob.college_id)
    print(jim.gpa)

    print(alice)
    print(bob)
    print(jim)

main()
