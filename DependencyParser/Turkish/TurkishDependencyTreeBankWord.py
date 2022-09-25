import re
from xml.etree.ElementTree import Element

from Dictionary.Word import Word
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse

from DependencyParser.Turkish.TurkishDependencyRelation import TurkishDependencyRelation


class TurkishDependencyTreeBankWord(Word):

    __parse: MorphologicalParse
    __original_parses: list
    __relation: TurkishDependencyRelation

    def __init__(self, wordNode: Element):
        """
        Given the parsed xml node which contains information about a word and related attributes including the
        dependencies, the method constructs a {@link TurkishDependencyTreeBankWord} from it.

        PARAMETERS
        -----------
        wordNode : Element
            Xml parsed node containing information about a word.
        """
        to_word = 0
        to_ig = 0
        self.__original_parses = []
        self.name = wordNode.text
        ig = wordNode.attrib["IG"]
        ig = ig[:ig.index("+")] + "+" + ig[ig.index("+") + 1:].upper()
        self.__parse = MorphologicalParse(self.splitIntoInflectionalGroups(ig))
        self.__relation = None
        relation_name = wordNode.attrib["REL"]
        if relation_name != "[,( )]":
            relation_parts = re.compile("[\\[()\\],]").split(relation_name)
            index = 0
            for part in relation_parts:
                if len(part) != 0:
                    index = index + 1
                    if index == 1:
                        to_word = int(part)
                    elif index == 2:
                        to_ig = int(part)
                    elif index == 3:
                        self.__relation = TurkishDependencyRelation(to_word - 1, to_ig - 1, part)
        for i in range(1, 10):
            if ("ORG_ID" + str(i)) in wordNode.attrib:
                ig = wordNode.attrib["ORG_ID" + str(i)]
                ig = ig[:ig.index("+")] + "+" + ig[ig.index("+") + 1:].upper()
                self.__original_parses.append(MorphologicalParse(self.splitIntoInflectionalGroups(ig)))

    def splitIntoInflectionalGroups(self, IG: str) -> list:
        """
        Given the morphological parse of a word, this method splits it into inflectional groups.

        PARAMETERS
        ----------
        IG : str
            Morphological parse of the word in string form.

        RETURNS
        -------
        list
            A list of inflectional groups stored as strings.
        """
        inflectional_groups = []
        IG = IG.replace("(+Punc", "@").replace(")+Punc", "$")
        IGs = re.compile("[\\[()\\]]").split(IG)
        for part in IGs:
            part = part.replace("@", "(+Punc").replace("$", ")+Punc")
            if len(part) != 0:
                inflectional_groups.append(part)
        return inflectional_groups

    def getParse(self) -> MorphologicalParse:
        """
        Accessor for the parse attribute

        RETURNS
        -------
        MorphologicalPArse
            Parse attribute
        """
        return self.__parse

    def getOriginalParse(self, index: int) -> MorphologicalParse:
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
        if index < len(self.__original_parses):
            return self.__original_parses[index]
        else:
            return None

    def size(self) -> int:
        """
        Number of words in this item.

        RETURNS
        -------
        int
            Number of words in this item.
        """
        return len(self.__original_parses)

    def getRelation(self) -> TurkishDependencyRelation:
        """
        Accessor for the relation attribute.

        RETURNS
        -------
        TurkishDependencyRelation
            relation attribute.
        """
        return self.__relation

    def __repr__(self):
        return f"{self.name} {self.__parse} {self.__original_parses} {self.__relation}"
