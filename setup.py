from setuptools import setup

setup(
    name='pydecdat',
    version='0.0.1',
    packages=['pydecdat'],
    extras_require={
        "gui": ["PyQt5==5.15.4"]
    },
    zip_safe=False,
    entry_points={
        "gui_scripts": "pydecdat=pydecdat.gui:main [gui]"
    }
)