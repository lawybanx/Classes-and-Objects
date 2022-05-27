class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name: str, age: int, tracks: list, score: float):
        # Raise TypeError
        if not isinstance(name, str):
            raise TypeError("Expected type of name: str")

        elif not isinstance(age, int):
            raise TypeError("Expected type of age: int")

        elif not isinstance(tracks, list):
            raise TypeError("Expected type of tracks: list")

        elif not isinstance(score, float):
            raise TypeError("Expected type of score: float")

        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Expected type of name: str")
        self.name = name
        return name

    def change_age(self, age: int):
        if not isinstance(age, int):
            raise TypeError('Expected type of age: int')
        self.age = age
        return age

    def add_track(self, track: str):
        self.tracks.append(track)
        return self.tracks

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
