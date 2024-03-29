import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# mention a project version
__version__ = "0.0.0"

REPO_NAME = "End-To-End-Machine-Learning-Project"
AUTHOR_USER_NAME = "jay-khade-45"
SRC_REPO = "mlProject"
AUTHOR_EMAIL = "jaykhade2023@gmail.com"

# using setuptools, we can set up src/mlproject as local package.
# local package?
# setting up this folder as local package, so we can import the functionality from here.
# .e present in requirement.txt will install setup.py file


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)