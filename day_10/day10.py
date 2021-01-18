#Functions with Outputs

def format_name(first_name,last_name):
    """This is an example of docstring - Take a first name
    and last name then format  it to return the title case version
    of the name"""
    if first_name=="" or last_name=="":
        return "You didn't provide valid inputs"
    formatted_first_name=first_name.title()
    formatted_last_name=last_name.title()
    return f"Result: {formatted_first_name} {formatted_last_name}"

output=format_name("jolo","VILLANUEVA")
print(output)
print(format_name(input("What is your first name: "), input("What is your last name: ")))
