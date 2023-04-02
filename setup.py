from setuptools import setup
from pixelsorter import (__name__ as __package_name__, __doc__, __version__, __author__, __email__, __license__)

if __name__=="__main__":
    setup(
        name=__package_name__,
        version=__version__,
        description=__doc__,
        url='https://github.com/Blotz/pixel-sorter',
        author=__author__,
        author_email=__email__,
        license=__license__,
        packages=['pixelsorter'],
        install_requires=[
            'numpy',
            'opencv-python',
            'filetype'
        ],
        entry_points={
            'console_scripts': [
                'pixelsorter=pixelsorter.cli:main',
            ],
        },
        zip_safe=False,
    )
