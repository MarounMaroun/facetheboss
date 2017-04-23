from setuptools import setup

with open('requirements.txt') as f:
    reqs = f.read().splitlines()

setup(
    name='facetheboss',
    version='0.1',
    packages=['faceboss'],
    entry_points={
        'console_scripts': [
            'faceboss=faceboss.faceboss:main',
        ],
    },
    install_requires=reqs
)
