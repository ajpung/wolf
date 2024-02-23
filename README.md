# WOLF
A **W**aveform **O**peration and **L**ayering **F**ramework

# Introduction
The goal of the WOLF toolkit is to build a means for ingesting, changing, and exploring sound alteration. Notes and commands used to contribute are contained in the documentation.

# Before running
Ensure your Python path is set to the local repository's source directory using:
`export PYTHONPATH=<path to repo>/src:$PYTHONPATH`.

# Documentation
Initially, documentation can be read from within the repository's `docs` folder,
found in: `<repository>/docs/build/index.html`. If `index.html` does not exist
yet, use the following two commands then try locating the `index.html` file.

```
python -m pip install ".[docs]" 
sphinx-build docs/source docs/build
```


# Installation
```
python -m pip install --upgrade pip setuptools wheel numpy
python -m pip install .[dev]
```

# Running the tool
(Needs completion)