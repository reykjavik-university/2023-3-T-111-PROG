from os import getcwd
from importlib import import_module
from pathlib import Path


def main():
    remove_at = get_function("remove_at")

    sequence = input()
    index_to_remove = int(input())
    return_val = remove_at(sequence, index_to_remove)

    assert isinstance(return_val, tuple), "Function did not return tuple."
    assert len(return_val) == 2, "Function did not return tuple of size 2."
    assert isinstance(
        return_val[0], str
    ), "First element of returned tuple is not a string."
    assert isinstance(
        return_val[1], str
    ), "Second element of returned tuple is not a string."

    print(return_val)


def get_function(name):
    for module in load_modules():
        if hasattr(module, name):
            return getattr(module, name)

    raise NameError(f"Name '{name}' is not defined.")


def load_modules():
    modules = []
    this_file = Path(__file__)
    for submission_file in this_file.parent.iterdir():
        if submission_file == this_file:
            continue

        if submission_file.suffix == ".py":
            modules.append(import_module(submission_file.stem))

    return modules


if __name__ == "__main__":
    main()
