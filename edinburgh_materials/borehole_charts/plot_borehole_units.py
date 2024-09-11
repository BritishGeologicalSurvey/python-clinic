"""
A module for plotting the units within borehole data.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

BOREHOLE_CSV = Path('reorganised_bh_records.csv')
MAP = Path('boreholes_of_the_north_sea.png')
GRAPH = Path('borehole_layer_list_counts.png')

print(f"Hellllllooooooooooooooo!!!! from {__name__}")


def load_csv(filename):
    df = pd.read_csv(filename)
    return df


def plot_map(df, output_filename):
    ax = df.plot(x='X_WGS84', y='Y_WGS84', kind='scatter', c='WATER_DEPTH')
    ax.set_title('Boreholes of the North Sea')
    fig = ax.get_figure()
    fig.savefig(output_filename)


def clean_borehole_df(borehole_df):
    clean_df = borehole_df.query('ID != 0 and PRIMARY_COMPONENT.notna()').copy()
    clean_df['PRIMARY_COMPONENT'] = (clean_df['PRIMARY_COMPONENT']
                                     .str.title()
                                     .str.strip())
    return clean_df


def plot_layer_list_counts(clean_bh_df, output_filename, cutoff=10, kind='bar'):
    fig = plt.figure()
    bh_layers = (clean_bh_df
                 .sort_values(['SAMPLE_NAME', 'BED_BASE'])
                 .groupby('SAMPLE_NAME')
                 .agg({'PRIMARY_COMPONENT': ', '.join}))
    counts = bh_layers['PRIMARY_COMPONENT'].value_counts()
    significant_counts = counts.loc[counts >= cutoff]
    if kind == 'pie':
        ax = significant_counts.plot(kind='pie', labels=signif_counts.index)
    elif kind == 'bar':
        ax = significant_counts.plot(kind='bar')
    fig.savefig(output_filename)


if __name__ == "__main__":
    df = load_csv(BOREHOLE_CSV)
    plot_map(df, MAP)
    print(f"Plotted {MAP}")
    clean_df = clean_borehole_df(df)
    plot_layer_list_counts(clean_df, GRAPH, cutoff=20)
    print(f"Plotted {GRAPH}")
