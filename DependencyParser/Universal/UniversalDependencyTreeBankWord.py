from Dictionary.Word import Word

from DependencyParser.Universal.UniversalDependencyPosType import UniversalDependencyPosType
from DependencyParser.Universal.UniversalDependencyRelation import UniversalDependencyRelation
from DependencyParser.Universal.UniversalDependencyTreeBankFeatures import UniversalDependencyTreeBankFeatures


class UniversalDependencyTreeBankWord(Word):

    id: int
    lemma: str
    upos: UniversalDependencyPosType
    xpos: str
    features: UniversalDependencyTreeBankFeatures
    relation: UniversalDependencyRelation
    deps: str
    misc: str

    def __init__(self, id: int, name: str, lemma: str, upos: UniversalDependencyPosType, xpos: str,
                 features: UniversalDependencyTreeBankFeatures, relation: UniversalDependencyRelation, deps: str,
                 misc: str):
        super().__init__(name)
        self.id = id
        self.lemma = lemma
        self.upos = upos
        self.xpos = xpos
        self.deps = deps
        self.features = features
        self.relation = relation
        self.misc = misc

    def getId(self) -> int:
        return self.id

    def getLemma(self) -> str:
        return self.lemma

    def getUpos(self) -> UniversalDependencyPosType:
        return self.upos

    def getXPos(self) -> str:
        return self.xpos

    def getFeatures(self) -> UniversalDependencyTreeBankFeatures:
        return self.features

    def getFeatureValue(self, featureName: str) -> str:
        return self.features.getFeatureValue(featureName)

    def getRelation(self) -> UniversalDependencyRelation:
        return self.relation

    def getDeps(self) -> str:
        return self.deps

    def getMisc(self) -> str:
        return self.misc

    def __str__(self) -> str:
        return self.id.__str__() + "\t" + self.name + "\t" + self.lemma + "\t" + self.upos.__str__() + "\t" + \
               self.xpos + "\t" + self.features.__str__() + "\t" + self.relation.to().__str__() + "\t" + \
               self.relation.__str__().lower() + "\t" + self.deps + "\t" + self.misc
