from __future__ import annotations

import xml

from Corpus.Corpus import Corpus

from DependencyParser.Turkish.TurkishDependencyTreeBankSentence import TurkishDependencyTreeBankSentence


class TurkishDependencyTreeBankCorpus(Corpus):

    def __init__(self, fileName: str = None):
        """
        Empty constructor for TurkishDependencyTreeBankCorpus. Initializes the sentences and wordList attributes.
        """
        super().__init__()
        if fileName is not None:
            root = xml.etree.ElementTree.parse(fileName).getroot()
            for sentenceNode in root:
                sentence = TurkishDependencyTreeBankSentence(sentenceNode)
                self.sentences.append(sentence)

    def emptyCorpus(self) -> TurkishDependencyTreeBankCorpus:
        """
        Constructor to create an empty copy of this corpus.

        RETURNS
        -------
        TurkishDependencyTreeBankCorpus
            An empty copy of this corpus.
        """
        return TurkishDependencyTreeBankCorpus()
