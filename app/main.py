class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(data: list) -> list:
    Person.people.clear()  # очистити перед створенням

    # First pass — create all persons
    for human in data:
        Person(human["name"], human["age"])

    # Second pass — assign relationships
    for human in data:
        person = Person.people[human["name"]]

        if human.get("wife"):
            person.wife = Person.people.get(human["wife"])

        if human.get("husband"):
            person.husband = Person.people.get(human["husband"])

    return list(Person.people.values())
