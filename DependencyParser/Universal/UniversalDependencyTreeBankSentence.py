from Corpus.Sentence import Sentence


class UniversalDependencyTreeBankSentence(Sentence):

    comments: list

    def __init__(self):
        super().__init__()
        self.comments = []

    def addComment(self, comment: str):
        self.comments.append(comment)

    def __str__(self) -> str:
        result = ""
        for comment in self.comments:
            result += comment + "\n"
        for word in self.words:
            result += word.__str__() + "\n"
        return result
