from Corpus.Corpus import Corpus
from DataStructure.CounterHashMap import CounterHashMap

from DependencyParser.Universal.UniversalDependencyRelation import UniversalDependencyRelation
from DependencyParser.Universal.UniversalDependencyTreeBankFeatures import UniversalDependencyTreeBankFeatures
from DependencyParser.Universal.UniversalDependencyTreeBankSentence import UniversalDependencyTreeBankSentence
import re

from DependencyParser.Universal.UniversalDependencyTreeBankWord import UniversalDependencyTreeBankWord


class UniversalDependencyTreeBankCorpus(Corpus):

    def __init__(self, fileName: str):
        self.sentences = []
        self.paragraphs = []
        self.wordList = CounterHashMap()
        sentence = None
        relation = None
        file = open(fileName, "r")
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if len(line) == 0:
                self.addSentence(sentence)
                sentence = None
            elif line.startswith("#"):
                if sentence is None:
                    sentence = UniversalDependencyTreeBankSentence()
                sentence.addComment(line.strip())
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
                        sentence.addWord(word)
