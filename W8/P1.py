from dataclasses import dataclass


@dataclass
class Act:
    name: str
    num_members: int
    kind: str
    stage: str

    def get_name(self):
        return self.name

    def get_num_members(self):
        return self.num_members

    def get_kind(self):
        return self.kind

    def get_stage(self):
        return self.stage

    def set_name(self, name):
        self.name = name

    def set_num_members(self, num_members):
        self.num_members = num_members

    def set_kind(self, kind):
        self.kind = kind

    def set_stage(self, stage):
        self.stage = stage

    def __str__(self):
        return f"{self.name}, {self.num_members} Members, {self.kind}, {self.stage}"


glass = Act("Glass", 3, "Magic", "1")
print(glass)
