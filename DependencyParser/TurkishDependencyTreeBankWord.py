from Dictionary.Word import Word

from DependencyParser.TurkishDependencyRelation import TurkishDependencyRelation


class TurkishDependencyTreeBankWord(Word):

    __parse: MorphologicalParse
    __originalParses: list
    __relation: TurkishDependencyRelation

    """
    Accessor for the parse attribute
    
    RETURNS
    -------
    MorphologicalPArse
        Parse attribute
    """
    def getParse(self) -> MorphologicalParse:
        return self.__parse

    """
    Accessor for a specific parse.
    
    PARAMETERS
    ----------
    index : int
        Index of the word.
        
    RETURNS
    -------
    MorphologicalParse
        Parse of the index'th word
    """
    def getOriginalParse(self, index: int) -> MorphologicalParse:
        if index < len(self.__originalParses):
            return self.__originalParses[index]
        else:
            return None

    """
    Number of words in this item.

    RETURNS
    -------
    int
        Number of words in this item.
    """

    def size(self) -> int:
        return len(self.__originalParses)

    """
    Accessor for the relation attribute.

    RETURNS
    -------
    TurkishDependencyRelation
        relation attribute.
    """
    def getRelation(self) -> TurkishDependencyRelation:
        return self.__relation
