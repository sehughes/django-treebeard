# -*- coding: utf-8 -*-
"""

    treebeard.exceptions
    --------------------

    Exceptions

    :copyright: 2008 by Gustavo Picon
    :license: Apache License 2.0

"""


class InvalidPosition(Exception):
    """
    Raised when passing an invalid pos value
    """


class InvalidMoveToDescendant(Exception):
    """
    Raised when attemping to move a node to one of it's descendants.
    """


class MissingNodeOrderBy(Exception):
    """
    Raised when an operation needs a missing
    :attr:`~treebeard.MP_Node.node_order_by` attribute
    """


class PathOverflow(Exception):
    """
    Raised when trying to add or move a node to a position where no more nodes
    can be added (see :attr:`~treebeard.MP_Node.path` and
    :attr:`~treebeard.MP_Node.alphabet` for more info)
    """
