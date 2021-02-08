import unittest

from DependencyParser.Stanford.StanfordDependencyRelation import StanfordDependencyRelation
from DependencyParser.Stanford.StanfordDependencyType import StanfordDependencyType


class StanfordDependencyRelationTest(unittest.TestCase):

    def test_DependencyType(self):
        self.assertEqual(StanfordDependencyRelation.getDependencyTag("acomp"), StanfordDependencyType.ACOMP)
        self.assertEqual(StanfordDependencyRelation.getDependencyTag("discourse"), StanfordDependencyType.DISCOURSE)
        self.assertEqual(StanfordDependencyRelation.getDependencyTag("Iobj"), StanfordDependencyType.IOBJ)
        self.assertEqual(StanfordDependencyRelation.getDependencyTag("iobj"), StanfordDependencyType.IOBJ)
