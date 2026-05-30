Dependency TreeBanks
============

Tesnière introduced the dependency trees, structural order, the concept of dependency and applied his representation concepts in a variety of languages such as French, Greek, Russian, Italian, and so on. In structural order, syntactic relations are presented in a hierarchical manner as opposed to the linear order. He uses “stemmas” to reflect hierarchy. 

Today, dependency grammars are divided into two. One study from the tradition that applies this distinction to the dependency grammar is the Prague Dependency Treebank (PDT) developed by the Prague School of Functional and Structural Linguistics. A famous example for the other school of thought that displays linear order is the Penn Treebank that functioned between the years of 1989-1996, containing seven million annotated texts from American English. 

In 2005, The Stanford Dependencies developed for the parsing of the English language and to be used in NLP studies and in Stanford Dependency Parser. Stanford Dependencies were acknowledged as the standard for the dependency analyses of English. However, the Stanford Dependency parser could not reach an adequate accuracy when it was used with other dependency schemes. In the following years, the Universal Dependency Treebank (UDT) project pioneered to develop treebanks for languages other than English by transforming the Stanford dependencies into a more inclusive annotation scheme for a diverse set of languages.

The developments in the dependency treebanking made it clear that Turkish language needed a Treebank of its own. The first Turkish language dependency treebank is METU-Sabanci Turkish Treebank. This treebank used a corpus that consisted of 7,262 sentences and included morphological and syntactic annotations. In 2016, this tree-bank was revisited under the name of ITU-METU-Sabancı Treebank (IMST) to reduce the inconsistencies of its earlier version. They succeeded to reduce inconsistencies by applying a new annotation scheme. As a last step, The Bogazici-ITU-METU-Sabancı Treebank (BIMST) is updated as the same corpus. Having a linguistic team of three people, they created a new annotation scheme for IMST and manually re-annotated the data of 5.635 sentences while introducing new dependency relations that were not present in IMST.

Annotated UD (Universal Dependencies) Datasets
============
[Atis (Turkish)](http://104.247.163.162/nlptoolkit/turkish-ud1.html)

[Atis (English)](http://104.247.163.162/nlptoolkit/english-ud1.html)

[Tourism](http://104.247.163.162/nlptoolkit/turkish-ud5.html)

[Framenet](http://104.247.163.162/nlptoolkit/turkish-ud6.html)

[Kenet](http://104.247.163.162/nlptoolkit/turkish-ud7.html)

[Penn-Treebank](http://104.247.163.162/nlptoolkit/turkish-ud8.html)

[Gb](http://104.247.163.162/nlptoolkit/turkish-ud2.html)

[Pud](http://104.247.163.162/nlptoolkit/turkish-ud3.html)

[Imst](http://104.247.163.162/nlptoolkit/turkish-ud4.html)

Video Lectures
============

[<img src="https://github.com/StarlangSoftware/TurkishDependencyParser/blob/master/video1.jpg" width="50%">](https://youtu.be/fY8tn8ny0m4)[<img src="https://github.com/StarlangSoftware/TurkishDependencyParser/blob/master/video2.jpg" width="50%">](https://youtu.be/vS5o49V0wrU)

For Developers
============
You can also see either [Cython](https://github.com/starlangsoftware/TurkishDependencyParser-Cy), [Java](https://github.com/starlangsoftware/TurkishDependencyParser), [C++](https://github.com/starlangsoftware/TurkishDependencyParser-CPP), [C](https://github.com/starlangsoftware/TurkishDependencyParser-C), [Swift](https://github.com/starlangsoftware/TurkishDependencyParser-Swift), [Js](https://github.com/starlangsoftware/TurkishDependencyParser-Js), [Php](https://github.com/starlangsoftware/TurkishDependencyParser-Php), or [C#](https://github.com/starlangsoftware/TurkishDependencyParser-CS) repository.

## Requirements

* [Python 3.13 or higher](#python)
* [Git](#git)

### Python 

To check if you have a compatible version of Python installed, use the following command:

    python -V
    
You can find the latest version of Python [here](https://www.python.org/downloads/).

### Git

Install the [latest version of Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

## Pip Install

	pip3.13 install NlpToolkit-DependencyParser
	
## Download Code

In order to work on code, create a fork from GitHub page. 
Use Git for cloning the code to your local or below line for Ubuntu:

	git clone <your-fork-git-link>

A directory called DependencyParser will be created. Or you can use below link for exploring the code:

	git clone https://github.com/starlangsoftware/TurkishDependencyParser-Py.git

## Open project with Pycharm IDE

Steps for opening the cloned project:

* Start IDE
* Select **File | Open** from main menu
* Choose `TurkishDependencyParser-Py` file
* Select open as project option
* Couple of seconds, dependencies with Maven will be downloaded. 

# Cite

	@INPROCEEDINGS{9259799,
  	author={A. {Kuzgun} and N. {Cesur} and B. N. {Arıcan} and M. {Özçelik} and B. {Marşan} and N. {Kara} and D. B. {Aslan} and O. T. {Yıldız}},
  	booktitle={2020 Innovations in Intelligent Systems and Applications Conference (ASYU)}, 
  	title={On Building the Largest and Cross-Linguistic Turkish Dependency Corpus}, 
  	year={2020},
  	volume={},
  	number={},
  	pages={1-6},
  	doi={10.1109/ASYU50717.2020.9259799}}

For Contibutors
============

### Setup.py file
1. Do not forget to set package list. All subfolders should be added to the package list.
```
    packages=['Classification', 'Classification.Model', 'Classification.Model.DecisionTree',
              'Classification.Model.Ensemble', 'Classification.Model.NeuralNetwork',
              'Classification.Model.NonParametric', 'Classification.Model.Parametric',
              'Classification.Filter', 'Classification.DataSet', 'Classification.Instance', 'Classification.Attribute',
              'Classification.Parameter', 'Classification.Experiment',
              'Classification.Performance', 'Classification.InstanceList', 'Classification.DistanceMetric',
              'Classification.StatisticalTest', 'Classification.FeatureSelection'],
```
2. Package name should be lowercase and only may include _ character.
```
    name='nlptoolkit_math',
```

### Python files
1. Do not forget to comment each function.
```
    def __broadcast_shape(self, shape1: Tuple[int, ...], shape2: Tuple[int, ...]) -> Tuple[int, ...]:
        """
        Determines the broadcasted shape of two tensors.

        :param shape1: Tuple representing the first tensor shape.
        :param shape2: Tuple representing the second tensor shape.
        :return: Tuple representing the broadcasted shape.
        """
```
2. Function names should follow caml case.
```
    def addItem(self, item: str):
```
3. Local variables should follow snake case.
```
	det = 1.0
	copy_of_matrix = copy.deepcopy(self)
```
4. Class variables should be declared in each file.
```
class Eigenvector(Vector):
    eigenvalue: float
```
5. Variable types should be defined for function parameters and class variables.
```
    def getIndex(self, item: str) -> int:
```
6. For abstract methods, use ABC package and declare them with @abstractmethod.
```
    @abstractmethod
    def train(self, train_set: list[Tensor]):
        pass
```
7. For private methods, use __ as prefix in their names.
```
    def __infer_shape(self, data: Union[List, List[List], List[List[List]]]) -> Tuple[int, ...]:
```
8. For private class variables, use __ as prefix in their names.
```
class Matrix(object):
    __row: int
    __col: int
    __values: list[list[float]]
```
9. Write \_\_repr\_\_ class methods as toString methods
10. Write getter and setter class methods.
```
    def getOptimizer(self) -> Optimizer:
        return self.optimizer
    def setValue(self, value: Optional[Tensor]) -> None:
        self._value = value
```
11. If there are multiple constructors for a class, define them as constructor1, constructor2, ..., then from the original constructor call these methods.
```
    def constructor1(self):
        self.__values = []
        self.__size = 0

    def constructor2(self, values: list):
        self.__values = values.copy()
        self.__size = len(values)

    def __init__(self,
                 valuesOrSize=None,
                 initial=None):
        if valuesOrSize is None:
            self.constructor1()
        elif isinstance(valuesOrSize, list):
            self.constructor2(valuesOrSize)
```
12. Extend test classes from unittest and use separate unit test methods.
```
class TensorTest(unittest.TestCase):

    def test_inferred_shape(self):
        a = Tensor([[1.0, 2.0], [3.0, 4.0]])
        self.assertEqual((2, 2), a.getShape())

    def test_shape(self):
        a = Tensor([1.0, 2.0, 3.0])
        self.assertEqual((3, ), a.getShape())
```
13. Enumerated types should be used when necessary as enum classes.
```
class AttributeType(Enum):
    """
    Continuous Attribute
    """
    CONTINUOUS = auto()
    """
    Discrete Attribute
    """
    DISCRETE = auto()
```
