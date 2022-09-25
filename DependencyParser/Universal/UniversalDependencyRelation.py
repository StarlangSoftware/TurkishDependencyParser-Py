from __future__ import annotations

from DependencyParser.DependencyRelation import DependencyRelation
from DependencyParser.ParserEvaluationScore import ParserEvaluationScore
from DependencyParser.Universal.UniversalDependencyPosType import UniversalDependencyPosType
from DependencyParser.Universal.UniversalDependencyType import UniversalDependencyType


class UniversalDependencyRelation(DependencyRelation):
    __universal_dependency_type: UniversalDependencyType

    universal_dependency_types = ["ACL", "ADVCL",
                                  "ADVMOD", "AMOD",
                                  "APPOS",
                                  "AUX", "AUXPASS",
                                  "CASE", "CC", "CCOMP",
                                  "CLF", "COMPOUND",
                                  "CONJ", "COP", "CSUBJ",
                                  "DEP", "DET",
                                  "DISCOURSE", "DISLOCATED",
                                  "EXPL",
                                  "FIXED", "FLAT",
                                  "FOREIGN",
                                  "GOESWITH",
                                  "IOBJ",
                                  "LIST",
                                  "MARK",
                                  "NMOD", "NSUBJ",
                                  "NUMMOD",
                                  "OBJ", "OBL", "ORPHAN",
                                  "PARATAXIS", "PUNCT",
                                  "REPARANDUM", "ROOT",
                                  "VOCATIVE",
                                  "XCOMP", "ACL:RELCL",
                                  "AUX:PASS", "CC:PRECONJ",
                                  "COMPOUND:PRT", "DET:PREDET",
                                  "FLAT:FOREIGN", "NSUBJ:PASS",
                                  "CSUBJ:PASS", "NMOD:NPMOD",
                                  "NMOD:POSS", "NMOD:TMOD",
                                  "ADVMOD:EMPH", "AUX:Q",
                                  "COMPOUND:LVC", "COMPOUND:REDUP",
                                  "CSUBJ:COP", "NMOD:COMP",
                                  "NMOD:PART", "NSUBJ:COP",
                                  "OBL:AGENT", "OBL:TMOD",
                                  "OBL:NPMOD"]

    universal_dependency_tags = [UniversalDependencyType.ACL, UniversalDependencyType.ADVCL,
                                 UniversalDependencyType.ADVMOD, UniversalDependencyType.AMOD,
                                 UniversalDependencyType.APPOS,
                                 UniversalDependencyType.AUX, UniversalDependencyType.AUXPASS,
                                 UniversalDependencyType.CASE, UniversalDependencyType.CC,
                                 UniversalDependencyType.CCOMP,
                                 UniversalDependencyType.CLF, UniversalDependencyType.COMPOUND,
                                 UniversalDependencyType.CONJ, UniversalDependencyType.COP,
                                 UniversalDependencyType.CSUBJ,
                                 UniversalDependencyType.DEP, UniversalDependencyType.DET,
                                 UniversalDependencyType.DISCOURSE, UniversalDependencyType.DISLOCATED,
                                 UniversalDependencyType.EXPL,
                                 UniversalDependencyType.FIXED, UniversalDependencyType.FLAT,
                                 UniversalDependencyType.FOREIGN,
                                 UniversalDependencyType.GOESWITH,
                                 UniversalDependencyType.IOBJ,
                                 UniversalDependencyType.LIST,
                                 UniversalDependencyType.MARK,
                                 UniversalDependencyType.NMOD, UniversalDependencyType.NSUBJ,
                                 UniversalDependencyType.NUMMOD,
                                 UniversalDependencyType.OBJ, UniversalDependencyType.OBL,
                                 UniversalDependencyType.ORPHAN,
                                 UniversalDependencyType.PARATAXIS, UniversalDependencyType.PUNCT,
                                 UniversalDependencyType.REPARANDUM, UniversalDependencyType.ROOT,
                                 UniversalDependencyType.VOCATIVE,
                                 UniversalDependencyType.XCOMP, UniversalDependencyType.ACL_RELCL,
                                 UniversalDependencyType.AUX_PASS, UniversalDependencyType.CC_PRECONJ,
                                 UniversalDependencyType.COMPOUND_PRT,
                                 UniversalDependencyType.DET_PREDET, UniversalDependencyType.FLAT_FOREIGN,
                                 UniversalDependencyType.NSUBJ_PASS, UniversalDependencyType.CSUBJ_PASS,
                                 UniversalDependencyType.NMOD_NPMOD, UniversalDependencyType.NMOD_POSS,
                                 UniversalDependencyType.NMOD_TMOD, UniversalDependencyType.ADVMOD_EMPH,
                                 UniversalDependencyType.AUX_Q, UniversalDependencyType.COMPOUND_LVC,
                                 UniversalDependencyType.COMPOUND_REDUP, UniversalDependencyType.CSUBJ_COP,
                                 UniversalDependencyType.NMOD_COMP, UniversalDependencyType.NMOD_PART,
                                 UniversalDependencyType.NSUBJ_COP, UniversalDependencyType.OBL_AGENT,
                                 UniversalDependencyType.OBL_TMOD, UniversalDependencyType.OBL_NPMOD]

    universal_dependency_pos_types = ["ADJ", "ADV", "INTJ", "NOUN", "PROPN", "VERB", "ADP", "AUX", "CCONJ",
                                      "DET", "NUM", "PART", "PRON", "SCONJ", "PUNCT", "SYM", "X"]

    universal_dependency_pos_tags = [UniversalDependencyPosType.ADJ, UniversalDependencyPosType.ADV,
                                     UniversalDependencyPosType.INTJ, UniversalDependencyPosType.NOUN,
                                     UniversalDependencyPosType.PROPN,
                                     UniversalDependencyPosType.VERB, UniversalDependencyPosType.ADP,
                                     UniversalDependencyPosType.AUX, UniversalDependencyPosType.CCONJ,
                                     UniversalDependencyPosType.DET, UniversalDependencyPosType.NUM,
                                     UniversalDependencyPosType.PART,
                                     UniversalDependencyPosType.PRON, UniversalDependencyPosType.SCONJ,
                                     UniversalDependencyPosType.PUNCT, UniversalDependencyPosType.SYM,
                                     UniversalDependencyPosType.X]

    @staticmethod
    def getDependencyTag(tag: str) -> UniversalDependencyType:
        """
        The getDependencyTag method takes an dependency tag as string and returns the UniversalDependencyType
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
        for j in range(len(UniversalDependencyRelation.universal_dependency_tags)):
            if tag.upper() == UniversalDependencyRelation.universal_dependency_types[j]:
                return UniversalDependencyRelation.universal_dependency_tags[j]
        return None

    @staticmethod
    def getDependencyPosType(tag: str) -> UniversalDependencyPosType:
        for j in range(len(UniversalDependencyRelation.universal_dependency_pos_types)):
            if tag.upper() == UniversalDependencyRelation.universal_dependency_pos_types[j]:
                return UniversalDependencyRelation.universal_dependency_pos_tags[j]
        return None

    def __init__(self,
                 toWord: int,
                 dependencyType: str = None):
        """
        Overriden Universal Dependency Relation constructor. Gets toWord as input and calls it super class's constructor

        PARAMETERS
        ----------
        toWord : int
            Index of the word in the sentence that dependency relation is related
        """
        super().__init__(toWord)
        if dependencyType is not None:
            self.__universal_dependency_type = UniversalDependencyRelation.getDependencyTag(dependencyType)

    def compareRelations(self, relation: UniversalDependencyRelation) -> ParserEvaluationScore:
        LS = 0.0
        LAS = 0.0
        UAS = 0.0
        if self.__str__() == relation.__str__():
            LS = 1.0
            if self.to_word == relation.to():
                LAS = 1.0
        if self.to_word == relation.to():
            UAS = 1.0
        return ParserEvaluationScore(LAS, UAS, LS, 1)

    def __str__(self) -> str:
        return self.__universal_dependency_type.name
