from setuptools import setup, find_packages

setup(
    name='croco',
    version='1.0.0',
	packages=find_packages(),
	install_requires=[
		'torch',
		'numpy',
		'einops',
	]
)