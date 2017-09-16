

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name="p3-bittrex",
    packages=["p3-bittrex"],
    version="0.1.0",
    description="Bittrex API pacakge",
    author="Andy Hsieh",
    author_email="andy.hsieh@hotmail.com",
    license='LICENSE',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
        'Topic :: Office/Business :: Financial',
    ],
    install_requires=[
        "requests >= 2.18.3",
    ],
    long_description="""\
    Pybittrex is a bittrex API pacakge.
    -----------------------------------------
    This version requires Python3 or later;
    """

)
