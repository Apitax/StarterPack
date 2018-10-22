from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='StarterPack',
    packages=find_packages(),  # this must be the same as the name above
    version='3.0.0',
    description='Provides a simple way to deploy Apitax with a custom project.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Shawn Clake',
    author_email='shawn.clake@gmail.com',
    url='https://github.com/Apitax/StarterPack',
    keywords=['restful', 'api', 'commandtax', 'scriptax'],
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'apitaxcore==3.0.6',  # Core
        'commandtax==0.0.8',  # Commandtax Support
        'scriptax==0.0.5',  # Scriptax Support (.ah)
        'scriptaxstd==0.0.7',  # Scriptax STD Lib
        'apitaxdrivers==0.0.12',  # Misc Drivers (ie. Github connectivity)
        'apitax==3.0.3',  # Apitax
    ],
)
