from setuptools import setup

setup(
    name="python-snowtrace",
    version="1.1",
    description="A minimal, yet complete, python API for snowtrace.io.",
    url="https://github.com/EmperorMew/python-snowtrace",
    author="EmperorMew",
    author_email="info@ethmint.com",
    license="MIT",
    packages=[
        "etherscan",
        "etherscan.configs",
        "etherscan.enums",
        "etherscan.modules",
        "etherscan.utils",
    ],
    install_requires=["requests"],
    include_package_data=True,
    zip_safe=False,
)
