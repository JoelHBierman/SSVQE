# This code is part of Qiskit.
#
# (C) Copyright IBM 2017.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"The Qiskit Terra setup file."

import os
import re
from setuptools import setup, find_packages


with open("requirements.txt") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name="ssvqe",
    version="0.1.0",
    description="An implementation of the Subspace Search Variational Quantum Eigensolver in Qiskit",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum",
    packages=find_packages(exclude=["test*"]),
    install_requires=REQUIREMENTS,
    include_package_data=True,
    python_requires=">=3.8",
    project_urls={
        "Bug Tracker": "https://github.com/Qiskit/qiskit-terra/issues",
        "Documentation": "https://qiskit.org/documentation/",
        "Source Code": "https://github.com/Qiskit/qiskit-terra",
    },
    options={"bdist_wheel": {"py_limited_api": "cp38"}},
    zip_safe=False,
)
