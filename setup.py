from setuptools import find_packages, setup
from typing import List

def get_requirements(filepath: str) -> List[str]:
    requirements=[]
    Hypen_dot='-e .'
    with open(filepath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('/n',"") for req in requirements]
        if Hypen_dot in requirements:
            requirements.remove(Hypen_dot)

        return requirements

setup(
        name='Diamond prediction model',
        version='0.1',
        author='Javier',
        author_email="aviverma.cse@gmail.com",
        install_requires=get_requirements('requirements.txt'),
        packages=find_packages()
)


