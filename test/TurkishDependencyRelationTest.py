import unittest

from DependencyParser.Turkish.TurkishDependencyRelation import TurkishDependencyRelation
from DependencyParser.Turkish.TurkishDependencyType import TurkishDependencyType


class TurkishDependencyRelationTest(unittest.TestCase):

    def test_DependencyType(self):
        self.assertEqual(TurkishDependencyRelation.getDependencyTag("subject"), TurkishDependencyType.SUBJECT)
        self.assertEqual(TurkishDependencyRelation.getDependencyTag("vocative"), TurkishDependencyType.VOCATIVE)
        self.assertEqual(TurkishDependencyRelation.getDependencyTag("Relativizer"), TurkishDependencyType.RELATIVIZER)

