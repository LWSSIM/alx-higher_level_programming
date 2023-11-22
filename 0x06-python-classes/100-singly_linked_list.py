#!/usr/bin/python3
"""
Module:
    class: Node
        that defines a node of a singly linked list
    class: SinglyLinkedList
        that defines a singly linked list
"""


class Node:
    """
    class: Node

    Note:
        create and manage Nodes of a SLL

    Args:
        arg1 (int): data
        arg2 (Node object): next_node

    Methods:
        __init__: init the class attributes

    Properties:
        data:
        next_node:
    """

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter for data in Node class

        Args:
            None

        Return:
            data: in node object (int)

        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter for data in Node object

        Args:
            param1 (int): value to store in data attr
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Getter for next_node

        Returns:
           Node: The next node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter for next_node attribute in Node object

        Args:
            param1 (Node): the next_node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    class: SinglyLinkedList

    Note:
        defines a singly linked list of type Node

    Args:
        arg1 (type):

    Methods:
        __init__: init the class attributes head
        __str__: used to print content of this class
        sorted_insert: insert new nodes and sort the list
    """

    def __init__(self):
        self.__head = None

    def __str__(self):
        """
        prints the entire list in stdout one node number by line

        Args:
            the list as str
        """
        the_list = ""
        tmp = self.__head
        while tmp is not None:
            the_list += str(tmp.data)
            if tmp.next_node is not None:
                the_list += "\n"
            tmp = tmp.next_node
        return the_list

    def sorted_insert(self, value):
        """
        sorted storing of a new Node

        Args:
            value (int): data to store
        """
        new = Node(value)
        if not self.__head or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while tmp.next_node is not None:
                if value < tmp.next_node.data:
                    break
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
