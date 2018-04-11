from setuptools import setup, find_packages

setup(
    name="scdmaker",
    version="0.1",
    description="SCD create/edit/verify toolbox",
    author="Ivan Alexandrov",
    packages=find_packages(),
    platforms="any",
    install_requires=[
        "lxml"
    ],
    include_packages_data=True,
    zip_safe=False
)
