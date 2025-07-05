import unittest

from DependencyParser.Universal.UniversalDependencyTreeBankCorpus import UniversalDependencyTreeBankCorpus


class TurkishDependencyTreeBankCorpusTest(unittest.TestCase):

    def wordCount(self, corpus: UniversalDependencyTreeBankCorpus)-> int:
        word_count = 0
        for i in range (0, corpus.sentenceCount()):
            word_count += corpus.getSentence(i).wordCount()
        return word_count

    def splitCount(self, corpus: UniversalDependencyTreeBankCorpus)-> int:
        split_count = 0
        for i in range (0, corpus.sentenceCount()):
            split_count += corpus.getSentence(i).splitSize()
        return split_count

    def test_DependencyCorpus1(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_gb-ud-test.conllu")
        self.assertEqual(2880, corpus.sentenceCount())
        self.assertEqual(17177, self.wordCount(corpus))
        self.assertEqual(371, self.splitCount(corpus))

    def test_DependencyCorpus2(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_imst2-ud-dev.conllu")
        self.assertEqual(1100, corpus.sentenceCount())
        self.assertEqual(10542, self.wordCount(corpus))
        self.assertEqual(279, self.splitCount(corpus))

    def test_DependencyCorpus3(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_imst2-ud-test.conllu")
        self.assertEqual(1100, corpus.sentenceCount())
        self.assertEqual(10032, self.wordCount(corpus))
        self.assertEqual(278, self.splitCount(corpus))

    def test_DependencyCorpus4(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_imst2-ud-train.conllu")
        self.assertEqual(3435, corpus.sentenceCount())
        self.assertEqual(37522, self.wordCount(corpus))
        self.assertEqual(1082, self.splitCount(corpus))

    def test_DependencyCorpus5(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_pud-ud-test.conllu")
        self.assertEqual(1000, corpus.sentenceCount())
        self.assertEqual(16881, self.wordCount(corpus))
        self.assertEqual(346, self.splitCount(corpus))

    def test_DependencyCorpus6(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_boun-ud-dev.conllu")
        self.assertEqual(979, corpus.sentenceCount())
        self.assertEqual(12289, self.wordCount(corpus))
        self.assertEqual(266, self.splitCount(corpus))

    def test_DependencyCorpus7(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_boun-ud-test.conllu")
        self.assertEqual(979, corpus.sentenceCount())
        self.assertEqual(12210, self.wordCount(corpus))
        self.assertEqual(194, self.splitCount(corpus))

    def test_DependencyCorpus8(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_boun-ud-train.conllu")
        self.assertEqual(7803, corpus.sentenceCount())
        self.assertEqual(100713, self.wordCount(corpus))
        self.assertEqual(2914, self.splitCount(corpus))

    def test_DependencyCorpus9(self):
        corpus = UniversalDependencyTreeBankCorpus("../en_partut-ud-test.conllu")
        self.assertEqual(153, corpus.sentenceCount())
        self.assertEqual(3408, self.wordCount(corpus))

    def test_DependencyCorpus10(self):
        corpus = UniversalDependencyTreeBankCorpus("../en_ewt-ud-test.conllu")
        self.assertEqual(2077, corpus.sentenceCount())
        self.assertEqual(25094, self.wordCount(corpus))

    def test_DependencyCorpus11(self):
        corpus = UniversalDependencyTreeBankCorpus("../en_lines-ud-test.conllu")
        self.assertEqual(1035, corpus.sentenceCount())
        self.assertEqual(17675, self.wordCount(corpus))

    def test_DependencyCorpus12(self):
        corpus = UniversalDependencyTreeBankCorpus("../en_gum-ud-test.conllu")
        self.assertEqual(1096, corpus.sentenceCount())
        self.assertEqual(19905, self.wordCount(corpus))

    if __name__ == '__main__':
        unittest.main()
