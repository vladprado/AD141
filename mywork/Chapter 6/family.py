class Family:

    def __init__(self, parent1, parent2, *kids):
        self._parent1 = parent1
        self._parent2 = parent2
        self._kids = list(kids)

    def add(self, child):
        self._kids.append(child)

    def __str__(self) -> str:
        kids_names = ""
        for kid in self._kids:
            kids_names += " and " + kid._name
        return "Family members: " + self._parent1._name + " and " + \
            self._parent2._name + kids_names

    def __lt__(self, other_family):
        return len(self._kids) < len(other_family._kids)

    def __gt__(self, other_family):
        return len(self._kids) > len(other_family._kids)

    def __eq__(self, other_family):
        return len(self._kids) == len(other_family._kids)
