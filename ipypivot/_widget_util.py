

import pandas as pd


def shape_df(df,
             options):
    """
    Build multi index dataframe from pivottable.js data
    """

    row_names = options['rows']
    col_names = options['cols']

    if row_names and col_names:
        df2 = df.set_index(row_names)

        row_idx = df2.index
        data = df2.values

        col_tuples = [tuple(e.split('-'))
                      for e in list(df.columns[len(row_names):])]

        col_idx = pd.MultiIndex.from_tuples(tuples=col_tuples,
                                            names=col_names)

        df_res = pd.DataFrame(data=data,
                              index=row_idx,
                              columns=col_idx)

    elif row_names and not col_names:
        df2 = df.set_index(row_names)

        df_res = pd.DataFrame(df2)

    elif not row_names and col_names:
        row_idx = df.index
        data = df.values

        col_tuples = [tuple(e.split('-'))
                      for e in list(df.columns)]

        col_idx = pd.MultiIndex.from_tuples(tuples=col_tuples,
                                            names=col_names)

        df_res = pd.DataFrame(data=data,
                              index=row_idx,
                              columns=col_idx)

    else:

        df_res = pd.DataFrame()

    return df_res
