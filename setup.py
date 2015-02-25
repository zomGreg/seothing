from setuptools import setup
 
APP = ['seothing.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True}
OPTIONS = {
    'argv_emulation': True,
    'packages': ['mechanize', 'bs4']
    }

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
