# ipypivot

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/PierreMarion23/ipypivot-binder/master?filepath=demo_pivot_table.ipynb)

## 1 - Overview

This is a [jupyter widget (or ipywidget)](https://ipywidgets.readthedocs.io/en/stable/) wrapping the very convenient [pivotTable.js](https://pivottable.js.org/examples/) library.  

It enables to display and embed a pivotTable in a Jupyter notebook in a few Python lines.  

## 2 - Install

From pip:

```bash
$ pip install ipypivot
```

From conda:

```bash
$ conda install -c conda-forge ipypivot
```

For more info about jupyter widgets (installation process, packaging and publishing), and also tips about the development of custom widgets, see [this tutorial repo](https://github.com/ocoudray/first-widget). All what's written there is also true for this package, just changing the name `first-widget` into `ipypivot`.

## 3 - User Guide

See the [demo notebook](https://nbviewer.jupyter.org/github/PierreMarion23/ipypivot/blob/master/notebooks/demo_ipypivot.ipynb) for examples and explanations.  

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
