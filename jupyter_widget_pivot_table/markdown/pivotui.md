+ The `PivotUI` object say `p` has 2 buttons:
+ **Save** to snapshot the current state and access with `p.table.df_export` (dataframe) and `p.table.options` (dict)  
    + Options which are javascript functions are discarded when passed to Python
    + The first snapshot takes place immediately after creation as recorded by the timestamp right of the buttons
    + However there is a slight delay - so wait for say 0.2s to access it (ie add `sleep(0.2)` in a notebook)
+ **Restore** to apply the options saved

