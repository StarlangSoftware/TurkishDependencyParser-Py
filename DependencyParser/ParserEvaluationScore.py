from __future__ import annotations

class ParserEvaluationScore:

    LAS: float
    UAS: float
    LS: float
    wordCount: int

    def __init__(self, LAS: float = 0.0, UAS: float = 0.0, LS : float = 0.0, wordCount : int = 0):
        self.LAS = LAS
        self.UAS = UAS
        self.LS = LS
        self.wordCount = wordCount

    def getLS(self) -> float:
        return self.LS

    def getLAS(self) -> float:
        return self.LAS

    def getUAS(self) -> float:
        return self.UAS

    def getWordCount(self) -> int:
        return self.wordCount

    def add(self, parserEvaluationScore: ParserEvaluationScore):
        self.LAS = (self.LAS * self.wordCount + parserEvaluationScore.LAS * parserEvaluationScore.wordCount) / \
                   (self.wordCount + parserEvaluationScore.wordCount)
        self.UAS = (self.UAS * self.wordCount + parserEvaluationScore.UAS * parserEvaluationScore.wordCount) / \
                   (self.wordCount + parserEvaluationScore.wordCount)
        self.LS = (self.LS * self.wordCount + parserEvaluationScore.LS * parserEvaluationScore.wordCount) / \
                  (self.wordCount + parserEvaluationScore.wordCount)
        self.wordCount += parserEvaluationScore.wordCount
