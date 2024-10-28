# Copyright (c) 2017 Salas Lin (leVirve)
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

from setuptools import setup, find_packages


def version():
    with open('onegan/__init__.py') as f:
        for line in f:
            if line.startswith('__version__'):
                return line.replace("'", '').split()[-1]


def pip_requirements():
    return [
        'torchvision==0.15.2',
        'tensorboardX==2.6.2.2',
        'tqdm==4.66.5',
        'PyYAML==6.0.2',
    ]


setup(
    name='onegan',
    version=version(),
    url='http://github.com/leVirve/OneGAN',
    description='One GAN framework for fast development setups.',
    author='Salas Lin (leVirve)',
    author_email='gae.m.project@gmail.com',
    license='MIT',
    platforms='any',
    packages=find_packages(),
    zip_safe=False,
    keywords='GAN framework',
    install_requires=[
        *pip_requirements(),
        'numpy==1.26.4',
        'scipy==1.14.1',
        # 'opencv',
        'pillow==9.5.0',
        'torch==2.0.1'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Customer Service',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6'
    ]
)
