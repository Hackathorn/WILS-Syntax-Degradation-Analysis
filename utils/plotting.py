import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_metrics(df, norm_l1=False):
    """
    Plot multiple semantic distance metrics to compare degradation effects.

    Parameters:
        df (pd.DataFrame): DataFrame containing columns 'cos_sim', 'l2_sim', 'l1_sim'
    """
    
    l1 = df['l1_sim']
    if norm_l1:
        # Normalize L1 distance to range 0..1 for scale alignment
        l1 = (l1 - l1.min()) / (l1.max() - l1.min()) if l1.max() != l1.min() else l1

    plt.figure(figsize=(10, 6))
    plt.plot(df['cos_sim'], marker='o', label='Cosine Distance')
    plt.plot(df['l2_sim'], marker='s', label='L2 (Euclidean) Distance')
    plt.plot(l1, marker='^', label='L1 (Manhattan) Distance (normalized)')

    plt.title('Semantic Distance Metrics by Degradation Step')
    plt.xlabel('Degradation Step')
    plt.ylabel('Distance from Original')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def plot_all_metrics(df_list, plot_type="stripplot"): 

    # Prepare long-form DataFrame for seaborn
    records = []

    for df in df_list:
        for step, row in df.reset_index().iterrows():
            records.append({'step': step, 'metric': 'Cosine', 'value': row['cos_sim']})
            records.append({'step': step, 'metric': 'L2',     'value': row['l2_sim']})
            records.append({'step': step, 'metric': 'L1',     'value': row['l1_sim']})

    plot_df = pd.DataFrame.from_records(records)

    # Normalize L1 values to 0-1
    if not plot_df[plot_df['metric'] == 'L1']['value'].empty:
        l1_vals = plot_df[plot_df['metric'] == 'L1']['value']
        l1_norm = (l1_vals - l1_vals.min()) / (l1_vals.max() - l1_vals.min())
        plot_df.loc[plot_df['metric'] == 'L1', 'value'] = l1_norm

        plt.figure(figsize=(12, 6))
        marker_mapping = {'Cosine': 'o', 'L2': 's', 'L1': '^'}

        """ choose between swarm-plot or violin-plot or strip-plot """
        match plot_type:
            case "stripplot":
                sns.stripplot(data=plot_df, x='step', y='value', hue='metric', dodge=True, palette='Set2', size=3)
            case "swarmplot":
                sns.swarmplot(data=plot_df, x='step', y='value', hue='metric', dodge=True, palette='Set2', size=3)
            case "violinplot":
                sns.violinplot(data=plot_df, x='step', y='value', hue='metric', dodge=True, palette='Set2', fill=False)

        plt.title("Semantic Degradation Distributions by Step")
        plt.xlabel("Degradation Step")
        plt.ylabel("Distance from Original")
        plt.legend(title="Metric")
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()
