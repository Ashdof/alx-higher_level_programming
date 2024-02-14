#!/usr/bin/python3
""" 1-main """
<<<<<<< HEAD
from models.rectangle import Rectangle
=======

import models.rectangle
# from models.rectangle import Rectangle
>>>>>>> 5d0af4e (Added trial files)

if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
