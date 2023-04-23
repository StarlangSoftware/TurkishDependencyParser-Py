from DependencyParser.Universal.UniversalDependencyPosType import UniversalDependencyPosType
from DependencyParser.Universal.UniversalDependencyRelation import UniversalDependencyRelation


class UniversalDependencyTreeBankFeatures:

    feature_list: dict

    universal_feature_types = ["PronType", "NumType", "Poss", "Reflex", "Foreign",
            "Abbr", "Typo", "Gender", "Animacy", "NounClass",
            "Number", "Case", "Definite", "Degree", "VerbForm",
            "Mood", "Tense", "Aspect", "Voice", "Evident",
            "Polarity", "Person", "Polite", "Clusivity"]

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
                                ["Ex", "In"]]

    turkish_feature_values = [["Art", "Dem", "Ind", "Int", "Neg", "Prs", "Rcp", "Rel", "Tot"],
                              ["Card", "Dist", "Ord"],
                              [],
                              ["Yes"],
                              [],

                              ["Yes"],
                              [],
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
                              [],
                              []]

    english_feature_values = [["Art", "Dem", "Emp", "Ind", "Int", "Neg", "Prs", "Rcp", "Rel", "Tot"],
                              ["Card", "Frac", "Mult", "Ord"],
                              ["Yes"],
                              [],
                              [],

                              [],
                              [],
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

                              [],
                              ["1", "2", "3"],
                              [],
                              []]

    @staticmethod
    def featureIndex(featureName: str) -> int:
        if '[' in featureName:
            featureName = featureName[0: featureName.index('[')]
        for i in range(len(UniversalDependencyTreeBankFeatures.universal_feature_types)):
            if UniversalDependencyTreeBankFeatures.universal_feature_types[i] == featureName:
                return i
        return -1

    @staticmethod
    def posIndex(uPos: str) -> int:
        index = 0
        for universalDependencyPosType in UniversalDependencyPosType:
            if universalDependencyPosType.name == uPos:
                return index
            index = index + 1
        return -1

    @staticmethod
    def dependencyIndex(universalDependency: str) -> int:
        index = 0
        for dependency in UniversalDependencyRelation.universal_dependency_types:
            if dependency == universalDependency:
                return index
            index = index + 1
        return -1

    @staticmethod
    def numberOfValues(language: str, featureName: str) -> int:
        feature_index = UniversalDependencyTreeBankFeatures.featureIndex(featureName)
        if feature_index != -1:
            if language == "en":
                return len(UniversalDependencyTreeBankFeatures.english_feature_values[feature_index])
            elif language == "tr":
                return len(UniversalDependencyTreeBankFeatures.turkish_feature_values[feature_index])
        return -1

    @staticmethod
    def featureValueIndex(language: str, featureName: str, featureValue: str):
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
        return self.feature_list[feature]

    def featureExists(self, feature: str) -> bool:
        return feature in self.feature_list

    def __str__(self) -> str:
        if len(self.feature_list) == 0:
            return "_"
        result = ""
        for feature in self.feature_list:
            if result == "":
                result = feature + "=" + self.getFeatureValue(feature)
            else:
                result += "|" + feature + "=" + self.getFeatureValue(feature)
        return result
