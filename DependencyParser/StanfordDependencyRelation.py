from DependencyParser.DependencyRelation import DependencyRelation
from DependencyParser.StanfordDependencyType import StanfordDependencyType


class StanfordDependencyRelation(DependencyRelation):

    __stanfordDependencyType: StanfordDependencyType

    stanfordDependencyTypes = ["acomp", "advcl", "advmod", "agent", "amod", "appos", "aux", "auxpass", "cc", "ccomp",
                               "conj", "cop", "csubj", "csubjpass", "dep", "det", "discourse", "dobj", "expl",
                               "goeswith", "iobj", "mark", "mwe", "neg", "nn", "npadvmod", "nsubj", "nsubjpass", "num",
                               "number", "parataxis", "pcomp", "pobj", "poss", "possessive", "preconj", "predet",
                               "prep", "prepc", "prt", "punct", "quantmod", "rcmod", "ref", "root", "tmod", "vmod",
                               "xcomp", "xsubj"]

    stanfordDependencyTags = [StanfordDependencyType.ACOMP, StanfordDependencyType.ADVCL,
                              StanfordDependencyType.ADVMOD, StanfordDependencyType.AGENT, StanfordDependencyType.AMOD,
                              StanfordDependencyType.APPOS, StanfordDependencyType.AUX,
                              StanfordDependencyType.AUXPASS, StanfordDependencyType.CC, StanfordDependencyType.CCOMP,
                              StanfordDependencyType.CONJ, StanfordDependencyType.COP,
                              StanfordDependencyType.CSUBJ, StanfordDependencyType.CSUBJPASS,
                              StanfordDependencyType.DEP, StanfordDependencyType.DET, StanfordDependencyType.DISCOURSE,
                              StanfordDependencyType.DOBJ, StanfordDependencyType.EXPL, StanfordDependencyType.GOESWITH,
                              StanfordDependencyType.IOBJ, StanfordDependencyType.MARK,
                              StanfordDependencyType.MWE, StanfordDependencyType.NEG, StanfordDependencyType.NN,
                              StanfordDependencyType.NPADVMOD, StanfordDependencyType.NSUBJ,
                              StanfordDependencyType.NSUBJPASS, StanfordDependencyType.NUM,
                              StanfordDependencyType.NUMBER, StanfordDependencyType.PARATAXIS,
                              StanfordDependencyType.PCOMP,
                              StanfordDependencyType.POBJ, StanfordDependencyType.POSS,
                              StanfordDependencyType.POSSESSIVE, StanfordDependencyType.PRECONJ,
                              StanfordDependencyType.PREDET,
                              StanfordDependencyType.PREP, StanfordDependencyType.PREPC, StanfordDependencyType.PRT,
                              StanfordDependencyType.PUNCT, StanfordDependencyType.QUANTMOD,
                              StanfordDependencyType.RCMOD, StanfordDependencyType.REF, StanfordDependencyType.ROOT,
                              StanfordDependencyType.TMOD, StanfordDependencyType.VMOD,
                              StanfordDependencyType.XCOMP, StanfordDependencyType.XSUBJ]

    """
    The getDependencyTag method takes an dependency tag as string and returns the {@link StanfordDependencyType}
    form of it.

    PARAMETERS
    ----------
    tag : str
        Type of the dependency tag in string form
        
    RETURNS
    -------
    StanfordDependencyType
        Type of the dependency in StanfordDependencyType form
    """
    def getDependencyTag(tag: str) -> StanfordDependencyType:
        for j in range(len(StanfordDependencyRelation.stanfordDependencyTags)):
            if tag == StanfordDependencyRelation.stanfordDependencyTypes[j]:
                return StanfordDependencyRelation.stanfordDependencyTypes[j]
        return None

    """
    Another constructor for StanfordDependencyRelation. Gets input toWord and dependencyType as arguments and
    calls the super class's constructor and sets the dependency type.

    PARAMETERS
    ----------
    toWord : int
        Index of the word in the sentence that dependency relation is related
    dependencyType : str
        Type of the dependency relation in string form
    """
    def __init__(self, toWord: int, dependencyType: str = None):
        super().__init__(toWord)
        if dependencyType is not None:
            self.__stanfordDependencyType = StanfordDependencyRelation.getDependencyTag(dependencyType)

    def __str__(self) -> str:
        return self.__stanfordDependencyType.name
