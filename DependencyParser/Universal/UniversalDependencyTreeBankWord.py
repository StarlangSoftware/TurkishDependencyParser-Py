from Dictionary.Word import Word

from DependencyParser.Universal.UniversalDependencyPosType import UniversalDependencyPosType
from DependencyParser.Universal.UniversalDependencyRelation import UniversalDependencyRelation
from DependencyParser.Universal.UniversalDependencyTreeBankFeatures import UniversalDependencyTreeBankFeatures


class UniversalDependencyTreeBankWord(Word):

    id: int
    lemma: str
    u_pos: UniversalDependencyPosType
    x_pos: str
    features: UniversalDependencyTreeBankFeatures
    relation: UniversalDependencyRelation
    deps: str
    misc: str

    def constructor1(self,
                 id: int,
                 lemma: str,
                 upos: UniversalDependencyPosType,
                 xpos: str,
                 features: UniversalDependencyTreeBankFeatures,
                 relation: UniversalDependencyRelation,
                 deps: str,
                 misc: str):
        self.id = id
        self.lemma = lemma
        self.u_pos = upos
        self.x_pos = xpos
        self.deps = deps
        self.features = features
        self.relation = relation
        self.misc = misc

    def constructor2(self):
        self.id = 0
        self.lemma = ""
        self.u_pos = UniversalDependencyPosType.X
        self.x_pos = ""
        self.features = None
        self.deps = ""
        self.misc = ""
        self.relation = UniversalDependencyRelation()

    def __init__(self,
                 id: int = None,
                 name: str = None,
                 lemma: str = None,
                 upos: UniversalDependencyPosType = None,
                 xpos: str = None,
                 features: UniversalDependencyTreeBankFeatures = None,
                 relation: UniversalDependencyRelation = None,
                 deps: str = None,
                 misc: str = None):
        if id is not None:
            super().__init__(name)
            self.constructor1(id,
                              lemma,
                              upos,
                              xpos,
                              features,
                              relation,
                              deps,
                              misc)
        else:
            super().__init__("root")
            self.constructor2()

    def getId(self) -> int:
        return self.id

    def getLemma(self) -> str:
        return self.lemma

    def getUpos(self) -> UniversalDependencyPosType:
        return self.u_pos

    def getXPos(self) -> str:
        return self.x_pos

    def getFeatures(self) -> UniversalDependencyTreeBankFeatures:
        return self.features

    def getFeatureValue(self, featureName: str) -> str:
        return self.features.getFeatureValue(featureName)

    def featureExists(self, featureName: str) -> bool:
        return self.features.featureExists(featureName)

    def getRelation(self) -> UniversalDependencyRelation:
        return self.relation

    def setRelation(self, relation: UniversalDependencyRelation):
        self.relation = relation

    def getDeps(self) -> str:
        return self.deps

    def getMisc(self) -> str:
        return self.misc

    def __str__(self) -> str:
        return self.id.__str__() + "\t" + self.name + "\t" + self.lemma + "\t" + self.u_pos.__str__() + "\t" + \
               self.x_pos + "\t" + self.features.__str__() + "\t" + self.relation.to().__str__() + "\t" + \
               self.relation.__str__().lower() + "\t" + self.deps + "\t" + self.misc
