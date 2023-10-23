from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name='viphoneme',
    version='3.0.0',    
    description='Python package for convert text to phoneme ipa, use for cross language embedding Text-to-speech Reseach',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/v-nhandt21/Viphoneme',
    author='AILAB',
    author_email='dotrinhan99@gmail.com',
    license='AILAB',
    packages=['viphoneme'],
    include_package_data=True,
    install_requires=[],

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: Free for non-commercial use',
        'Natural Language :: Vietnamese',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: C++',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],  
)