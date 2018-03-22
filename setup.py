from setuptools import setup
import os,glob,warnings,sys,fnmatch

def recursive_glob(basedir, pattern):
    matches = []
    for root, dirnames, filenames in os.walk(basedir):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches

PACKAGENAME='snsedextend'
# Add the project-global data
pkgdatadir = os.path.join(PACKAGENAME, 'data')
data_files = []
data_files.extend(recursive_glob(pkgdatadir, '*'))
data_files = [f[len(PACKAGENAME)+1:] for f in data_files]

setup(
    name='surveySim',
    install_requires=['astropy','numpy','scipy','sncosmo'],
    author='Justin Pierel',
    packages=['surveySim'],
    author_email='jr23@email.sc.edu',
    package_data={'surveySim':data_files},
    version='0.0.5'
)
