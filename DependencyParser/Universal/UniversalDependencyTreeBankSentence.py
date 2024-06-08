from __future__ import annotations
from Corpus.Sentence import Sentence
from DependencyParser.ParserEvaluationScore import ParserEvaluationScore
from DependencyParser.Universal.UniversalDependencyRelation import UniversalDependencyRelation
from DependencyParser.Universal.UniversalDependencyTreeBankFeatures import UniversalDependencyTreeBankFeatures
from DependencyParser.Universal.UniversalDependencyTreeBankWord import UniversalDependencyTreeBankWord
import re


class UniversalDependencyTreeBankSentence(Sentence):

    comments: list

    def __init__(self, language: str, sentence: str = None):
        """
        Constructor for the UniversalDependencyTreeBankSentence.  Get a line as input and splits the line wrt tab
        character. The number of items should be 10. The items are id, surfaceForm, lemma, upos, xpos, feature list,
        head word index, dependency type, external dependencies and miscellaneous things for one word.
        :param language: Language name. Currently, 'en' and 'tr' languages are supported.
        :param sentence: Sentence string to be processed.
        """
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
                            surface_form = items[1]
                            lemma = items[2]
                            u_pos = UniversalDependencyRelation.getDependencyPosType(items[3])
                            if u_pos is None:
                                print("Line does not contain universal pos ->" + line)
                            x_pos = items[4]
                            features = UniversalDependencyTreeBankFeatures(language, items[5])
                            if items[6] != "_":
                                to = int(items[6])
                                dependency_type = items[7].upper()
                                relation = UniversalDependencyRelation(to, dependency_type)
                            else:
                                relation = None
                            deps = items[8]
                            misc = items[9]
                            word = UniversalDependencyTreeBankWord(int(id), surface_form, lemma, u_pos, x_pos, features,
                                                               relation, deps, misc)
                            self.addWord(word)

    def addComment(self, comment: str):
        """
        Adds a comment string to comments array list.
        :param comment: Comment to be added.
        """
        self.comments.append(comment)

    def __str__(self) -> str:
        """
        Overridden toString method. Concatenates the strings of words to get the string of a sentence.
        :return: Concatenation of the strings of thw strings of words.
        """
        result = ""
        for comment in self.comments:
            result += comment + "\n"
        for word in self.words:
            result += word.__str__() + "\n"
        return result

    def compareParses(self, sentence: UniversalDependencyTreeBankSentence) -> ParserEvaluationScore:
        """
        Compares the sentence with the given sentence and returns a parser evaluation score for this comparison. The result
        is calculated by summing up the parser evaluation scores of word by word dpendency relation comparisons.
        :param sentence: Universal dependency sentence to be compared.
        :return: A parser evaluation score object.
        """
        score = ParserEvaluationScore()
        for i in range(len(self.words)):
            relation1 = self.words[i].getRelation()
            relation2 = sentence.getWord(i).getRelation()
            if relation1 is not None and relation2 is not None:
                score.add(relation1.compareRelations(relation2))
        return score
