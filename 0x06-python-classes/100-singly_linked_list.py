#!/usr/bin/python3
"""A module that defines a singly linked list"""


class Node:
    """A class represents a node in a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialise a new node

        Args:
            data (int): the value to be stored in the node
            next_node (Node): the address to the next node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Return the data of the node"""

        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node with value

        Args:
            value (int): the value to set the data of the node
        """

        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Return the next node"""

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the data of the next node with value

        Args:
            value (Node): a new node to set to the linked list
        """

        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list"""

    def __init__(self):
        """Initialise a new linked list"""

        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node

        Args:
            value (Node): the new node to insert into the linked list
        """

        newNode = Node(value)

        if self.__head is None:
            newNode.next_node = None
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            ptr = self.__head

            while (ptr.next_node is not None and ptr.next_node.data < value):
                ptr = ptr.next_node

            newNode.next_node = ptr.next_node
            ptr.next_node = newNode

    def __str__(self):
        """Print the linked list"""

        values = []
        ptr = self.__head

        while ptr is not None:
            values.append(str(ptr.data))
            ptr = ptr.next_node

        return ('\n'.join(values))
