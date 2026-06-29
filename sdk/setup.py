from setuptools import setup, find_packages

setup(
    name="promptshield",
    version="1.0.0",
    author="Dhimahi Mehta",
    author_email="dhimahimehta01@gmail.com",
    description="Official Python SDK for PromptShield",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Dhimahi-T-Mehta/PromptShield",
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "promptshield=promptshield.cli:main",
        ],
    },
    install_requires=[
        "requests>=2.31.0",
    ],
    python_requires=">=3.9",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries",
    ],
)