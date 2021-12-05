from setuptools import setup

PACKAGE_NAME = 'kbtdd'

setup(
    # metadata
    name=PACKAGE_NAME,

    # options
    packages=[PACKAGE_NAME],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.8',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=3',
        ],
    },
    entry_points='''
        [console_scripts]
        {app}={pkg}.cli:main
    '''.format(app=PACKAGE_NAME.replace('_', '-'), pkg=PACKAGE_NAME),
)