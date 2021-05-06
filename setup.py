import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mo_module2",
    version="0.0.1",
    author="Oleksandr Pozden",
    author_email="oleksandr.pozden@gmail.com",
    description="Collection of numerical methods of unconditional minimazation tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OlexandrPozden/mo_module2.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)