class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name = "", age = 0, tracks = [], score = 0.0):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, change):
        print(change)

    def change_age(self, change):
        print(change )

    def add_track(self, change):
        print([change])

    def get_score(self):
        print(self.score)


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)

# # Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
