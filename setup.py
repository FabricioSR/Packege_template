from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_template",
    version="0.0.1",
    author="Fabricio",
    author_email="fabricio-rreis@hotmail.com",
    description="first packege",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FabricioSR/Packege_template.git",
    packages=find_packages(),
    install_requires='requirements.txt',
    python_requires='>=3.8',
    )   
