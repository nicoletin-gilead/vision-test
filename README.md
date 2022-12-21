vision-test
===============================================================================

A brief description of the project.

The goals of the vision-test are:

* a list of the core features of the project.

-------------------------------------------------------------------------------

Table of Contents
-----------------

1. [Overview][#1]

2. [Getting Started][#2]

   2.1. [Project Organization][#2.1]

   2.2. [Setting Up the Project][#2.2]

3. [Project Conventions][#3]

4. [Software Quick References][#4]

-------------------------------------------------------------------------------

## 1. Overview

A more detailed description of the project.

### References

* List of key project references

-------------------------------------------------------------------------------

## 2. Getting Started

### 2.1. Project Organization

```
├── README.md             <- this file
├── LICENSE               <- license for contents of the project
├── NOTICE                <- copyright notice for contents of the project
├── Makefile              <- Makefile containing useful shortcuts (`make`
│                            rules). Use `make help` to show the list of
│                            available rules.
├── Project.toml          <- Julia project configuration file (e.g., Julia
│                            package dependencies)
├── pyproject.toml        <- Python project metadata file (e.g., Python package
│                            dependencies)
├── poetry.lock           <- Poetry lockfile
├── bin/                  <- scripts and programs
├── data/                 <- project data. See "Project Conventions" section
│   │                        for data organization and processing conventions.
│   │
│   ├── final/            <- data directly used to generate key results
│   │                        (e.g., data for figures in reports)
│   ├── processed/        <- processed data that is ready for use
│   └── raw/              <- source data in its original format
├── docs/                 <- project documentation
│   │
│   ├── api/              <- source code documentation (generated by `make docs`)
│   └── references/       <- reference materials (e.g., research articles)
├── extras/               <- additional files and references that may be useful
│   │                        for the project
│   │
│   └── quick-references/ <- quick references for software tools that support
├── notebooks/            <- research notes and Jupyter notebooks. See "Project
│                            Conventions" section for notebook conventions.
├── reports/              <- research reports
├── src/                  <- project source code
└── tests/                <- project test code
```

### 2.2. Setting Up the Project

__Note__: this project uses `poetry` to manage Python package dependencies.

* ___Prerequisites___

  * Install [Git][git].

  * Install [Python][python] 3.8 (or greater). __Recommendation__: use `pyenv`
    to configure the project to use a specific version of Python.
  
  * Install [Julia][julia] 1.6 (or greater).
  
  * Install [Poetry][poetry] 1.2 (or greater).

   * _Optional_. Install [direnv][direnv].

* Set up a dedicated virtual environment for the project. Any of the common
  virtual environment options (e.g., `venv`, `direnv`, `conda`) should work.
  Below are instructions for setting up a `direnv` or `poetry` environment.

  __Note__: to avoid conflicts between virtual environments, only one method
  should be used to manage the virtual environment.

  * __`direnv` Environment__. __Note__: `direnv` manages the environment for
    both Python and the shell.

    * ___Prerequisite___. Install `direnv`.

    * Copy `extras/dot-envrc` to the project root directory, and rename it to
      `.envrc`.

      ```shell
      $ cd $PROJECT_ROOT_DIR
      $ cp extras/dot-envrc .envrc
      ```

    * Grant permission to direnv to execute the .envrc file.

      ```shell
      $ direnv allow
      ```

  * __`poetry` Environment__. __Note__: `poetry` only manages the Python
    environment (it does not manage the shell environment).

    * Create a `poetry` environment that uses a specific Python executable.
      For instance, if `python3` is on your `PATH`, the following command
      creates (or activates if it already exists) a Python virtual environment
      that uses `python3`.

      ```shell
      $ poetry env use python3
      ```

      For commands to use other Python executables for the virtual environment,
      see the [Poetry Quick Reference][poetry-quick-reference].

* Upgrade `pip` to the latest released version.

  ```shell
  $ pip install --upgrade pip
  ```

* Install the Python packages required for the project.

  ```shell
  $ poetry install
  ```

  __Note__. For virtual environments not created with `poetry` (e.g.,
  `direnv`), a system- or user-level installation of `poetry` might fail
  (e.g., if paths to Python packages required by `poetry` are missing from the
  `PYTHONPATH` environment variable in the virtual environment). To avoid
  having to manually modify `PYTHONPATH`, install `poetry` within the virtual
  environment before running `poetry install`:

  ```shell
  $ pip install poetry
  ```

* Set up the Julia environment.

  ```julia
  julia> ]

  (...) pkg> instantiate
  ```

* Download project data from remote storage.

  ```shell
  $ dvc pull
  ```

* Do research! Make discoveries! Advance knowledge!

-------------------------------------------------------------------------------

## 3. Project Conventions

### Guidelines for Organizing Data

* All data should be placed in the `data` directory.

* Data should be organized into the following subdirectories.

  * `raw`: source data in its original format. Data in this directiory data
    should never be modified.

  * `processed`: processed data that is ready for use. All data in this
    directory should be generated by a deterministic, automateable process
    (possibly multi-step) that uses ___only raw data___ as input.

  * `final`: data directly used to generate key results (e.g., data for figures
    in reports). All data in this directory should be generated by a
    deterministic, automateable process (possibly multi-step) that uses
    processed and/or raw data as input.

### Guidelines for Organizing `notebooks` Directory

* Depending on the nature of the project, it may be useful to organize the
  `notebooks` directory into sub-directories (e.g., by team member, by
  sub-project).

#### Research Notes

* Research notes should be placed in the `notebooks` directory and should
  be named using the following conventions:

  * `YYYY-MM-DD-AUTHOR_INITIALS-BRIEF_DESCRIPTION.md`

    or

  * `YYYY-MM-AUTHOR_INITIALS-Notes.md`

    where the year and month indicate the month that the notes were written.

  The time period covered by each set of research notes should be adjusted to
  match the pace of the project (which may change over time). For instance, if
  updates are made only a few times a year, it is reasonable to omit the month
  from the file name: `YYYY-AUTHOR_INITIALS-Notes.md`.

* When a non-trivial modification is made to an existing entry, the
  modification date should be indicated in a "last updated" line that
  immediately follows the entry header. For instance:

  `_Last Updated_: 2022-05-31`

#### Jupyter Notebooks

* Jupyter notebooks should be placed in the `notebooks` directory and should
  be named using the following convention:

  `YYYY-MM-DD-AUTHOR_INITIALS-BRIEF_DESCRIPTION.ipynb`

  where the date used for the notebook is approximately the date the original
  experiment was performed.

  * Example: `2019-01-17-KC-information_theory_analysis.ipynb`

* _Notebook Modifications_

  * When minor modifications are made to a notebook (e.g., code updates that
    do not materially change the results, addition of a few of related
    experiments), use a "History" block (in Markdown format) to document the
    changes. Example:

    ```markdown
    ### History

    #### 2022-05-31
    - Replaced `distplot()` with `histplot()` because `distplot()` has been deprecated.
    ```

  * When signification changes are made to a notebook (e.g., major
    modifications to algorithms, addition of experiments to explore a new
    direction), the modified notebook should saved to a new file with a name
    constructed from the modification date and the initials of the person who
    made the modifications.

-------------------------------------------------------------------------------

## 4. Software Quick References

* [Automated Testing][automated-testing]

* [FastDS Quick Reference][fastds-quick-reference]

* [Julia Quick Reference][julia-quick-reference]

* [Jupyter Quick Reference][jupyter-quick-reference]

* [MLflow Quick Reference][mlflow-quick-reference]

* [pdoc Quick Reference][pdoc-quick-reference]

* [pyenv Quick Reference][pyenv-quick-reference]

* [Poetry Quick Reference][poetry-quick-reference]

* [Project Environment][project-environment]

-------------------------------------------------------------------------------

[-----------------------------INTERNAL LINKS-----------------------------]: #

[#1]: #1-overview

[#2]: #2-getting-started
[#2.1]: #21-project-organization
[#2.2]: #22-setting-up-the-project

[#3]: #3-project-conventions
[#3.1]: #31-jupyter-notebook-conventions
[#3.2]: #32-guidelines-for-organizing-data

[#4]: #4-software-quick-references

[-----------------------------REPOSITORY LINKS-----------------------------]: #

[automated-testing]: extras/quick-references/Automated-Testing.md

[fastds-quick-reference]: extras/quick-references/FastDS-Quick-Reference.md

[julia-quick-reference]: extras/quick-references/Julia-Quick-Reference.md

[jupyter-quick-reference]: extras/quick-references/Jupyter-Quick-Reference.md

[mlflow-quick-reference]: extras/quick-references/MLflow-Quick-Reference.md

[pdoc-quick-reference]: extras/quick-references/pdoc-Quick-Reference.md

[pyenv-quick-reference]: extras/quick-references/pyenv-Quick-Reference.md

[poetry-quick-reference]: extras/quick-references/Poetry-Quick-Reference.md

[project-environment]: extras/quick-references/Project-Environment.md

[-----------------------------EXTERNAL LINKS-----------------------------]: #

[direnv]: https://direnv.net/

[git]: https://git-scm.com/

[julia]: https://julialang.org/

[python]: https://www.python.org/

[poetry]: https://python-poetry.org/
