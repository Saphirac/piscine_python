from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    author="saph",
    author_email="saph@42.fr",
    url="https://github.com/Saphirac/piscine_python",
    license="MIT",
    packages=find_packages(),  # automatically finds ft_package
    python_requires=">=3.6",
)
