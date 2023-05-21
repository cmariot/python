from setuptools import setup, find_packages

setup(
    name='my_minipack',
    description='Howto create a package in python.',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[],
    author='cmariot',
    author_email='cmariot@student.42.fr',
    license='GPLv3',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GPLv3 License',
        'Intended Audience :: Developers',
        'Intended Audience :: Students',
        'Topic :: Education',
        'Topic :: HowTo',
        'Topic :: Package',
    ],
)
