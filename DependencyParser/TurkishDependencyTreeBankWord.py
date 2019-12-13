from Dictionary.Word import Word

from DependencyParser.TurkishDependencyRelation import TurkishDependencyRelation


class TurkishDependencyTreeBankWord(Word):

    __parse: MorphologicalParse
    __originalParses: list
    __relation: TurkishDependencyRelation