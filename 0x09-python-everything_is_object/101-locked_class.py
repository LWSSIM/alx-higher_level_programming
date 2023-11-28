#!/usr/bin/python3
'''Locked Class
'''


class LockedClass:
    '''attribute creation restriction

        Note:
            use the slot method to only allows the
                creation of a first_name attribute
    '''
    __slots__ = ('first_name',)
