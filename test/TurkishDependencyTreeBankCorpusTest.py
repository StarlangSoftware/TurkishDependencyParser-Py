import unittest

from DataStructure.CounterHashMap import CounterHashMap

from DependencyParser.TurkishDependencyTreeBankCorpus import TurkishDependencyTreeBankCorpus
from DependencyParser.TurkishDependencyType import TurkishDependencyType


class TurkishDependencyTreeBankCorpusTest(unittest.TestCase):

    def test_DependencyCorpus(self):
        relationCounts = CounterHashMap()
        corpus = TurkishDependencyTreeBankCorpus("../metu-treebank.xml")
        self.assertEqual(5635, corpus.sentenceCount())
        wordCount = 0
        for i in range(corpus.sentenceCount()):
            sentence = corpus.getSentence(i)
            wordCount += sentence.wordCount()
            for j in range(sentence.wordCount()):
                word = sentence.getWord(j)
                if word.getRelation() is not None:
                    relationCounts.put(word.getRelation().getTurkishDependencyType())
        self.assertEqual(11692, relationCounts.get(TurkishDependencyType.MODIFIER))
        self.assertEqual(903, relationCounts.get(TurkishDependencyType.INTENSIFIER))
        self.assertEqual(1142, relationCounts.get(TurkishDependencyType.LOCATIVE_ADJUNCT))
        self.assertEqual(240, relationCounts.get(TurkishDependencyType.VOCATIVE))
        self.assertEqual(7261, relationCounts.get(TurkishDependencyType.SENTENCE))
        self.assertEqual(16, relationCounts.get(TurkishDependencyType.EQU_ADJUNCT))
        self.assertEqual(159, relationCounts.get(TurkishDependencyType.NEGATIVE_PARTICLE))
        self.assertEqual(4481, relationCounts.get(TurkishDependencyType.SUBJECT))
        self.assertEqual(2476, relationCounts.get(TurkishDependencyType.COORDINATION))
        self.assertEqual(2050, relationCounts.get(TurkishDependencyType.CLASSIFIER))
        self.assertEqual(73, relationCounts.get(TurkishDependencyType.COLLOCATION))
        self.assertEqual(1516, relationCounts.get(TurkishDependencyType.POSSESSOR))
        self.assertEqual(523, relationCounts.get(TurkishDependencyType.ABLATIVE_ADJUNCT))
        self.assertEqual(23, relationCounts.get(TurkishDependencyType.FOCUS_PARTICLE))
        self.assertEqual(1952, relationCounts.get(TurkishDependencyType.DETERMINER))
        self.assertEqual(1361, relationCounts.get(TurkishDependencyType.DATIVE_ADJUNCT))
        self.assertEqual(202, relationCounts.get(TurkishDependencyType.APPOSITION))
        self.assertEqual(289, relationCounts.get(TurkishDependencyType.QUESTION_PARTICLE))
        self.assertEqual(597, relationCounts.get(TurkishDependencyType.S_MODIFIER))
        self.assertEqual(10, relationCounts.get(TurkishDependencyType.ETOL))
        self.assertEqual(8338, relationCounts.get(TurkishDependencyType.OBJECT))
        self.assertEqual(271, relationCounts.get(TurkishDependencyType.INSTRUMENTAL_ADJUNCT))
        self.assertEqual(85, relationCounts.get(TurkishDependencyType.RELATIVIZER))
        self.assertEqual(53993, wordCount)


if __name__ == '__main__':
    unittest.main()
