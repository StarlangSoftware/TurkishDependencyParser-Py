class UniversalDependencyTreeBankFeatures:

    feature_list: dict

    def __init__(self, features: str):
        self.feature_list = {}
        if features != "_":
            _list = features.split("\\|")
            for feature in _list:
                if "=" in feature:
                    feature_name = feature[0: feature.index("=") - 1].strip()
                    feature_value = feature[feature.index("=") + 1:].strip()
                    self.feature_list[feature_name] = feature_value
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
