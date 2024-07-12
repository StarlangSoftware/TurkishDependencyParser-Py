from DependencyParser.Universal.UniversalDependencyPosType import UniversalDependencyPosType
from DependencyParser.Universal.UniversalDependencyRelation import UniversalDependencyRelation


class UniversalDependencyTreeBankFeatures:

    feature_list: dict

    universal_feature_types = ["PronType", "NumType", "Poss", "Reflex", "Foreign",
            "Abbr", "Typo", "Gender", "Animacy", "NounClass",
            "Number", "Case", "Definite", "Degree", "VerbForm",
            "Mood", "Tense", "Aspect", "Voice", "Evident",
            "Polarity", "Person", "Polite", "Clusivity", "NumForm"]

    universal_feature_values = [["Art", "Dem", "Emp", "Exc", "Ind", "Int", "Neg", "Prs", "Rcp", "Rel", "Tot"],
                                ["Card", "Dist", "Frac", "Mult", "Ord", "Range", "Sets"],
                                ["Yes"],
                                ["Yes"],
                                ["Yes"],

                                ["Yes"],
                                ["Yes"],
                                ["Com", "Fem", "Masc", "Neut"],
                                ["Anim", "Hum", "Inan", "Nhum"],
                                ["Bantu1", "Bantu2", "Bantu3", "Bantu4", "Bantu5", "Bantu6", "Bantu7", "Bantu8", "Bantu9", "Bantu10", "Bantu11", "Bantu12", "Bantu13", "Bantu14", "Bantu15", "Bantu16", "Bantu17", "Bantu18", "Bantu19", "Bantu20", "Bantu21", "Bantu22", "Bantu23", "Wol1", "Wol2", "Wol3", "Wol4", "Wol5", "Wol6", "Wol7", "Wol8", "Wol9", "Wol10", "Wol11", "Wol12"],

                                ["Coll", "Count", "Dual", "Grpa", "Grpl", "Inv", "Pauc", "Plur", "Ptan", "Sing", "Tri"],
                                ["Abs", "Acc", "Erg", "Nom", "Abe", "Ben", "Cau", "Cmp", "Cns", "Com", "Dat", "Dis", "Equ", "Gen", "Ins", "Par", "Tem", "Tra", "Voc", "Abl", "Add", "Ade", "All", "Del", "Ela", "Ess", "Ill", "Ine", "Lat", "Loc", "Per", "Sbe", "Sbl", "Spl", "Sub", "Sup", "Ter"],
                                ["Com", "Cons", "Def", "Ind", "Spec"],
                                ["Abs", "Aug", "Cmp", "Dim", "Equ", "Pos", "Sup"],
                                ["Conv", "Fin", "Gdv", "Ger", "Inf", "Part", "Sup", "Vnoun"],

                                ["Adm", "Cnd", "Des", "Imp", "Ind", "Int", "Irr", "Jus", "Nec", "Opt", "Pot", "Prp", "Qot", "Sub"],
                                ["Fut", "Imp", "Past", "Pqp", "Pres"],
                                ["Hab", "Imp", "Iter", "Perf", "Prog", "Prosp"],
                                ["Act", "Antip", "Bfoc", "Cau", "Dir", "Inv", "Lfoc", "Mid", "Pass", "Rcp"],
                                ["Fh", "Nfh"],

                                ["Neg", "Pos"],
                                ["0", "1", "2", "3", "4"],
                                ["Elev", "Form", "Humb", "Infm"],
                                ["Ex", "In"],
                                ["Word", "Digit", "Roman"]]

    turkish_feature_values = [["Art", "Dem", "Ind", "Int", "Neg", "Prs", "Rcp", "Rel", "Tot"],
                              ["Card", "Dist", "Ord"],
                              [],
                              ["Yes"],
                              ["Yes"],

                              ["Yes"],
                              ["Yes"],
                              [],
                              [],
                              [],

                              ["Plur", "Sing"],
                              ["Acc", "Nom", "Dat", "Equ", "Gen", "Ins", "Abl", "Loc"],
                              ["Def", "Ind"],
                              ["Cmp", "Sup"],
                              ["Conv", "Fin", "Part", "Vnoun"],

                              ["Cnd", "Des", "Gen", "Imp", "Ind", "Nec", "Opt", "Pot", "DesPot", "CndPot", "CndGen", "CndGenPot", "GenPot", "PotPot", "GenNecPot", "GenNec", "NecPot", "GenPotPot", "ImpPot"],
                              ["Fut", "Past", "Pqp", "Pres", "Aor"],
                              ["Imp", "Perf", "Prog", "Prosp", "Hab", "Rapid"],
                              ["Cau", "Pass", "Rcp", "Rfl", "CauCau", "CauCauPass", "CauPass", "CauPassRcp", "CauRcp", "PassPass", "PassRfl", "PassRcp"],
                              ["Fh", "Nfh"],

                              ["Neg", "Pos"],
                              ["1", "2", "3"],
                              ["Form", "Infm"],
                              [],
                              []]

    english_feature_values = [["Art", "Dem", "Emp", "Ind", "Int", "Neg", "Prs", "Rcp", "Rel", "Tot"],
                              ["Card", "Frac", "Mult", "Ord"],
                              ["Yes"],
                              ["Yes"],
                              ["Yes"],

                              ["Yes"],
                              ["Yes"],
                              ["Fem", "Masc", "Neut"],
                              [],
                              [],

                              ["Plur", "Sing"],
                              ["Acc", "Nom", "Gen"],
                              ["Def", "Ind"],
                              ["Cmp", "Pos", "Sup"],
                              ["Fin", "Ger", "Inf", "Part"],

                              ["Imp", "Ind", "Sub"],
                              ["Past", "Pres"],
                              [],
                              ["Pass"],
                              [],

                              ["Neg"],
                              ["1", "2", "3"],
                              [],
                              [],
                              ["Word", "Digit", "Roman"]]

    @staticmethod
    def featureIndex(featureName: str) -> int:
        """
        Returns the index of the universal feature type in the universalFeatureTypes array, given the name of the feature
        type.
        :param featureName: Name of the feature type
        :return: Index of the universal feature type in the universalFeatureTypes array. If the name does not exist, the
        function returns -1.
        """
        if '[' in featureName:
            featureName = featureName[0: featureName.index('[')]
        for i in range(len(UniversalDependencyTreeBankFeatures.universal_feature_types)):
            if UniversalDependencyTreeBankFeatures.universal_feature_types[i] == featureName:
                return i
        return -1

    @staticmethod
    def posIndex(uPos: str) -> int:
        """
        Returns the index of the given universal dependency pos.
        :param uPos: Given universal dependency part of speech tag.
        :return: The index of the universal dependency pos.
        """
        index = 0
        for universalDependencyPosType in UniversalDependencyPosType:
            if universalDependencyPosType.name == uPos:
                return index
            index = index + 1
        return -1

    @staticmethod
    def dependencyIndex(universalDependency: str) -> int:
        """
        Returns the index of the universal dependency type in the universalDependencyTypes array, given the name of the
        universal dependency type.
        :param universalDependency: Universal dependency type
        :return: Index of the universal dependency type in the universalDependencyTypes array. If the name does not exist,
        the function returns -1.
        """
        index = 0
        for dependency in UniversalDependencyRelation.universal_dependency_types:
            if dependency == universalDependency:
                return index
            index = index + 1
        return -1

    @staticmethod
    def numberOfValues(language: str, featureName: str) -> int:
        """
        Returns the number of distinct values for a feature in a given language
        :param language: Language name. Currently, 'en' and 'tr' languages are supported.
        :param featureName: Name of the feature type.
        :return: The number of distinct values for a feature in a given language
        """
        feature_index = UniversalDependencyTreeBankFeatures.featureIndex(featureName)
        if feature_index != -1:
            if language == "en":
                return len(UniversalDependencyTreeBankFeatures.english_feature_values[feature_index])
            elif language == "tr":
                return len(UniversalDependencyTreeBankFeatures.turkish_feature_values[feature_index])
        return -1

    @staticmethod
    def featureValueIndex(language: str, featureName: str, featureValue: str):
        """
        Returns the index of the given value in the feature value array for the given feature in the given
        language.
        :param language: Language name. Currently, 'en' and 'tr' languages are supported.
        :param featureName: Name of the feature.
        :param featureValue: Value of the feature.
        :return: The index of the given feature value in the feature value array for the given feature in the given
        language.
        """
        feature_index = UniversalDependencyTreeBankFeatures.featureIndex(featureName)
        if feature_index != -1:
            if language == "en":
                search_array = UniversalDependencyTreeBankFeatures.english_feature_values
            elif language == "tr":
                search_array = UniversalDependencyTreeBankFeatures.turkish_feature_values
            else:
                search_array = UniversalDependencyTreeBankFeatures.universal_feature_values
            feature_value_index = -1
            for i in range(len(search_array[feature_index])):
                if search_array[feature_index][i] == featureValue:
                    feature_value_index = i
            return feature_value_index
        return -1

    def __init__(self, language: str, features: str):
        """
        Constructor of a UniversalDependencyTreeBankFeatures object. Given the language of the word and features of the
        word as a string, the method splits the features with respect to pipe character. Then for each feature type and
        value pair, their values and types are inserted into the featureList hash map. The method also check for validity
        of the feature values for that feature type.
        :param language: Language name. Currently, 'en' and 'tr' languages are supported.
        :param features: Feature string.
        """
        self.feature_list = {}
        if features != "_":
            _list = features.split("|")
            for feature in _list:
                if "=" in feature:
                    feature_name = feature[0: feature.index("=")].strip()
                    feature_value = feature[feature.index("=") + 1:].strip()
                    if UniversalDependencyTreeBankFeatures.featureValueIndex(language, feature_name, feature_value) != -1:
                        self.feature_list[feature_name] = feature_value
                    else:
                        print("Either the feature " + feature_name + " or the value " + feature_value + " is wrong")
                else:
                    print("Feature does not contain = ->" + features)

    def getFeatureValue(self, feature: str) -> str:
        """
        Gets the value of a given feature.
        :param feature: Name of the feature
        :return: Value of the feature
        """
        return self.feature_list[feature]

    def featureExists(self, feature: str) -> bool:
        """
        Checks if the given feature exists in the feature list.
        :param feature: Name of the feature
        :return: True, if the feature list contains the feature, false otherwise.
        """
        return feature in self.feature_list

    def __str__(self) -> str:
        """
        Overridden toString method. Returns feature with their values separated with pipe characters.
        :return: A string of feature values and their names separated with pipe character.
        """
        if len(self.feature_list) == 0:
            return "_"
        result = ""
        for feature in self.feature_list:
            if result == "":
                result = feature + "=" + self.getFeatureValue(feature)
            else:
                result += "|" + feature + "=" + self.getFeatureValue(feature)
        return result
