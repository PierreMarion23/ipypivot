# Installation Guide

This is a step by step guide to install, enable and publish the [ipywidget](https://ipywidgets.readthedocs.io/en/stable/) `ipypivot`.

## 1 - Installation

To install use pip and npm:

    $ git clone https://github.com/PierreMarion23/ipypivot.git
    $ cd ipypivot/js
    $ npm install
    $ cd ..
    $ pip install .
    $ jupyter nbextension enable --py --sys-prefix ipypivot


For a development installation:

    $ git clone https://github.com/PierreMarion23/ipypivot.git
    $ cd ipypivot/js
    $ npm install
    $ cd ..
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix ipypivot
    $ jupyter nbextension enable --py --sys-prefix ipypivot

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

There you can see a `ipypivot` folder or symlink back to the source folder `static/`.  
For example:

    drwxr-xr-x  4 Olivier  staff   136B Sep 30 18:09 jupyter-js-widgets/
    drwxr-xr-x  5 Olivier  staff   170B Oct  3 02:42 ipypivot/

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
        ipypivot/extension  enabled 
        - Validating: OK


## 3 - Commands

### 3.1 - `npm install`

It is run from folder `js/` which contains the js+css **source code**.  
It performs the following:
+ Download the node modules mentioned in fields `dependencies` and `devDependencies` in npm config file `package.json`.
+ Run `webpack` according to config file `webpack.config.js`

The first step is the `npm install` command per se.  
The second is the `prepare` command as defined in `package.json`. And `npm prepare` is automatically executed after npm install as explained in the [official doc](https://docs.npmjs.com/misc/scripts).

The result is the creation of folders `js/dist` and `ipypivot/static` containing compiled javascript from source code in folder `js/`.

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
+ The files in folder `static/` are copied to `share/jupyter/nbextensions/ipypivot`
+ Note that for a **dev install**:
    + An `egg-link` file links back to the source folder
    + No file is copied to the folder `nbextensions/ipypivot`
    + Thanks to the `--symlink`, during dev, you just need to restart the kernel to take into account any modification in the Python code!

### 3.3 - `jupyter nbextension (install|uninstall)`

The full command is:
```bash
$ jupyter nbextension (install|uninstall) --py [--symlink] --sys-prefix ipypivot
```

It copies [create symlinks] resp. removes `static/` files to resp. from the nbextension data folder `share/jupyter/nbextensions/ipypivot` and adds resp. removes lines in config file `notebook.json` in config directory `/usr/local/anaconda3/etc/jupyter`.

The config file `notebook.json` contains the following:

    {
        "load_extensions": {
            "jupyter-js-widgets/extension": true,
            "ipypivot/extension": true
        }
    }


### 3.4 - `jupyter nbextension (enable|disable)`

The full command is:
```bash
$ jupyter nbextension (enable|disable) --py --sys-prefix ipypivot
```

It sets to true resp. false the `ipypivot/extension` line in config file `notebook.json` in config directory `/usr/local/anaconda3/etc/jupyter`.

### 3.5 - `npm run prepare`

The full command is:
```bash
# from folder js/
$ npm run prepare
```
It is a script (which simply calls `webpack`) in npm config file `package.json`.  

In an active dev activity (in the folder `js/`) substitute `npm install` by `npm run prepare` as there is no need to reload node_modules from the internet or even to get them from the local npm cache (located in `~/.npm`)

This re-compile the source js folder into `static/`. The symlinks bring back from `share/jupyter/nbextensions/ipypivot` to `js/static/`. So just reload the notebook. The new js is available instantly !

### 3.6 - `npm run watch`

To automate the build (i.e. running webpack) process start `npm run watch`.  
It will run in the background and trigger `npm run prepare` each time any change occurs in the `js/lib/` folder.  

## 4 - Publish


In addition to a regular Python packages, the Javascript part can be published too.  
The latter is useful only to use jupyter widgets in a non-notebook context.  

### 4.1 - Publish new version of ipypivot on PyPI

```bash
# Update version in __meta__.py
# git add and commit and push

# from top folder
python setup.py sdist upload -r pypi

# tag version
git tag -a X.X.X -m 'comment'
git push --tags
```


### 4.2 - Publish new version of ipypivot on NPM


```bash
# from js/ folder

# clean out the dist/ and node_modules/ folders
# for example to remove any git untracked file/folder: 
# git clean -fdx

# Update version in package.json

npm install

# test run to see what you will publish
# npm pack

# before publishing
# create a user if necessary 
# login npm
# ref: https://docs.npmjs.com/getting-started/publishing-npm-packages

npm publish

# check out the result on https://www.npmjs.com/
```
