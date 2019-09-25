# Assume we have a method which takes in fullname and returns first and last names


def split_fullname(fullname):
    firstname = fullname.split()[0]
    lastname = fullname.split()[-1]
    return firstname, lastname  # we can return multiple values separated just by separating them with a comma


first_name = split_fullname('Bruce Wayne')  # Since we return 2 values, we need 2 variables to store them.
print(first_name)

# The thing is, we are not really returning multiple values here. We're just returning a tuple object of two elements
# which is unpacked when we provide two variables to store them. If we give only one variable, it will be stored as
# a tuple object
