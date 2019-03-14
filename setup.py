#!/usr/bin/python3

from distutils.core import setup
import os

dir = os.path.dirname(__file__)
path_to_main_file = os.path.join(dir, "pypipackagetosrpmmod/__init__.py")
path_to_readme = os.path.join(dir, "README.md")
for line in open(path_to_main_file):
	if line.startswith('__version__'):
		version = line.split()[-1].strip("'").strip('"')
		break
else:
	raise ValueError('"__version__" not found in "pypipackagetosrpmmod/__init__.py"')
readme = open(path_to_readme).read(-1)

classifiers = [
'Development Status :: 4 - Beta',
'Environment :: Console',
'Environment :: No Input/Output (Daemon)',
'Intended Audience :: End Users/Desktop',
'Intended Audience :: System Administrators',
'License :: OSI Approved :: GNU General Public License (GPL)',
'Operating System :: POSIX :: Linux',
'Programming Language :: Python :: 2',
'Programming Language :: Python :: 3',
'Programming Language :: Python :: 2.7',
'Programming Language :: Python :: 3.6',
]

setup(
	name = 'pypipackage-to-srpm',
	version=version,
	description = 'Automate the creation of source and binary RPM packages out of source packages downloaded from PyPI',
	long_description = readme,
	author='Manuel Amador (Rudd-O)',
	author_email='rudd-o@rudd-o.com',
	license="GPL",
	url = 'http://github.com/Rudd-O/pypipackage-to-srpm',
	packages=['pypipackagetosrpmmod'],
	classifiers = classifiers,
	scripts = ["pypipackage-to-srpm", "pip-discover-deps"],
	keywords = "packaging",
	zip_safe=False,
)
