import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='XTConnect',
    version='1.0.1',
    author='Shoeb Shah',
    author_email='shoebshah064@gmail.com',
    description='XTConnect API wrapper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/shoebshah64/XTConnect',
    project_urls = {
        "Bug Tracker": "https://github.com/shoebshah64/XTConnect/issues"
    },
    license='MIT',
    packages=['XTConnect'],
    install_requires=[
        'bidict',
        'certifi',
        'chardet',
        'idna',
        'python-engineio==3.14.2',
        'python-socketio==4.6.0',
        'requests',
        'six',
        'urllib3',
        'websocket-client'
        ],
)
#pip install python-engineio==3.14.2 python-socketio==4.6.0
