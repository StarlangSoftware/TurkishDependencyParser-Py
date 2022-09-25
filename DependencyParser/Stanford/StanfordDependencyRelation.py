from DependencyParser.DependencyRelation import DependencyRelation
from DependencyParser.Stanford.StanfordDependencyType import StanfordDependencyType


class StanfordDependencyRelation(DependencyRelation):
    __stanford_dependency_type: StanfordDependencyType

    stanford_dependency_types = ["ACOMP", "ADVCL", "ADVMOD", "AGENT", "AMOD", "APPOS", "AUX", "AUXPASS", "CC", "CCOMP",
                                 "CONJ", "COP", "CSUBJ", "CSUBJPASS", "DEP", "DET", "DISCOURSE", "DOBJ", "EXPL",
                                 "GOESWITH", "IOBJ", "MARK", "MWE", "NEG", "NN", "NPADVMOD", "NSUBJ", "NSUBJPASS",
                                 "NUM",
                                 "NUMBER", "PARATAXIS", "PCOMP", "POBJ", "PASS", "POSSESSIVE", "PRECONJ", "PREDET",
                                 "PREP", "PREPC", "PRT", "PUNCT", "QUANTMOD", "RCMOD", "REF", "ROOT", "TMOD", "VMOD",
                                 "XCOMP", "XSUBJ"]

    stanford_dependency_tags = [StanfordDependencyType.ACOMP, StanfordDependencyType.ADVCL,
                                StanfordDependencyType.ADVMOD, StanfordDependencyType.AGENT,
                                StanfordDependencyType.AMOD,
                                StanfordDependencyType.APPOS, StanfordDependencyType.AUX,
                                StanfordDependencyType.AUXPASS, StanfordDependencyType.CC, StanfordDependencyType.CCOMP,
                                StanfordDependencyType.CONJ, StanfordDependencyType.COP,
                                StanfordDependencyType.CSUBJ, StanfordDependencyType.CSUBJPASS,
                                StanfordDependencyType.DEP, StanfordDependencyType.DET,
                                StanfordDependencyType.DISCOURSE,
                                StanfordDependencyType.DOBJ, StanfordDependencyType.EXPL,
                                StanfordDependencyType.GOESWITH,
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

    @staticmethod
    def getDependencyTag(tag: str) -> StanfordDependencyType:
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
        for j in range(len(StanfordDependencyRelation.stanford_dependency_tags)):
            if tag.upper() == StanfordDependencyRelation.stanford_dependency_types[j]:
                return StanfordDependencyRelation.stanford_dependency_tags[j]
        return None

    def __init__(self,
                 toWord: int,
                 dependencyType: str = None):
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
        super().__init__(toWord)
        if dependencyType is not None:
            self.__stanford_dependency_type = StanfordDependencyRelation.getDependencyTag(dependencyType)

    def __str__(self) -> str:
        return self.__stanford_dependency_type.name
