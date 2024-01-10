#!/usr/bin/python3

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import importlib.util

    module_name = "hidden_4"
    module = importlib.import_module(module_name)

    names = dir(module)
    for name in names:
        if name[:2] != "__":
            print(name)
