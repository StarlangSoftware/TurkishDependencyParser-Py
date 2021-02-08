import unittest

from DependencyParser.Universal.UniversalDependencyPosType import UniversalDependencyPosType
from DependencyParser.Universal.UniversalDependencyRelation import UniversalDependencyRelation
from DependencyParser.Universal.UniversalDependencyType import UniversalDependencyType


class UniversalDependencyRelationTest(unittest.TestCase):

    def test_DependencyPosType(self):
        self.assertEqual(UniversalDependencyRelation.getDependencyPosType("adj"), UniversalDependencyPosType.ADJ)
        self.assertEqual(UniversalDependencyRelation.getDependencyPosType("intj"), UniversalDependencyPosType.INTJ)
        self.assertEqual(UniversalDependencyRelation.getDependencyPosType("Det"), UniversalDependencyPosType.DET)

    def test_DependencyType(self):
        self.assertEqual(UniversalDependencyRelation.getDependencyTag("acl"), UniversalDependencyType.ACL)
        self.assertEqual(UniversalDependencyRelation.getDependencyTag("iobj"), UniversalDependencyType.IOBJ)
        self.assertEqual(UniversalDependencyRelation.getDependencyTag("Iobj"), UniversalDependencyType.IOBJ)
        self.assertEqual(UniversalDependencyRelation.getDependencyTag("fixed"), UniversalDependencyType.FIXED)

