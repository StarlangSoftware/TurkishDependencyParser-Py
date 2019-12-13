from DependencyParser.DependencyRelation import DependencyRelation
from DependencyParser.UniversalDependencyType import UniversalDependencyType


class UniversalDependencyRelation(DependencyRelation):

    __universalDependencyType: UniversalDependencyType

    universalDependencyTypes = ["acl", "advcl", "advmod", "amod", "appos", "aux", "case", "cc", "ccomp", "clf",
                                "compound", "conj", "cop", "csubj", "dep", "det", "discourse", "dislocated", "expl",
                                "fixed", "flat", "goeswith", "iobj", "list", "mark", "nmod", "nsubj", "nummod", "obj",
                                "obl", "orphan", "parataxis", "punct", "reparandum", "root", "vocative", "xcomp"]

    universalDependencyTags = [UniversalDependencyType.ACL, UniversalDependencyType.ADVCL,
                               UniversalDependencyType.ADVMOD, UniversalDependencyType.AMOD,
                               UniversalDependencyType.APPOS,
                               UniversalDependencyType.AUX, UniversalDependencyType.CASE,
                               UniversalDependencyType.CC, UniversalDependencyType.CCOMP, UniversalDependencyType.CLF,
                               UniversalDependencyType.COMPOUND, UniversalDependencyType.CONJ,
                               UniversalDependencyType.COP, UniversalDependencyType.CSUBJ, UniversalDependencyType.DEP,
                               UniversalDependencyType.DET, UniversalDependencyType.DISCOURSE,
                               UniversalDependencyType.DISLOCATED, UniversalDependencyType.EXPL,
                               UniversalDependencyType.FIXED, UniversalDependencyType.FLAT,
                               UniversalDependencyType.GOESWITH, UniversalDependencyType.IOBJ,
                               UniversalDependencyType.LIST, UniversalDependencyType.MARK, UniversalDependencyType.NMOD,
                               UniversalDependencyType.NSUBJ, UniversalDependencyType.NUMMOD,
                               UniversalDependencyType.OBJ, UniversalDependencyType.OBL, UniversalDependencyType.ORPHAN,
                               UniversalDependencyType.PARATAXIS, UniversalDependencyType.PUNCT,
                               UniversalDependencyType.REPARANDUM, UniversalDependencyType.ROOT,
                               UniversalDependencyType.VOCATIVE, UniversalDependencyType.XCOMP]

    """
    The getDependencyTag method takes an dependency tag as string and returns the {@link UniversalDependencyType}
    form of it.

    PARAMETERS
    ----------
    tag : str
        Type of the dependency tag in string form
        
    RETURNS
    -------
    UniversalDependencyType
        Type of the dependency in UniversalDependencyType form
    """
    def getDependencyTag(tag: str) -> UniversalDependencyType:
        for j in range(len(UniversalDependencyRelation.universalDependencyTags)):
            if tag == UniversalDependencyRelation.universalDependencyTypes[j]:
                return UniversalDependencyRelation.universalDependencyTags[j]
        return None

    """
    Overriden Universal Dependency Relation constructor. Gets toWord as input and calls it super class's constructor

    PARAMETERS
    ----------
    toWord : int
        Index of the word in the sentence that dependency relation is related
    """
    def __init__(self, toWord: int, dependencyType: str=None):
        super().__init__(toWord)
        if dependencyType is not None:
            self.__universalDependencyType = UniversalDependencyRelation.getDependencyTag(dependencyType)

    def __str__(self) -> str:
        return self.__universalDependencyType.name
