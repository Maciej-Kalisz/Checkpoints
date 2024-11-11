from P1 import Act


class LineUp:
    acts = []

    def __init__(self):
        self.acts = []

    def add_act(self, act: Act):
        if len(self.acts) < 30:
            self.acts.append(act)
        else:
            print("The festival is full!")

    def __str__(self):
        sb = ""

        for act in self.acts:
            sb += act.__str__()
            sb += "\n"

        return sb

    def number_of_acts(self):
        return len(self.acts)

    def total_members(self):
        sum = 0

        for act in self.acts:
            sum += act.num_members

        return sum

    def total_kinds(self):
        kinds = set()

        for act in self.acts:
            kinds.add(act.kind)

        return len(kinds)
