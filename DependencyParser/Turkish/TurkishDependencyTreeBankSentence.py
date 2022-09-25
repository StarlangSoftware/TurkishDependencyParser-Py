from xml.etree.ElementTree import Element

from Corpus.Sentence import Sentence

from DependencyParser.Turkish.TurkishDependencyTreeBankWord import TurkishDependencyTreeBankWord


class TurkishDependencyTreeBankSentence(Sentence):

    def __init__(self, sentenceNode: Element):
        """
        Given the parsed xml node which contains information about a sentence, the method constructs a
        TurkishDependencyTreeBankSentence from it.

        PARAMETERS
        ----------
        sentenceNode : Element
            Xml parsed node containing information about a sentence.
        """
        super().__init__()
        for word_node in sentenceNode:
            word = TurkishDependencyTreeBankWord(word_node)
            self.words.append(word)

    def maxDependencyLength(self) -> int:
        """
        Calculates the maximum of all word to related word distances, where the distances are calculated in terms of
        index differences.

        RETURNS
        -------
        int
            Maximum of all word to related word distances.
        """
        max_length = 0
        for i in range(len(self.words)):
            word = self.words[i]
            if word.getRelation() is not None and word.getRelation().to() - i > max_length:
                max_length = word.getRelation().to() - i
        return max_length
