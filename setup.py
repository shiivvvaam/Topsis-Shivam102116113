from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

setup(
    name="Topsis-Shivam102116113",
    version="1.0.0",
    author="Shivam",
    author_email="sdhiman1_be21@thapar.edu",
    description="Calculating topsis score and finding rank",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={'':'src'},
    py_modules=['Topsis-Shivam102116113'],
    include_package_data=True,
    install_requires=['pandas','numpy','os','sys','requests'],
    
)
