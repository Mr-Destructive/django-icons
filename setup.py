import pathlib

from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()


setup(
    name="django-icons",
    zip_safe=False,
    version="21.3",
    description="Icons for Django",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/zostera/django-icons",
    author="Dylan Verheul",
    author_email="dylan@dyve.net",
    license="BSD-3-Clause",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Django>=2.2",
        'importlib-metadata<3; python_version<"3.8"',
    ],
)
