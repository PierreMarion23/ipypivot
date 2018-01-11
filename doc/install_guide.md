# Installation Guide

This is a step by step guide to install, enable and publish the [ipywidget](https://ipywidgets.readthedocs.io/en/stable/) `jupyter-widget-pivot-table`.

## 1 - Installation

To install use pip and npm:

    $ git clone https://github.com/PierreMarion23/pivot-table-widget.git
    $ cd jupyter_widget_pivot_table/js
    $ npm install
    $ cd ..
    $ pip install .
    $ jupyter nbextension enable --py --sys-prefix jupyter_widget_pivot_table


For a development installation:

    $ git clone https://github.com/PierreMarion23/pivot-table-widget.git
    $ cd jupyter_widget_pivot_table/js
    $ npm install
    $ cd ..
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix jupyter_widget_pivot_table
    $ jupyter nbextension enable --py --sys-prefix jupyter_widget_pivot_table

## 2 - Paths

All the paths directly from a macOS system (with [Anaconda](https://www.anaconda.com/what-is-anaconda/) installed with [brew](https://brew.sh/)) where sys.prefix = `/usr/local/anaconda3`.  
It should be relatively easy to translate in other systems.  


To check where jupyter install extensions:

    $ jupyter --paths
    config:
        /Users/Olivier/.jupyter
        /usr/local/anaconda3/etc/jupyter
        /usr/local/etc/jupyter
        /etc/jupyter
    data:
        /Users/Olivier/Library/Jupyter
        /usr/local/anaconda3/share/jupyter
        /usr/local/share/jupyter
        /usr/share/jupyter
    runtime:
        /Users/Olivier/Library/Jupyter/runtime

The flag `--sys-prefix` means extension are installed in this data folder:

    /usr/local/anaconda3/share/jupyter

There you can see a `jupyter-widget-pivot-table` folder or symlink back to the source folder `static/`.  
For example:

    drwxr-xr-x  4 Olivier  staff   136B Sep 30 18:09 jupyter-js-widgets/
    drwxr-xr-x  5 Olivier  staff   170B Oct  3 02:42 jupyter-widget-pivot-table/

To check nbextensions are properly install and enabled, for example:

    $ jupyter nbextension list
    Known nbextensions:
    config dir: /Users/Olivier/.jupyter/nbconfig
        notebook section
        codefolding/main  enabled 
        - Validating: OK
        comment-uncomment/main  enabled 
        - Validating: OK
        default_style/main  enabled 
        - Validating: OK
    config dir: /usr/local/anaconda3/etc/jupyter/nbconfig
        notebook section
        jupyter-js-widgets/extension  enabled 
        - Validating: OK
        jupyter-widget-pivot-table/extension  enabled 
        - Validating: OK


## 3 - Commands

### 3.1 - `npm install`

It is run from folder `js/` which contains the js+css **source code**.  
It performs the following:
+ Download the node modules mentioned in fields `dependencies` and `devDependencies` in npm config file `package.json`.
+ Run `webpack` according to config file `webpack.config.js`

The first step is the `npm install` command per se.  
The second is the `prepare` command as defined in `package.json`. And `npm prepare` is automatically executed after npm install as explained in the [official doc](https://docs.npmjs.com/misc/scripts).

The result is the creation of folders `js/dist` and `jupyter_widget_pivot_table/static` containing compiled javascript from source code in folder `js/`.

### 3.2 - `pip install`

The full command is:
```bash
# regular install from folder containing setup.py
$ pip install .

# dev install from folder containing setup.py
$ pip install -e .
```

This command must be run **AFTER** the folder `static/` was created.

It is a standard `pip install` command:
+ The source files and egg-info are copied to `/usr/local/anaconda3/lib/python3.6/site-packages`
+ The files in folder `static/` are copied to `share/jupyter/nbextensions/jupyter-widget-pivot-table`
+ Note that for a **dev install**:
    + An `egg-link` file links back to the source folder
    + No file is copied to the folder `nbextensions/jupyter-widget-pivot-table`
    + Thanks to the `--symlink`, during dev, you just need to restart the kernel to take into account any modification in the Python code!

### 3.3 - `jupyter nbextension (install|uninstall)`

The full command is:
```bash
$ jupyter nbextension (install|uninstall) --py [--symlink] --sys-prefix jupyter_widget_pivot_table
```

It copies [create symlinks] resp. removes `static/` files to resp. from the nbextension data folder `share/jupyter/nbextensions/jupyter-widget-pivot-table` and adds resp. removes lines in config file `notebook.json` in config directory `/usr/local/anaconda3/etc/jupyter`.

The config file `notebook.json` contains the following:

    {
        "load_extensions": {
            "jupyter-js-widgets/extension": true,
            "jupyter-widget-pivot-table/extension": true
        }
    }


### 3.4 - `jupyter nbextension (enable|disable)`

The full command is:
```bash
$ jupyter nbextension (enable|disable) --py --sys-prefix jupyter_widget_pivot_table
```

It sets to true resp. false the `jupyter-widget-pivot-table/extension` line in config file `notebook.json` in config directory `/usr/local/anaconda3/etc/jupyter`.

### 3.5 - `npm run prepare`

The full command is:
```bash
# from folder js/
$ npm run prepare
```
It is a script (which simply calls `webpack`) in npm config file `package.json`.  

In an active dev activity (in the folder `js/`) substitute `npm install` by `npm run prepare` as there is no need to reload node_modules from the internet or even to get them from the local npm cache (located in `~/.npm`)

This re-compile the source js folder into `static/`. The symlinks bring back from `share/jupyter/nbextensions/jupyter-widget-pivot-table` to `js/static/`. So just reload the notebook. The new js is available instantly !

### 3.6 - `npm run watch`

To automate the build (i.e. running webpack) process start `npm run watch`.  
It will run in the background and trigger `npm run prepare` each time any change occurs in the `js/lib/` folder.  

## 4 - Publish on PyPI 

A few comments on the release process are available in the RELEASE.md file. Below is our experience on the matter of publishing on PyPI:

In order to publish a first version of your widget on PyPI:
+ Create an account on [PyPI](https://pypi.python.org/pypi?%3Aaction=register_form)
+ `pip install twine` (if not already installed)
+ `python setup.py sdist`
+ `twine upload dist/*`

To upload a new version of your widget:
+ change version in `jupyter_widget_pivot_table/_version.py`
+ delete `dist`
+ `python setup.py sdist`
+ `twine upload dist/*`

The full documentation can be found [here](https://packaging.python.org/tutorials/distributing-packages/).

