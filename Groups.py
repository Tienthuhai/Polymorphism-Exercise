class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __getitem__(self, index):
        return self.people[index]

    def __iter__(self):
        return iter(self.people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(repr(person) for person in self.people)}"

    def __eq__(self, other):
        if isinstance(other, Group):
            return self.name == other.name and self.people == other.people
        return False

    def __add__(self, other):
        if isinstance(other, Group):
            return Group(name=f"{self.name} & {other.name}", people=self.people + other.people)
        return NotImplemented


# Test code
p1 = Person("John", "Doe")
p2 = Person("Jane", "Doe")
p3 = Person("Jim", "Beam")

group1 = Group("Family", [p1, p2])
group2 = Group("Friends", [p3])

# Displaying a group
print(group1)  # Should print: Group Family with members John Doe, Jane Doe

# Accessing a member by index
print(group1[1])  # Should print: Jane Doe

# Iterating over the group members
for person in group1:
    print(person)

# Checking the length of the group
print(len(group1))  # Should print: 2

# Combining two groups
combined_group = group1 + group2
print(combined_group)  # Should print: Group Family & Friends with members John Doe, Jane Doe, Jim Beam

# Checking if two groups are equal
print(group1 == group2)  # Should print: False
