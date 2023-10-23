def leftpad(s: str, width: int, fillchar: str) -> str:
    """
    Arguments:
               s: the input string
           width: non-negative integer; the max width of the padded string
        fillchar: length-one character
    Examples:
    
    >>> leftpad("Hello world", width=15, char='@')
    "@@@@Hello world"
    
    >>> leftpad("Jumanji", width=2, char='X')
    Jumanji
    """

    assert isinstance(width, int) and width >= 0, width
    assert isinstance(fillchar, str) and len(fillchar) == 1, fillchar
    # CODE goes here