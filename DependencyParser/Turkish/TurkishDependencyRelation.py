from DependencyParser.DependencyRelation import DependencyRelation
from DependencyParser.Turkish.TurkishDependencyType import TurkishDependencyType


class TurkishDependencyRelation(DependencyRelation):

    __toIG: int
    __turkishDependencyType: TurkishDependencyType

    turkishDependencyTypes = ["VOCATIVE", "SUBJECT", "DATIVE.ADJUNCT", "OBJECT", "POSSESSOR",
                              "MODIFIER", "S.MODIFIER", "ABLATIVE.ADJUNCT", "DETERMINER", "SENTENCE",
                              "CLASSIFIER", "LOCATIVE.ADJUNCT", "COORDINATION", "QUESTION.PARTICLE", "INTENSIFIER",
                              "INSTRUMENTAL.ADJUNCT", "RELATIVIZER", "NEGATIVE.PARTICLE", "ETOL", "COLLOCATION",
                              "FOCUS.PARTICLE", "EQU.ADJUNCT", "APPOSITION"]

    turkishDependencyTags = [TurkishDependencyType.VOCATIVE, TurkishDependencyType.SUBJECT,
                             TurkishDependencyType.DATIVE_ADJUNCT, TurkishDependencyType.OBJECT,
                             TurkishDependencyType.POSSESSOR,
                             TurkishDependencyType.MODIFIER, TurkishDependencyType.S_MODIFIER,
                             TurkishDependencyType.ABLATIVE_ADJUNCT, TurkishDependencyType.DETERMINER,
                             TurkishDependencyType.SENTENCE,
                             TurkishDependencyType.CLASSIFIER, TurkishDependencyType.LOCATIVE_ADJUNCT,
                             TurkishDependencyType.COORDINATION, TurkishDependencyType.QUESTION_PARTICLE,
                             TurkishDependencyType.INTENSIFIER,
                             TurkishDependencyType.INSTRUMENTAL_ADJUNCT, TurkishDependencyType.RELATIVIZER,
                             TurkishDependencyType.NEGATIVE_PARTICLE, TurkishDependencyType.ETOL,
                             TurkishDependencyType.COLLOCATION,
                             TurkishDependencyType.FOCUS_PARTICLE, TurkishDependencyType.EQU_ADJUNCT,
                             TurkishDependencyType.APPOSITION]

    @staticmethod
    def getDependencyTag(tag: str) -> TurkishDependencyType:
        """
        The getDependencyTag method takes an dependency tag as string and returns the TurkishDependencyType
        form of it.

        PARAMETERS
        ----------
        tag : str
            Type of the dependency tag in string form

        RETURNS
        -------
        TurkishDependencyType
            Type of the dependency in TurkishDependencyType form
        """
        for j in range(len(TurkishDependencyRelation.turkishDependencyTypes)):
            if tag.upper() == TurkishDependencyRelation.turkishDependencyTypes[j]:
                return TurkishDependencyRelation.turkishDependencyTags[j]
        return None

    def __init__(self, toWord: int, toIG: int, dependencyType: str):
        """
        Another constructor for TurkishDependencyRelation. Gets input toWord, toIG, and dependencyType as arguments and
        calls the super class's constructor and sets the IG and dependency type.

        PARAMETERS
        ----------
        toWord : int
            Index of the word in the sentence that dependency relation is related
        toIG : int
            Index of the inflectional group the dependency relation is related
        dependencyType : str
            Type of the dependency relation in string form
        """
        super().__init__(toWord)
        self.__toIG = toIG
        self.__turkishDependencyType = TurkishDependencyRelation.getDependencyTag(dependencyType)

    def toIG(self) -> int:
        """
        Accessor for the toIG attribute

        RETURNS
        -------
        int
            toIG attribute
        """
        return self.__toIG

    def getTurkishDependencyType(self) -> TurkishDependencyType:
        """
        Accessor for the turkishDependencyType attribute

        RETURNS
        -------
        TurkishDependencyType
            turkishDependencyType attribute
        """
        return self.__turkishDependencyType

    def __str__(self) -> str:
        return self.__turkishDependencyType.name
