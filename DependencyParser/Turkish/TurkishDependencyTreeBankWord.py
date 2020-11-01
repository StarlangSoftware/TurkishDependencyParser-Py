import re
from xml.etree.ElementTree import Element

from Dictionary.Word import Word
from MorphologicalAnalysis.MorphologicalParse import MorphologicalParse

from DependencyParser.Turkish.TurkishDependencyRelation import TurkishDependencyRelation


class TurkishDependencyTreeBankWord(Word):

    __parse: MorphologicalParse
    __originalParses: list
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
        toWord = 0
        toIG = 0
        self.__originalParses = []
        self.name = wordNode.text
        IG = wordNode.attrib["IG"]
        IG = IG[:IG.index("+")] + "+" + IG[IG.index("+") + 1:].upper()
        self.__parse = MorphologicalParse(self.splitIntoInflectionalGroups(IG))
        self.__relation = None
        relationName = wordNode.attrib["REL"]
        if relationName != "[,( )]":
            relationParts = re.compile("[\\[()\\],]").split(relationName)
            index = 0
            for part in relationParts:
                if len(part) != 0:
                    index = index + 1
                    if index == 1:
                        toWord = int(part)
                    elif index == 2:
                        toIG = int(part)
                    elif index == 3:
                        self.__relation = TurkishDependencyRelation(toWord - 1, toIG - 1, part)
        for i in range(1, 10):
            if ("ORG_ID" + str(i)) in wordNode.attrib:
                IG = wordNode.attrib["ORG_ID" + str(i)]
                IG = IG[:IG.index("+")] + "+" + IG[IG.index("+") + 1:].upper()
                self.__originalParses.append(MorphologicalParse(self.splitIntoInflectionalGroups(IG)))

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
        inflectionalGroups = []
        IG = IG.replace("(+Punc", "@").replace(")+Punc", "$")
        IGs = re.compile("[\\[()\\]]").split(IG)
        for part in IGs:
            part = part.replace("@", "(+Punc").replace("$", ")+Punc")
            if len(part) != 0:
                inflectionalGroups.append(part)
        return inflectionalGroups

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
        if index < len(self.__originalParses):
            return self.__originalParses[index]
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
        return len(self.__originalParses)

    def getRelation(self) -> TurkishDependencyRelation:
        """
        Accessor for the relation attribute.

        RETURNS
        -------
        TurkishDependencyRelation
            relation attribute.
        """
        return self.__relation
