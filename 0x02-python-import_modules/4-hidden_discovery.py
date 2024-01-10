#!/usr/bin/python3

import importlib.util

if __name__ == "__main__":

    module_name = "hidden_4"
    module_spec = importlib.util.spec_from_file_location(
        module_name, "/mnt/c/Users/USER/Downloads/hidden_4.pyc"
    )
    module = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(module)

    filtered_names = [
        name for name in dir(module) if not name.startswith("__")
    ]

    filtered_names.sort()
    for name in filtered_names:
        print(name)
