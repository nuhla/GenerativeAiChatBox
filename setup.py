from setuptools import find_packages, setup

setup(
    name='mcqgeneratore',
    version='0.0.1',
    author='Nahla.I.M',
    author_email="NUHLAMASSRI@GMAAIL.COM",
    install_requires=['openai','langchain','stramlit','python-donenv','PyPDF2'],
    packages=find_packages()

)