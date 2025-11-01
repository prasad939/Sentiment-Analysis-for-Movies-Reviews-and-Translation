#used to create proper package and library
from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function return the  list of requirements
    
    """
    requirement_list:List[str] = []
    
    
    return requirement_list

setup(
    name=" Sentiment Analysis",
    version="0.0.1",
    author="Prasad",
    author_email="sanjurenuka1980@gmail.com",
    packages = find_packages(),
    install_required=get_requirements(),
)