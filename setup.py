from setuptools import find_packages, setup
from typing import List

hypen_e = "-e ."

def get_requirement(file_path: str) -> List[str]:
    """
    This function returns the list of requirements from the given file path.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Removes extra spaces or newlines
    
    if hypen_e in requirements:
        requirements.remove(hypen_e)
    
    return requirements

setup(
    name='PROJECT1',
    version='3.12.0',
    author='jyothprasad2724',
    author_email='jyothiprasadkommuru27@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirement.txt'),
    python_requires='>=3.6',
    
)
