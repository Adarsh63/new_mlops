from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = ("-e .")


def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        # Read line means 1 element will picked up from requirements.text file
        requirements = file_obj.readline()
        # list comprehension
        requirements = [req.replace("/n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="new_mlops",
    version="0.0.1",
    authore="Adarsh",
    authore_email="tadarshbt@gamil.com",
    packages=find_packages(),
    install_requirements=get_requirements("requirements.txt")
)
