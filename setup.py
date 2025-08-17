import setuptools
from pathlib import Path

here = Path(__file__).parent
long_description = (here / 'README.md').read_text()

setuptools.setup(
    name='ipynbname',
    version='2024.1.0.0',
    author='Mark McPherson',
    author_email='msm1089@yahoo.co.uk',
    description='Simply returns either notebook filename or the full path to the notebook when run from Jupyter notebook in browser.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='MIT',
    keywords='jupyter notebook filename'.split(),
    url='https://github.com/msm1089/ipynbname',
    packages=setuptools.find_packages(),
    package_data={},
    install_requires=['ipykernel'],
    python_requires='>=3.4, <4',
    classifiers=[
        'Operating System :: OS Independent',
        'Development Status :: 4 - Beta',
        'Framework :: Jupyter',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License'
    ]
)
