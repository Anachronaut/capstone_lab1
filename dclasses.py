from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: int

def main():
    alice = Student('Alice', 'aa1234aa')
    bob = Student('Bob', 'bb1234bb')

    print (alice.name)
    print(bob.college_id)


    print(alice)
    print(bob)

main()
