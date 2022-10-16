from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="slider_grafic",
    version="0.0.1",
    author="gleibson",
    author_email="gleibson11@gmail.com",
    description="Cria um grafico com slider para um simulador de biossensor óptico",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GleibsonCardoso/silder_grafic_projetc",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
