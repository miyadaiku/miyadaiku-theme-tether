#!/usr/bin/env python3
import pathlib
from miyadaiku import setuputils

DIR = pathlib.Path(__file__).resolve().parent

srcdir = DIR / 'node_modules/tether/dist/js'
destdir = DIR / 'miyadaiku_theme_tether/externals/js'
copy_files = [[srcdir, ['*.js'], destdir]]

setuputils.copyfiles(copy_files)
