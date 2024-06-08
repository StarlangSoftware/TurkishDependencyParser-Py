from __future__ import annotations


class ParserEvaluationScore:

    LAS: float
    UAS: float
    LS: float
    word_count: int

    def __init__(self, LAS: float = 0.0, UAS: float = 0.0, LS: float = 0.0, wordCount: int = 0):
        """
        Another constructor of the parser evaluation score object.
        :param LAS: Label attachment score
        :param UAS: Unlabelled attachment score
        :param LS: Label score
        :param wordCount: Number of words evaluated
        """
        self.LAS = LAS
        self.UAS = UAS
        self.LS = LS
        self.word_count = wordCount

    def getLS(self) -> float:
        """
        Accessor for the LS field
        :return: Label score
        """
        return self.LS

    def getLAS(self) -> float:
        """
        Accessor for the LAS field
        :return: Label attachment score
        """
        return self.LAS

    def getUAS(self) -> float:
        """
        Accessor for the UAS field
        :return: Unlabelled attachment score
        """
        return self.UAS

    def getWordCount(self) -> int:
        """
        Accessor for the word count field
        :return: Number of words evaluated
        """
        return self.word_count

    def add(self, parserEvaluationScore: ParserEvaluationScore):
        """
        Adds a parser evaluation score to the current evaluation score.
        :param parserEvaluationScore: Parser evaluation score to be added.
        """
        self.LAS = (self.LAS * self.word_count + parserEvaluationScore.LAS * parserEvaluationScore.word_count) / \
                   (self.word_count + parserEvaluationScore.word_count)
        self.UAS = (self.UAS * self.word_count + parserEvaluationScore.UAS * parserEvaluationScore.word_count) / \
                   (self.word_count + parserEvaluationScore.word_count)
        self.LS = (self.LS * self.word_count + parserEvaluationScore.LS * parserEvaluationScore.word_count) / \
                  (self.word_count + parserEvaluationScore.word_count)
        self.word_count += parserEvaluationScore.word_count
