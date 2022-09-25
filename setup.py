from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name='NlpToolkit-DependencyParser',
    version='1.0.23',
    packages=['DependencyParser', 'DependencyParser.Turkish', 'DependencyParser.Universal', 'DependencyParser.Stanford'],
    url='https://github.com/StarlangSoftware/TurkishDependencyParser-Py',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Turkish Dependency Parser',
    install_requires=['NlpToolkit-MorphologicalAnalysis'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
