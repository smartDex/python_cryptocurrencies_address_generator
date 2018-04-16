from setuptools import setup, find_packages

setup(
    name='cryptocurrency-wallet-generator',
    packages=find_packages(),
    version='0.0.7',
    url='https://github.com/smartDex/python_cryptocurrencies_address_generator',
    author='vladislav Burov',
    author_email='burvvladislav@gmail.com',
    description='Simple Python package that can generate wallets for several cryptocurrencies',
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    install_requires=[
        'ecdsa==0.13',
        'ethereum==2.1.0',
    ],
)
