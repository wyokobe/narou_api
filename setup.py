import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="narou_api",
    version="0.0.2",
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'narou_api=narou_api:main',
        ],
    },
    author="wyokobe",
    author_email="wyokobe@gmail.com",
    description="unofficial syosetu.com api library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wyokobe/narou_api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
