from __future__ import annotations
from Corpus.Sentence import Sentence
from DependencyParser.ParserEvaluationScore import ParserEvaluationScore


class UniversalDependencyTreeBankSentence(Sentence):

    comments: list

    def __init__(self):
        super().__init__()
        self.comments = []

    def addComment(self, comment: str):
        self.comments.append(comment)

    def __str__(self) -> str:
        result = ""
        for comment in self.comments:
            result += comment + "\n"
        for word in self.words:
            result += word.__str__() + "\n"
        return result

    def compareParses(self, sentence: UniversalDependencyTreeBankSentence) -> ParserEvaluationScore:
        score = ParserEvaluationScore()
        for i in range(len(self.words)):
            relation1 = self.words[i].getRelation()
            relation2 = sentence.getWord(i).getRelation()
            if relation1 is not None and relation2 is not None:
                score.add(relation1.compareRelations(relation2))
        return score
