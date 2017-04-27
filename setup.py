from setuptools import setup, find_packages

setup(
    name='OCL Pygments Lexer',
    version='0.0.1',
    author = "Marek Suchánek",
    author_email='suchama4@fit.cvut.cz',
    description = "Pygments lexer for OCL",
    license = "MIT",
    keywords = "pygments lexer ocl",
    url = "https://github.com/MarekSuchanek/pygments-ocl-lexer",
    packages=find_packages(),
    entry_points="""
    [pygments.lexers]
    ocllexer = ocl_lexer:OCLLexer
    """,
    install_requires={
        'pygments'
    }
)
