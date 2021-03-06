from setuptools import find_packages, setup
setup(
    name='AlgoFunc',
    packages=find_packages(include=['algofunc']),
    version='0.1.0',
    description='A library of algorithm functions for Python',
    author='Alec Nazworth',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)