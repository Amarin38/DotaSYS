# What you'll be able to do at the end of this tutorial
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('penguins')

sns.set_style(style='whitegrid')

sns.scatterplot(
    data=df,
    x='bill_length_mm',
    y='bill_depth_mm',
    hue='species',
    style='sex',
    palette='Paired_r'
)

plt.title('Exploring Physical Attributes of Different Penguins')
plt.xlabel('Bill Length (mm)')
plt.ylabel('Bill Depth (mm)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0)

plt.show()
