# -*- coding: utf-8 -*-
from setuptools import setup

packages = ['fuzzy_lightning']

package_data = {'': ['*'], 'fuzzy_lightning': ['cpp/*']}

install_requires = [
    'pybind11>=2.6.0',
    'scikit-learn>=1.0.2',
    'scipy>=1.7.0',
    'sparse-dot-topn>=0.3.1',
]

setup_kwargs = {
    'name': 'fuzzy-lightning',
    'version': '0.1.3',
    'description': 'Perform fast approximate string matching.',
    'long_description': '#fuzzy-lightning\nFast approximate string matching.\n',
    'author': 'Tom Matthews',
    'author_email': 'tomukmatthews@gmail.com',
    'maintainer': 'Tom Matthews',
    'maintainer_email': 'tomukmatthews@gmail.com',
    'url': 'https://github.com/tomukmatthews/fuzzy-lightning',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8.1,<4.0.0',
}
from build import build

build(setup_kwargs)

setup(**setup_kwargs)
