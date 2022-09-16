from setuptools import setup

setup(
    name='ep-lt28ga-subplate-fit',
    version='0.0.1',
    description='surface_fit wrapper',
    author='Jennings Zhang',
    author_email='Jennings.Zhang@childrens.harvard.edu',
    url='https://github.com/FNNDSC/ep-lt28ga-subplate-fit',
    py_modules=['lt28ga_surface_fit'],
    scripts=['surface_fit_script.pl'],
    install_requires=['chris_plugin'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'lt28ga_surface_fit = lt28ga_surface_fit:main'
        ]
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ],
    extras_require={
        'none': [],
        'dev': [
            'pytest~=7.1'
        ]
    }
)
