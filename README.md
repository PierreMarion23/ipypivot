# ipypivot

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/PierreMarion23/ipypivot-binder/master?filepath=demo_pivot_table.ipynb)

## 1 - Overview

This is a [jupyter widget (or ipywidget)](https://ipywidgets.readthedocs.io/en/stable/) wrapping the very convenient [pivotTable.js](https://pivottable.js.org/examples/) library.  

It enables to display and embed a pivotTable in a Jupyter notebook in a few Python lines.  

## 2 - Install

An ipywidget is a Python package with some associated javascript files.  
As such the installation requires 2 step:

```bash
$ pip install ipypivot
$ jupyter nbextension enable --py --sys-prefix ipypivot
```

For more info about the installation of this widget, and also tips about the development of custom jupyter widgets, see the [Install Guide](doc/install_guide.md).

## 3 - User Guide

See the [demo notebook](notebooks/demo_pivot_table.ipynb) for examples and explanations.  

In short:
+ The 2 pivotTable.js functions `pivot()` and `pivotUI()` are tranparently accessible.  
+ The data is expected in [pandas DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) format.  
+ The options are input as an option helper object (`Pivot_Options` or `PivotUI_Options`)  
+ _Note_: the range of possible options for `pivot()` and `pivotUI()` differ - but there is overlap.


Basic examples:

```python
df = pd.DataFrame(data=[{'color': 'blue', 'shape': 'circle'},
                        {'color': "red", 'shape': 'triangle'}])

# pivot()
p = pt.Pivot(df_data=df)
opts = p.options
opts.rows = ['color']
opts.cols = ['shape']
display(p)

# pivotUI
p = pt.PivotUI(df_data=df)
opts = p.options
opts.rows = ['color']
opts.cols = ['shape']
display(p)
```


## 4 - Alternative

The repo branch `alt` contains an alternative widget PivotUI widget.  
It has the same the same features but is implemented in pure web (buttons and 'Last Save' fields).  
As opposed to the master branch which implements a combo of core and custom widgets.  
The latter is more modular and flexible. In this case it is also slightly more complex.  
But it may serve as an example for building a Jupyter widget from several component widgets.

## 5 - Credit

This repo is the result from a collaboration between [oscar6echo](https://github.com/oscar6echo), [ocoudray](https://github.com/ocoudray), and [PierreMarion23](https://github.com/PierreMarion23).
