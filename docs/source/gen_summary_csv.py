#!/usr/bin/env python3
import sys
from pathlib import Path

import pandas as pd

# path_here = Path('.').resolve()
# path_csv = path_here / 'input_files/SUEWS_SiteInfo/csv-table'
# path_csv.exists()


# load all csv as a whole df
def load_df_csv(path_csv):
    if not path_csv.exists():
        print(str(path_csv), 'not existing!')
        sys.exit()

    # get list of all csv file names
    list_csv = list(path_csv.glob('*csv'))
    df_csv = pd.concat(
        {csv.stem: pd.read_csv(csv, skipinitialspace=True, quotechar='"')
            for csv in list_csv},
        sort=False)
    return df_csv


# retrieve description from rst files
# file_options = path_csv.parent / 'Input_Options.rst'


def load_df_opt_desc(file_options):
    ser_opts = pd.read_csv(
        file_options,
        sep='\n', skipinitialspace=True)
    ser_opts = ser_opts.iloc[:, 0]
    ind_opt = ser_opts.index[ser_opts.str.contains('.. option::')]
    ser_opt_name = ser_opts[ind_opt].str.replace('.. option::', '').str.strip()
    ser_opt_desc = ser_opts[ind_opt + 2].str.strip()
    df_opt_desc = pd.DataFrame(
        {'desc': ser_opt_desc.values}, index=ser_opt_name.rename('option'))
    return df_opt_desc


# df_opt_desc = load_df_opt_desc(file_options)


def gen_csv_suews(path_csv):
    # load all csv as a whole df
    df_csv = load_df_csv(path_csv)

    # retrieve description from rst files
    file_options = path_csv.parent / 'Input_Options.rst'
    df_opt_desc = load_df_opt_desc(file_options)

    list_csv_suews = df_csv.index.levels[0].to_series().filter(like='SUEWS')
    for csv_suews in list_csv_suews:
        df_csv_suews = df_csv.loc[csv_suews].dropna(axis=1).copy()
        df_csv_suews.loc[:, 'No.'] = df_csv_suews.loc[:, 'No.'].astype(int)
        for ind, row in df_csv_suews.iterrows():
            # print(row)
            # dict_row=row._asdict()
            var = row.loc['Column Name'].strip('`')
            if var in df_csv_suews.index:
                df_csv_suews.at[
                    ind, 'Description'] = df_opt_desc.loc[var].values[0]
        df_csv_suews.to_csv(path_csv / (csv_suews + '.csv'), index=False)

    return list_csv_suews
