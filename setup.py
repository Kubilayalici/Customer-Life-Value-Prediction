from setuptools import setup, find_packages
from typing import List

HYPEN_REQUIREMENT = "-e ."

def requirements(file_path: str) -> List[str]:
    """
    Parse a requirements file and return a list of packages.
    """
    requirements_list = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements_list = [req.strip() for req in requirements if req.strip()]
            if HYPEN_REQUIREMENT in requirements_list:
                requirements_list.remove(HYPEN_REQUIREMENT)
    except FileNotFoundError:
        pass
    return requirements_list

# Parse requirements from requirements.txt
requirements_list = requirements("requirements.txt")

setup(
    name="end_to_end_cltvp",
    version="0.1",
    author="Kubilay ALICI",
    author_email="kkubilay.alici@gmail.com",
    packages=find_packages(),
    install_requires=requirements_list,
)

