from os.path import dirname
from os.path import join
import setuptools


def readme() -> str:
    """Utility function to read the README file.
    Used for the long_description.  It's nice, because now 1) we have a top
    level README file and 2) it's easier to type in the README file than to put
    a raw string in below.
    :return: content of README.md
    """
    return open(join(dirname(__file__), "README.md")).read()


setuptools.setup(
    name="streamlit-sparrow-labeling",
    version="0.1.0",
    author="Andrej Baranovskij",
    author_email="andrejus.baranovskis@gmail.com",
    description="Streamlit component for invoice document labeling.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/katanaml/streamlit-sparrow-labeling-comp",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.9",
    install_requires=[
        "streamlit >= 1.15",
        "streamlit-nested-layout",
        "streamlit-javascript"
    ]
)
