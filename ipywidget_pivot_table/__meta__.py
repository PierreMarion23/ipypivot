
def _get_version(version_info):
    dic = {'alpha': 'a',
           'beta': 'b',
           'candidate': 'rc',
           'final': ''}
    vi = version_info
    specifier = '' if vi[3] == 'final' else dic[vi[3]] + str(vi[4])
    version = '%s.%s.%s%s' % (vi[0], vi[1], vi[2], specifier)
    return version


# meta data

__name__ = 'jupyter_widget_pivot_table'
name_url = __name__.replace('_', '-')

version_info = (0, 1, 3, 'final', 0)
__version__ = _get_version(version_info)

__description__ = 'Jupyter Widget wrapping pivottable.js'
__long_description__ = 'See repo README'
__author__ = 'oscar6echo'
__author_email__ = 'olivier.borderies@gmail.com'
__url__ = 'https://github.com/{}/{}'.format(__author__,
                                            name_url)
__download_url__ = 'https://github.com/{}/{}/tarball/{}'.format(__author__,
                                                                name_url,
                                                                __version__)
__keywords__ = ['jupyter-widget', 'pivottable', 'javascript']
__license__ = 'MIT'
__classifiers__ = ['Development Status :: 4 - Beta',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'
                   ]
__include_package_data__ = True
__data_files__ = [
    ('share/jupyter/nbextensions/jupyter-widget-pivot-table', [
        'jupyter_widget_pivot_table/static/extension.js',
        'jupyter_widget_pivot_table/static/index.js',
        'jupyter_widget_pivot_table/static/index.js.map',
    ]),
]
__package_data__ = {
    'api':
    ['api/pivot.json',
     'api/pivotui.json',
     ],
    'data':
    ['data/iris.csv',
     'data/mps.csv',
     'data/tips.csv',
     'data/weather.csv',
     ],
    'markdown':
    ['markdown/pivotui.md',
     ],
}

__zip_safe__ = False
