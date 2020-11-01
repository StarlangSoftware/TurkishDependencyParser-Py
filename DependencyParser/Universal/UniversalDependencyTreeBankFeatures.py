class UniversalDependencyTreeBankFeatures:

    featureList: dict

    def __init__(self, features: str):
        self.featureList = {}
        if features != "_":
            _list = features.split("\\|")
            for feature in _list:
                if "=" in feature:
                    featureName = feature[0: feature.index("=") - 1].strip()
                    featureValue = feature[feature.index("=") + 1:].strip()
                    self.featureList[featureName] = featureValue
                else:
                    print("Feature does not contain = ->" + features)

    def getFeatureValue(self, feature: str) -> str:
        return self.featureList[feature]

    def __str__(self) -> str:
        if len(self.featureList) == 0:
            return "_"
        result = ""
        for feature in self.featureList:
            if result == "":
                result = feature + "=" + self.getFeatureValue(feature)
            else:
                result += "|" + feature + "=" + self.getFeatureValue(feature)
        return result
