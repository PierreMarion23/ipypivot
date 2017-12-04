from __future__ import print_function

import os
import sys
import platform

from distutils.util import convert_path

from setuptools import setup, find_packages, Command
from setuptools.command.sdist import sdist
# from setuptools.command.bdist_wheel import bdist_wheel
from setuptools.command.build_py import build_py
from setuptools.command.egg_info import egg_info
from subprocess import Popen, PIPE, check_call

from setuptools.command.install import install

here = os.path.dirname(os.path.abspath(__file__))
node_root = os.path.join(here, 'js')
is_repo = os.path.exists(os.path.join(here, '.git'))

npm_path = os.pathsep.join([
    os.path.join(node_root, 'node_modules', '.bin'),
    os.environ.get('PATH', os.defpath),
])

from distutils import log
log.set_verbosity(log.DEBUG)
log.info('setup.py entered')
log.info('$PATH=%s' % os.environ['PATH'])

LONG_DESCRIPTION = 'A d3 based slider Jupyter Widget - for demo'


# def js_prerelease(command, strict=False):
#     """decorator for building minified js/css prior to another command"""
#     class DecoratedCommand(command):
#         def run(self):
#             jsdeps = self.distribution.get_command_obj('jsdeps')
#             log.info('/n/nis_repo =', is_repo)
#             if not is_repo and all(os.path.exists(t) for t in jsdeps.targets):
#                 log.info('regular sdist')
#                 # sdist, nothing to do
#                 command.run(self)
#                 return
#             log.info('NOT regular sdist')

#             try:
#                 self.distribution.run_command('jsdeps')
#             except Exception as e:
#                 missing = [t for t in jsdeps.targets if not os.path.exists(t)]
#                 if strict or missing:
#                     log.warn('rebuilding js and css failed')
#                     if missing:
#                         log.error('missing files: %s' % missing)
#                     raise e
#                 else:
#                     log.warn('rebuilding js and css failed (not a problem)')
#                     log.warn(str(e))
#             command.run(self)
#             update_package_data(self.distribution)
#     return DecoratedCommand


# def update_package_data(distribution):
#     """update package_data to catch changes during setup"""
#     build_py = distribution.get_command_obj('build_py')
#     # distribution.package_data = find_package_data()
#     # re-init build_py options which load package_data
#     build_py.finalize_options()


# class NPM(Command):

#     # description = 'install package.json dependencies using npm'
#     # user_options = []

#     node_modules = os.path.join(node_root, 'node_modules')
#     targets = [
#         os.path.join(here, 'widget_d3_slider', 'static', 'extension.js'),
#         os.path.join(here, 'widget_d3_slider', 'static', 'index.js')
#     ]

#     def initialize_options(self):
#         pass

#     def finalize_options(self):
#         pass

#     def get_npm_name(self):
#         npm_name = 'npm'
#         if platform.system() == 'Windows':
#             npm_name = 'npm.cmd'

#         return npm_name

#     def has_npm(self):
#         npm_name = self.get_npm_name()
#         try:
#             check_call([npm_name, '--version'])
#             return True
#         except:
#             return False

#     def should_run_npm_install(self):
#         # package_json = os.path.join(node_root, 'package.json')
#         # node_modules_exists = os.path.exists(self.node_modules)
#         # return self.has_npm()
#         return True

#     def run(self):
#         log.info('NPM start run')

#         has_npm = self.has_npm()
#         if not has_npm:
#             log.error(
#                 "`npm` unavailable.  If you're running this command using sudo, make sure `npm` is available to sudo")

#         env = os.environ.copy()
#         env['PATH'] = npm_path

#         if self.should_run_npm_install():
#             log.info(
#                 "Installing build dependencies with npm.  This may take a while...")
#             npm_name = self.get_npm_name()
#             check_call([npm_name, 'install'], cwd=node_root,
#                        stdout=sys.stdout, stderr=sys.stderr)
#             os.utime(self.node_modules, None)

#         for t in self.targets:
#             if not os.path.exists(t):
#                 msg = 'Missing file: %s' % t
#                 if not has_npm:
#                     msg += '\nnpm is required to build a development version of a widget extension'
#                 raise ValueError(msg)

#         # update package data in case this created new files
#         update_package_data(self.distribution)
#         log.info('NPM end run')


class CustomCommand(build_py):
    def run(self):
        # run npm to build static/ if not all target files are there

        def get_npm_name():
            return 'npm.cmd' if platform.system() == 'Windows' else 'npm'

        def has_npm(npm_name):
            try:
                check_call([npm_name, '--version'])
                return True
            except:
                return False

        targets = setup_args['data_files'][0][1]
        print('targets :', targets)
        if not all(os.path.exists(t) for t in targets):
            missing = [e for e in targets if not os.path.exists(e)]
            log.info('missing targets: {}'.format(missing))
            log.info('Need run npm install')

            cmd = '''
            cd js 
            npm install
            '''

            print('start cmd')

            process = Popen('/bin/bash', stdin=PIPE, stdout=PIPE)
            out, err = process.communicate(cmd.encode('utf-8'))
            print(out.decode('utf-8'))

            print('end cmd')

        else:
            log.info('All targets are there - No need for npm install')

        build_py.run(self)
        # build_py = self.distribution.get_command_obj('build_py')
        # build_py.finalize_options()


version_ns = {}
with open(os.path.join(here, 'widget_d3_slider', '_version.py')) as f:
    exec(f.read(), {}, version_ns)


meta_ns = {}
ver_path = convert_path(module + '/__meta__.py')
with open(ver_path) as ver_file:
    exec(ver_file.read(), meta_ns)


# ref https://packaging.python.org/tutorials/distributing-packages/
setup_args = {
    'name': 'widget_d3_slider',
    'version': version_ns['__version__'],
    'description': 'A Custom Jupyter Widget Library',
    'long_description': LONG_DESCRIPTION,
    'include_package_data': True,
    'data_files': [
        ('share/jupyter/nbextensions/jupyter-widget-d3-slider', [
            'widget_d3_slider/static/extension.js',
            'widget_d3_slider/static/index.js',
            'widget_d3_slider/static/index.js.map',
        ]),
    ],
    'install_requires': [
        'ipywidgets>=7.0.0',
    ],
    'packages': find_packages(),
    'zip_safe': False,
    'cmdclass': {
        'build_py': CustomCommand
    },
    # 'cmdclass': {
    # 'build_py': js_prerelease(build_py),
    # 'egg_info': js_prerelease(egg_info),
    # 'sdist': js_prerelease(sdist, strict=True),
    # 'jsdeps': NPM,
    # },

    'author': 'oscar6echo',
    'author_email': 'olivier.borderies@gmail.com',
    'url': 'https://github.com/oscar6echo/jupyter-widget-d3-slider',
    'keywords': [
        'ipython',
        'jupyter',
        'widgets',
    ],
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Multimedia :: Graphics',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
}


# run standard setup
setup(**setup_args)


# superfluous MANIFEST.in
# recursive-include widget_d3_slider/static *.*
