from setuptools import setup

setup(
    name='NlpToolkit-DependencyParser',
    version='1.0.15',
    packages=['DependencyParser', 'DependencyParser.Turkish', 'DependencyParser.Universal', 'DependencyParser.Stanford'],
    url='https://github.com/StarlangSoftware/TurkishDependencyParser-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Turkish Dependency Parser',
    install_requires=['NlpToolkit-MorphologicalAnalysis']
)
