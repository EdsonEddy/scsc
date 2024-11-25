from setuptools import setup

setup(
    name="pysimchecker",
    version="1.0.0",
    package_dir={'': 'src'},
	py_modules=["code_preprocessor", "constants", "file_utils", "main", "pycode_similar", "pysimchecker", "similarity", "union_find"],
    install_requires=[
        "pygments",
        "zss",
    ],
    author="Eddy Lecoña",
    author_email="crew0eddy@gmail.com",
    description="A tool for analyzing code snippets and detecting similarities",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/EdsonEddy/pysimchecker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
    ],
    keywords="code analysis, similarity detection, plagiarism detection, code snippets, code comparison",
    project_urls={
        "Bug Tracker": "https://github.com/EdsonEddy/pysimchecker/issues",
        "Documentation": "https://github.com/EdsonEddy/pysimchecker/wiki",
        "Source Code": "https://github.com/EdsonEddy/pysimchecker",
    },
    python_requires='>=3.9',
	platforms=["All"],
    entry_points={
        'console_scripts': [
            'pysimchecker=main:main',
        ],
    },
)