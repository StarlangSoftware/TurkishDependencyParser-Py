class DependencyRelation:

    toWord: int

    """
    Constructor for a DependencyRelation. Takes toWord as a parameter and sets the corresponding attribute.

    PARAMETERS
    ----------
    toWord : int
        Index of the word in the sentence that dependency relation is related
    """
    def __init__(self, toWord: int):
        self.toWord = toWord

    """
    Accessor for toWord attribute

    RETURNS
    -------
    int
        toWord attribute value
    """
    def to(self) -> int:
        return self.toWord
