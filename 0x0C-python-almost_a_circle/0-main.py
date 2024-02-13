#!/usr/bin/python3
""" 0-main """


from models.base import BaseModel

if __name__ == "__main__":

    b1 = BaseModel()
    print(b1.id)

    b2 = BaseModel()
    print(b2.id)

    b3 = BaseModel()
    print(b3.id)

    b4 = BaseModel(12)
    print(b4.id)

    b5 = BaseModel()
    print(b5.id)
