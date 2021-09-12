from Family import Family


def main():
    father_name = input("Enter father name")
    father_age = input("Enter father age")
    mother_name = input("Enter mother name")
    mother_age = input("Enter mother age")
    num_of_children = int(input("Enter number of children"))
    children = {}
    for i in range(num_of_children):
        child_name = input("Enter Child name")
        child_age = input("Enter Child age")
        children[child_name] = child_age
    last_name = input("Enter Last name")
    father_details = {"name": father_name, "age": father_age}
    mother_details = {"name": mother_name, "age": mother_age}
    parents = {"father": father_details, "mother": mother_details}
    f = Family(parents, children, last_name)
    print(f.get_children())


if __name__ == '__main__':
    main()
