from __future__ import annotations
from Corpus.Sentence import Sentence
from DependencyParser.ParserEvaluationScore import ParserEvaluationScore
from DependencyParser.Universal.UniversalDependencyRelation import UniversalDependencyRelation
from DependencyParser.Universal.UniversalDependencyTreeBankFeatures import UniversalDependencyTreeBankFeatures
from DependencyParser.Universal.UniversalDependencyTreeBankWord import UniversalDependencyTreeBankWord
import re


class UniversalDependencyTreeBankSentence(Sentence):

    comments: list

    def __init__(self, sentence: str = None):
        super().__init__()
        self.comments = []
        if sentence is not None:
            lines = sentence.split("\n")
            for line in lines:
                if len(line) == 0:
                    continue
                if line.startswith("#"):
                    self.addComment(line.strip())
                else:
                    items = line.split("\t")
                    if len(items) != 10:
                        print("Line does not contain 10 items ->" + line)
                    else:
                        id = items[0]
                        if re.fullmatch("\\d+", id):
                            surfaceForm = items[1]
                            lemma = items[2]
                            upos = UniversalDependencyRelation.getDependencyPosType(items[3])
                            if upos is None:
                                print("Line does not contain universal pos ->" + line)
                            xpos = items[4]
                            features = UniversalDependencyTreeBankFeatures(items[5])
                            if items[6] != "_":
                                to = int(items[6])
                                dependencyType = items[7].upper()
                                relation = UniversalDependencyRelation(to, dependencyType)
                            else:
                                relation = None
                            deps = items[8]
                            misc = items[9]
                            word = UniversalDependencyTreeBankWord(int(id), surfaceForm, lemma, upos, xpos, features,
                                                               relation, deps, misc)
                            self.addWord(word)

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
