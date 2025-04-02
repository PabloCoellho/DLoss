from setuptools import setup, find_packages

setup(
    name="dloss",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Pablo Coelho",
    author_email="pablo.martins@aluno.ufop.edu.br",
    description="Função de erro dloss",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PabloCoellho/DLoss",
    python_requires=">=3.6",
)
