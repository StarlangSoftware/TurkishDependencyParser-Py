from __future__ import annotations


class ParserEvaluationScore:

    LAS: float
    UAS: float
    LS: float
    word_count: int

    def __init__(self, LAS: float = 0.0, UAS: float = 0.0, LS: float = 0.0, wordCount: int = 0):
        self.LAS = LAS
        self.UAS = UAS
        self.LS = LS
        self.word_count = wordCount

    def getLS(self) -> float:
        return self.LS

    def getLAS(self) -> float:
        return self.LAS

    def getUAS(self) -> float:
        return self.UAS

    def getWordCount(self) -> int:
        return self.word_count

    def add(self, parserEvaluationScore: ParserEvaluationScore):
        self.LAS = (self.LAS * self.word_count + parserEvaluationScore.LAS * parserEvaluationScore.word_count) / \
                   (self.word_count + parserEvaluationScore.word_count)
        self.UAS = (self.UAS * self.word_count + parserEvaluationScore.UAS * parserEvaluationScore.word_count) / \
                   (self.word_count + parserEvaluationScore.word_count)
        self.LS = (self.LS * self.word_count + parserEvaluationScore.LS * parserEvaluationScore.word_count) / \
                  (self.word_count + parserEvaluationScore.word_count)
        self.word_count += parserEvaluationScore.word_count
