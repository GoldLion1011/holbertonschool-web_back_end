#!/usr/bin/env python3
"""I'm not sure what I'm looking at, much less doing here"""
from typing import Sequence, Tuple, List, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Holy TaMoly, Batman! What is this?"""
    return [(i, len(i)) for i in lst]
