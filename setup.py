from setuptools import find_packages,setup
from typing import List



def get_requirement(file_path:str)->List[str]:
    '''
    this function return prerequisite requirements
    '''
    requirements =[]

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements




setup(
    name="ML_project",
    version="0.1",
    author="shubham solanki",
    author_email="shubham163solankicp8@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement("requirements.txt"),
)