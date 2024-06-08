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
        """
        Constructor of the universal dependency word. Sets the attributes.
        :param id: Id of the word
        :param lemma: Lemma of the word
        :param upos: Universal part of speech tag.
        :param xpos: Extra part of speech tag
        :param features: Feature list of the word
        :param relation: Universal dependency relation of the word
        :param deps: External dependencies for the word
        :param misc: Miscellaneous information for the word.
        """
        self.id = id
        self.lemma = lemma
        self.u_pos = upos
        self.x_pos = xpos
        self.deps = deps
        self.features = features
        self.relation = relation
        self.misc = misc

    def constructor2(self):
        """
        Default constructor for the universal dependency word. Sets the attributes to default values.
        """
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
        """
        Accessor for the id attribute.
        :return: Id attribute
        """
        return self.id

    def getLemma(self) -> str:
        """
        Accessor for the lemma attribute.
        :return: Lemma attribute
        """
        return self.lemma

    def getUpos(self) -> UniversalDependencyPosType:
        """
        Accessor for the upos attribute.
        :return: Upos attribute
        """
        return self.u_pos

    def getXPos(self) -> str:
        """
        Accessor for the xpos attribute.
        :return: Xpos attribute
        """
        return self.x_pos

    def getFeatures(self) -> UniversalDependencyTreeBankFeatures:
        """
        Accessor for the features attribute.
        :return: Features attribute
        """
        return self.features

    def getFeatureValue(self, featureName: str) -> str:
        """
        Gets the value of a given feature.
        :param featureName: Name of the feature
        :return: Value of the feature
        """
        return self.features.getFeatureValue(featureName)

    def featureExists(self, featureName: str) -> bool:
        """
        Checks if the given feature exists.
        :param featureName: Name of the feature
        :return: True if the given feature exists, False otherwise
        """
        return self.features.featureExists(featureName)

    def getRelation(self) -> UniversalDependencyRelation:
        """
        Accessor for the relation attribute.
        :return: Relation attribute
        """
        return self.relation

    def setRelation(self, relation: UniversalDependencyRelation):
        """
        Mytator for the relation attribute.
        :param relation: New relation attribute
        """
        self.relation = relation

    def getDeps(self) -> str:
        """
        Accessor for the deps attribute.
        :return: Deps attribute
        """
        return self.deps

    def getMisc(self) -> str:
        """
        Accessor for the misc attribute.
        :return: Misc attribute
        """
        return self.misc

    def __str__(self) -> str:
        return self.id.__str__() + "\t" + self.name + "\t" + self.lemma + "\t" + self.u_pos.__str__() + "\t" + \
               self.x_pos + "\t" + self.features.__str__() + "\t" + self.relation.to().__str__() + "\t" + \
               self.relation.__str__().lower() + "\t" + self.deps + "\t" + self.misc
