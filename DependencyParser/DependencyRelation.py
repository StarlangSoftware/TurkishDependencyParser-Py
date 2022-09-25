class DependencyRelation:

    to_word: int

    def __init__(self, toWord: int):
        """
        Constructor for a DependencyRelation. Takes toWord as a parameter and sets the corresponding attribute.

        PARAMETERS
        ----------
        toWord : int
            Index of the word in the sentence that dependency relation is related
        """
        self.to_word = toWord

    def to(self) -> int:
        """
        Accessor for toWord attribute

        RETURNS
        -------
        int
            toWord attribute value
        """
        return self.to_word
