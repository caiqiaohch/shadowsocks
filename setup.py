from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()

setup(
    name="shadowsocks",
    version="2.3",
    license='MIT',
    description="A fast tunnel proxy that help you get through firewalls",
    author='caiqiaohch',
    author_email='caiqiaohch@163.com',
    url='https://github.com/caiqiaohch/shadowsocks',
    packages=['shadowsocks', 'shadowsocks.crypto'],
    package_data={
        'shadowsocks': ['README.rst', 'LICENSE']
    },
    install_requires=[],
    entry_points="""
    [console_scripts]
    sslocal = shadowsocks.local:main
    ssserver = shadowsocks.server:main
    """,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: Proxy Servers',
    ],
    long_description=long_description,
)
