import os
import re
import pathlib
from setuptools import setup, find_packages
from miyadaiku.common import setuputils

DIR = pathlib.Path(__file__).resolve().parent
os.chdir(DIR)

requires = [
    "miyadaiku"
]

srcdir = 'node_modules/tether/dist/js'
destdir = 'miyadaiku/themes/tether/externals/js'
copy_files = [[srcdir, ['*.js'], destdir]]
versionpy = DIR / 'miyadaiku/themes/tether/__version__.py'
version = re.search(r'"([\d.]+)"', versionpy.read_text())[1]

setup(
    name="miyadaiku.themes.tether",
    version=version,
    author="Atsuo Ishimoto",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description='Tether files for miyadaiku static site generator',
    long_description=setuputils.read_file(DIR, 'README.rst'),
    url='https://github.com/miyadaiku/miyadaiku-themes-tether',
    project_urls={
        'Miyadaiku': 'https://miyadaiku.github.io/',
    },

    packages=list(setuputils.list_packages(DIR, 'miyadaiku')),
    package_data={
        '': setuputils.SETUP_FILE_EXTS,
    },
    install_requires=requires,
    include_package_data=True,
    zip_safe=False,
    cmdclass={'copy_files': setuputils.copy_files},
    copy_files=copy_files,
)
