from setuptools import setup

setup(
    name='ffpbar',
    version='0.0.1',
    author='AP-Atul',
    author_email='atulpatare99@gmail.com',
    packages=['ffpbar/'],
    url='https://github.com/AP-Atul/ffpbar',
    license='LICENSE',
    description='Progress bar for FFmpeg using tqdm.',
    long_description=open('README.md').read(),
    install_requires=[
        "tqdm"
    ],
)
