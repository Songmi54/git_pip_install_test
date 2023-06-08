from setuptools import setup, find_packages

setup(
    name='MobilityCapstone1',
    version='0.0.1',
    description='DSC 공유대학 모빌리티캡스톤1 교통사고 유발요소 자동분석 시스템',
    author='songmi0504',
    author_email='songmi000504@gmail.com',
    url='https://github.com/Songmi54/git_pip_install_test.git',
    license='Songmi54',
    install_requires=['tensorflow', 'numpy', 'opencv'],
    packages=find_packages(exclude=[]),
    zip_safe=False
)