class Father(object):
    father_name = ""
    father_age = None

    def __init__(self, father_name, father_age):
        self.father_name = father_name
        self.father_age = father_age

    def set_father_name(self, name):
        self.father_name = name

    def set_father_age(self, age):
        self.father_age = age

    def get_father_age(self):
        return self.father_age

    def get_father_name(self):
        return self.father_name


# f = Father("mm",1 )
# yage = f.get_father_age()
# f.set_father_age(3)
# f.set_father_name("kk")
# print(yage)
# print(f.get_father_age())

class Mother(object):
    mother_name = ""
    mother_age = None

    def __init__(self, mother_name, mother_age):
        self.mother_name = mother_name
        self.father_age = mother_age

    def set_mother_name(self, name):
        self.mother_name = name

    def set_mother_age(self, age):
        self.mother_age = age

    def get_mother_name(self):
        return self.mother_name

    def get_mother_age(self):
        return self.mother_age


# m = Mother("sara",23)
# print(m.get_mother_age())
# print(m.get_mother_name())
# m.set_mother_age(24)
# m.set_mother_name("sari")
# print(m.get_mother_name())
# print(m.get_mother_age())

class Child(Mother, Father):
    child_name = ""
    child_age = None
    father: Father
    mother: Mother

    def __init__(self, child_name, child_age, father, mother):
        super().__init__(child_name, child_age,father,mother)
        self.child_age = child_name
        self.child_age = child_age
        self.father = father
        self.mother = mother

        # super(self).__init__(father_name, father_age, mother_name, mother_age())

    def set_child_name(self, name):
        self.child_name = name

    def set_child_age(self, age):
        self.child_age = age

    def get_child_name(self):
        return self.child_name

    def get_child_age(self):
        return self.child_age

    def set_father(self, father_name, father_age):
        self.father.father_name = father_name
        self.father.father_age = father_age

    def set_mother(self, mother_name, mother_age):
        self.mother.mother_name = mother_name
        self.mother.mother_age = mother_age

    def set_parents(self, father_details, mother_details):
        self.father.father_name = father_details["name"]
        self.father.father_name = father_details["age"]
        self.mother.mother_name = father_details["name"]
        self.mother.mother_age = father_details["age"]



class Family(Child):
    def __init__(self, parents, children, last_name=''):
        self.parents = dict(parents)
        self.children = list(children.items())
        self.last_name = ""

    def add_child(self, child_name, child_age):
        self.children.append(child_name, child_age)

    def get_children(self):
        return self.children

    def get_child(self, i):
        key = self.children.keys()
        value = self.children.values()
        return key[i - 1] + value[i - 1]

    def get_parents_names(self):
        return self.parents['father']['name'], self.parents['mother']['name']


