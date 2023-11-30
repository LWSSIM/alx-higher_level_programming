#!/usr/bin/python3
'''
   fn: prints 1st & last name
'''


def say_my_name(first_name, last_name=''):
    '''
    Prints formated name(s)

    Args:
        first_name: str type exclusively
        second_name: optional arg-> def("")

    Raises:
        type error if input not str
    '''
    for name, op in zip([first_name, last_name], ['first_name', 'last_name']):
        if not isinstance(name, str):
            raise TypeError("{} must be a string".format(op))

    print("My name is {} {}".format(first_name, last_name))
