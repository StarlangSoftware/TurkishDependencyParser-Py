from setuptools import setup

setup(
    name='NlpToolkit-DependencyParser',
    version='1.0.13',
    packages=['DependencyParser', 'DependencyParser.Turkish', 'DependencyParser.Universal', 'DependencyParser.Stanford'],
    url='https://github.com/olcaytaner/TurkishDependencyParser-Py',
    license='',
    author='olcaytaner',
    author_email='olcaytaner@isikun.edu.tr',
    description='Turkish Dependency Parser',
    install_requires=['NlpToolkit-MorphologicalAnalysis']
)
