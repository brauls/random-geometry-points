from os import path
from setuptools import setup

README_PATH = path.join(path.abspath(path.dirname(__file__)), 'README.md')
LONG_DESCRIPTION = open(README_PATH, encoding='utf-8').read()

setup(
    name="random_geometry_points",
    version="1.1.2",
    description="Library to generate random points (2D or 3D) on geometry surfaces",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/brauls/random-geometry-points",
    author="Benedikt Rauls",
    author_email="brauls101@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="geometry random points 2D 3D",
    project_urls={
        "Source": "https://github.com/brauls/random-geometry-points",
        "Tracker": "https://github.com/brauls/random-geometry-points/issues",
    },
    packages=["random_geometry_points"],
    install_requires=[],
    python_requires='>=3.6',
)
