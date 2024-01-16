import os

import numpy
from setuptools import Extension


def configuration():
    config = dict(name = "metrics",
                  ext_modules=[
                      Extension("_confusion_matrix",
                         sources=["_confusion_matrix.pyx"],
                         include_dirs=[numpy.get_include()],
                         extra_compile_args=["-O3"]),
                    Extension("_classification_performance_evaluator",
                         sources=["_classification_performance_evaluator.pyx"],
                         include_dirs=[numpy.get_include()],
                         extra_compile_args=["-O3"])])

    return config


if __name__ == "__main__":
    from setuptools import setup
    setup(**configuration())
