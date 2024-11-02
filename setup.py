import setuptools

with open ("README.md","r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-summarizer-by-p"
AUTHOR_USER_NAME="Purav101"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL="puravsoni529@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version = __version__,
    author  = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description  = "A small python package for nlp app",
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls ={
        "Bug Tracker ": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    pakckages = setuptools.find_packages(where="src")
)



