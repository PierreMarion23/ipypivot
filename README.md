# pivot-table-widget

## 1 - Installation

Before install, create a conda env with jupyter installed in it (for ex. from the env.yml file). See below (point 4) for more info about conda + jupyter.

Regular install:

    $ pip install pivot_table_widget
    $ jupyter nbextension enable --py --sys-prefix pivot_table_widget


Dev install - requires npm:

    $ git clone https://gitlab.com/oscar6echo/pivot-table-widget.git
    $ cd pivot-table-widget/js
    $ npm install
    $ cd ..
    $ pip install -e .
    $ jupyter nbextension install --py --symlink --sys-prefix pivot_table_widget
    $ jupyter nbextension enable --py --sys-prefix pivot_table_widget


## 2 - Paths

All the paths directly from my system (macOS with [Anaconda](https://www.anaconda.com/what-is-anaconda/) installed with [brew](https://brew.sh/)) where sys.prefix = `/usr/local/anaconda3`.  
It should be relatively easy to translate in yours.  


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

There you can see a `widget-d3-slider` folder or symlink back to the source folder `static/`.  
For example:

    drwxr-xr-x  4 Olivier  staff   136B Sep 30 18:09 jupyter-js-widgets/
    drwxr-xr-x  5 Olivier  staff   170B Oct  3 02:42 widget-d3-slider/

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
        widget-d3-slider/extension  enabled 
        - Validating: OK

## 3 - Commands

### 3.1 - `npm install`

It is run from folder `js/` which contains the js+css **source code**.  
It performs the following:
+ Download the node modules mentioned in fields `dependencies` and `devDependencies` in npm config file `package.json`.
+ Run `webpack` according to config file `webpack.config.js`

The outcome is the creation of folders `js/dist` and `widget_d3_slider/static` containing compiled javascript from source code in folder `js/`.

### 3.2 - `pip install`

The full command is:
```bash
# regular install from folder js/
$ pip install .

# dev install from folder js/
$ pip install -e .
```

This command must be run **AFTER** the folder `static/` was created.

It takes place in a standard fashion:
+ The source files and egg-info are copied to `/usr/local/anaconda3/lib/python3.6/site-packages`
+ The files in folder `static/` are copied to `share/jupyter/nbextensions/jupyter-drawing-pad`
+ Note that for a **dev install**:
    + An `egg-link` links back to the source folder
    + No file is copied to the folder `nbextensions/jupyter-drawing-pad`

### 3.2 - `jupyter nbextension (install|uninstall)`

The full command is:
```bash
$ jupyter nbextension (install|uninstall) --py [--symlink] --sys-prefix jupyter_drawing_pad
```

It copies [create symlinks] resp. removes `static/` files to resp. from the nbextension data folder `share/jupyter/nbextensions/jupyter-drawing-pad` and adds resp. removes lines in config file `notebook.json` in config directory `/usr/local/anaconda3/etc/jupyter`.

The config file `notebook.json` contains the following:

    {
        "load_extensions": {
            "jupyter-js-widgets/extension": true,
            "jupyter-drawing-pad/extension": true
        }
    }


### 3.3 - `jupyter nbextension (enable|disable)`

The full command is:
```bash
$ jupyter nbextension (enable|disable) --py --sys-prefix widget_d3_slider
```

It sets to true resp. false the `widget-d3-slider/extension` line in config file `notebook.json` in config directory `/usr/local/anaconda3/etc/jupyter`.

### 3.4 - `npm prepare`

The full command is:
```bash
# from folder js/
$ npm run prepare
```
It is a script (which simply calls `webpack`) in npm config file `package.json`.  

In an active dev activity (in the folder `js/`) substitute `npm install` by `npm prepare` as there is no need to reload node_modues from the internet or even to get them from the local npm cache (located in `~/.npm`)

This re-compile the source js folder into `static/`. The symlinks bring back from `share/jupyter/nbextensions/jupyter-drawing-pad` to `js/static/`. So just reload the notebook. The new js is available instantly !

### 3.5 - `npm watch`

The full command is:
```bash
# from folder js/
$ npm run watch
```
This script automatically triggers a `npm run prepare` command (`webpack`) each time a change is detected in the folder js/lib. Still, the notebook has to be relaoded for the new js to be available.

## 4. About the interaction between jupyter nb and conda env

- If jupyter is not installed in conda env, the default path when executing 'jupyter notebook' is the jupyter install in the root environment. Thus when a kernel is started in this configuration, it is launched inside the root conda env. On the top right side of the nb, "Python 3" is printed. To start a kernel inside another environment, you have to run the following commands :

```bash
source activate myenv
conda install ipykernel
python -m ipykernel install --user --name myenv --display-name "Python (myenv)"
```

Then in your nb : Kernel > change kernel > Python(myenv).

- If jupyter is installed in your conda env "myenv", the default path when executing 'jupyter notebook' from the env is the jupyter install in "myenv". Thus when a kernel is started in this configuration, it is launched inside this env, even though "Python 3" is printed in the nb. To start a kernel inside another environment, the same as above still applies.

As far as widgets are concerned: widgets may only be installed in a conda env which contains jupyter. If you run the installation of widgets inside a conda env, they should be installed within the jupyter bundle inside this conda env.
