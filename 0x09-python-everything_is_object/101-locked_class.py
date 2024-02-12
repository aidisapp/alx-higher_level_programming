#!/usr/bin/python3

class LockedClass:
    """Class that prevents the user from dynamically creating new instance attributes,
    except if the new instance attribute is called first_name.
    """
    def __setattr__(self, name, value):
        """Overrides the default setattr method to restrict attribute assignment.
        
        Args:
            name (str): The name of the attribute being assigned.
            value: The value to be assigned to the attribute.
        
        Raises:
            AttributeError: If the attribute being assigned is not 'first_name'.
        """
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
