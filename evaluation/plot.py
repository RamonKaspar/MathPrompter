import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import precision_score
import os

def compute_detailed_metrics(df):
    metrics = {
        'Method': ['MathPrompter Total', 'Algebraic Only', 'Python Only'],
        'Accuracy': [],
        'Hallucination Rate': [],
        'Precision': []
    }
    
    df = df.replace('None', np.nan)
        
    for col in ['Predicted Answer Total', 'Predicted Answer Algebraic Expression', 'Predicted Answer Python Code']:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        correct = df[df[col] == df['Correct Answer']]
        accuracy = len(correct) / len(df) if len(df) > 0 else 0
        
        hallucinations = df[(df[col] != df['Correct Answer']) & (df[col].notna()) & (df[col] != 'None')]
        hallucination_rate = len(hallucinations) / len(df) if len(df) > 0 else 0
        
        binary_true = (df['Correct Answer'] == df[col]).astype(int)
        binary_pred = (df[col].notna() & (df[col] != 'None')).astype(int)
        
        precision = precision_score(binary_true, binary_pred, zero_division=0)
        
        # Debugging prints
        print(f"\nColumn: {col}")
        print(f"Correct entries count: {len(correct)}")
        print(f"Total non-NA predictions count: {df[col].notna().sum()}")
        print(f"Accuracy: {accuracy}")
        print(f"Hallucination Rate: {hallucination_rate}")
        print(f"Precision: {precision}")
        
        metrics['Accuracy'].append(accuracy)
        metrics['Hallucination Rate'].append(hallucination_rate)
        metrics['Precision'].append(precision)

    return pd.DataFrame(metrics)

def plot_individual_metrics(df_metrics):
    metrics = df_metrics.columns[1:]
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
    for i, metric in enumerate(metrics):
        # Changed to set 'Method' as the hue and disable the legend directly.
        bar_plot = sns.barplot(x='Method', y=metric, hue='Method', data=df_metrics, ax=axes[i], palette='deep', legend=False)
        axes[i].set_title(f'{metric} Comparison by Method')
        axes[i].set_ylim(0, 1)

        # Adding labels inside the bars
        for p in bar_plot.patches:
            bar_plot.annotate(format(p.get_height(), '.2f'), 
                              (p.get_x() + p.get_width() / 2., p.get_height()), 
                              ha='center', va='center', 
                              size=9, xytext=(0, -12), 
                              textcoords='offset points')

    plt.tight_layout()
    plt.savefig(os.path.join('plots', 'individual_metrics.png'))
    plt.close()

def plot_radar_chart(df_metrics):
    labels = np.array(df_metrics.columns[1:])
    num_vars = len(labels)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    palette = sns.color_palette("deep", len(df_metrics['Method']))

    for idx, row in df_metrics.iterrows():
        data = row[labels].tolist()
        data += data[:1]
        ax.plot(angles, data, linewidth=2, label=row['Method'], color=palette[idx], linestyle='dashed') # Fixed linestyle redundancy
        ax.fill(angles, data, alpha=0)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, color='grey', size=12)
    ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

    plt.savefig(os.path.join('plots', 'radar_chart.png'))
    plt.close()

if __name__ == '__main__':
    if not os.path.exists('plots'):
        os.makedirs('plots')
    
    df = pd.read_csv('output_SVAMP_eval.csv')
    df.replace({'None': None}, inplace=True)

    df_metrics = compute_detailed_metrics(df)
    plot_individual_metrics(df_metrics)
    plot_radar_chart(df_metrics)