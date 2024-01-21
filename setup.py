from setuptools import find_packages, setup


def get_version():
    """Gets the rwkit version."""
    path = "rwpyt/__init__.py"
    with open(path) as file:
        lines = file.readlines()

    for line in lines:
        if line.startswith("__version__"):
            return line.strip().split()[-1].strip().strip('"')
    raise RuntimeError("bad version data in __init__.py")


setup(
    name="rwpyt",
    version=get_version(),
    description="A clean code base for reward learning.",
    author="Yi-Chen Li",
    author_email="ychenli.X@gmail.com",
    url="https://github.com/BepfCp/Reward-pytorch",
    packages=find_packages(include=["rwkit*"]),
    python_requires="<3.11,>=3.7",
    install_requires=[
        "gymnasium[all]",
        "hydra-core==1.3.2",
        "numpy",
        "omegaconf==2.3.0",
        "setuptools",
        "torch",
        "tqdm",
        "rlplugs @ git+https://github.com/BepfCp/rlplugs@main",
    ],
)
