from setuptools import setup, find_packages

setup(
    name="Linux_backport_tool",
    version="0.1",
    packages=find_packages(),
    author="Daniel Govnir",
    author_email="haveacar.zhovnir@gmail.com",
    description="Efficient Python-based solution for backporting changes from the recently updated C file to the old one",
    install_requires=[
        'annotated-types==0.6.0',
        'anyio==4.2.0',
        'certifi==2023.11.17',
        'charset-normalizer==3.3.2',
        'distro==1.9.0',
        'h11==0.14.0',
        'httpcore==1.0.2',
        'httpx==0.26.0',
        'idna==3.6',
        'pydantic==2.5.3',
        'pydantic-core==2.14.6',
        'sniffio==1.3.0',
        'tqdm==4.66.1',
        'typing-extensions==4.9.0',
        'urllib3==2.1.0',
    ],
    url ='https://www.daniel-govnir.com/',
)