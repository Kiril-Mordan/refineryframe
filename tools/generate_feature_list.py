import inspect
import os
import sys

def generate_feature_list(module, exceptions=[]):
    feature_list = []

    # Extract class attributes and methods with docstrings
    for name, attr in inspect.getmembers(module):
        if inspect.isclass(attr):
            # For classes, iterate through the class members
            for member_name, member_attr in inspect.getmembers(attr):
                if inspect.isfunction(member_attr) and f"{name}.{member_name}" not in exceptions:
                    description = inspect.getdoc(member_attr) or "No description available."
                    description = description.strip().split("\n\n")[0]  # Trim to the first line
                    feature_list.append({"function": f"{module.__name__}.{name}.{member_name}", "description": description[:1].lower() + description[1:]})
        # elif inspect.isfunction(attr) and f"{module.__name__}.{name}" not in exceptions:
        #     # For functions outside of classes
        #     description = inspect.getdoc(attr) or "No description available."
        #     description = description.strip().split("\n")[0]  # Trim to the first line
        #     feature_list.append({"function": f"{module.__name__}.{name}", "description": description})

    markdown_content = "## Feature List\n\n"

    for feature in feature_list:
        markdown_content += f"- `{feature['function']}` - {feature['description']}\n"

    with open("../docs/feature_list.md", "w") as file:
        file.write(markdown_content)

if __name__ == "__main__":
    sys.path.append(os.path.dirname(sys.path[0]))
    import refineryframe.refiner

    # List of exceptions (class.method) that you want to skip in the feature list
    exceptions_list = [
        "Refiner.__attrs_post_init__",
        "Refiner.__eq__",
        "Refiner.__ge__",
        "Refiner.__gt__",
        "Refiner.__init__",
        "Refiner.__le__",
        "Refiner.__lt__",
        "Refiner.__ne__",
        "Refiner.__repr__",
        "Refiner.initialize_logger",
        "Refiner.shout",
        "refineryframe.refiner.shoutOUT"
    ]

    generate_feature_list(refineryframe.refiner, exceptions=exceptions_list)
