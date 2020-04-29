import pathlib
from setuptools import setup, find_packages
from miyadaiku import setuputils

DIR = pathlib.Path(__file__).resolve().parent

srcdir = DIR / 'node_modules/tether/dist/js'
destdir = DIR / 'miyadaiku_theme_tether/externals/js'
copy_files = [[srcdir, ['*.js'], destdir]]

setup(
    cmdclass={'copy_files': setuputils.copy_files},
    copy_files=copy_files,
)
