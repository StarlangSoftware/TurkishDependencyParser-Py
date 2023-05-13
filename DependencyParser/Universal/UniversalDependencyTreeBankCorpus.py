from __future__ import annotations

from Corpus.Corpus import Corpus
from DataStructure.CounterHashMap import CounterHashMap
from DependencyParser.ParserEvaluationScore import ParserEvaluationScore
from DependencyParser.Universal.UniversalDependencyTreeBankSentence import UniversalDependencyTreeBankSentence


class UniversalDependencyTreeBankCorpus(Corpus):

    language: str

    def constructor1(self, fileName: str):
        self.sentences = []
        self.paragraphs = []
        self.wordList = CounterHashMap()
        if '/' in fileName:
            self.language = fileName[fileName.index('/') + 1:fileName.index('_')]
        else:
            self.language = fileName[0:fileName.index('_')]
        sentence = ""
        file = open(fileName, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                self.addSentence(UniversalDependencyTreeBankSentence(self.language, sentence))
                sentence = ""
            else:
                sentence = sentence + line + "\n"

    def __init__(self, fileName: str = None):
        if fileName is not None:
            self.constructor1(fileName)

    def compareParses(self, corpus: UniversalDependencyTreeBankCorpus) -> ParserEvaluationScore:
        score = ParserEvaluationScore()
        for i in range(len(self.sentences)):
            score.add(self.sentences[i].compareParses(corpus.getSentence(i)))
        return score
