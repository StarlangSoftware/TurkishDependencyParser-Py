from __future__ import annotations

from Corpus.Corpus import Corpus
from DataStructure.CounterHashMap import CounterHashMap
from DependencyParser.ParserEvaluationScore import ParserEvaluationScore
from DependencyParser.Universal.UniversalDependencyTreeBankSentence import UniversalDependencyTreeBankSentence


class UniversalDependencyTreeBankCorpus(Corpus):

    def __init__(self, fileName: str):
        self.sentences = []
        self.paragraphs = []
        self.wordList = CounterHashMap()
        sentence = ""
        file = open(fileName, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                self.addSentence(UniversalDependencyTreeBankSentence(sentence))
                sentence = ""
            else:
                sentence = sentence + line + "\n"

    def compareParses(self, corpus: UniversalDependencyTreeBankCorpus) -> ParserEvaluationScore:
        score = ParserEvaluationScore()
        for i in range(len(self.sentences)):
            score.add(self.sentences[i].compareParses(corpus.getSentence(i)))
        return score
