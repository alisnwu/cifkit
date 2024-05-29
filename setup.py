from setuptools import setup, find_packages

setup(
    name="cifpy",
    version="0.01",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[],  # List your dependencies here
)
