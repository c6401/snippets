from distutils.core import setup

setup(
    name='...',
    version='0.0.1',
    description='...',
    long_description=open('README.md').read(),
    author='...',
    author_email='...',
    url='https://github.com/',
    license='MIT',
    packages=['...'],
    install_requires=[
        '...',
    ],
    scripts=['...'],
    entry_points = {
        'console_scripts': [
            'commandmane = package:main',
        ],
    },
)
