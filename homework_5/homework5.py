#!/usr/bin/env python
# coding: utf-8

# In[182]:


import pandas as pd
import seaborn as sns
from matplotlib.pyplot import *
import numpy as np


# # 1.REAL data

# ## 1.1 GFF and BED readers

# In[80]:


def read_gff(file_path):
    columns = ['chromosome', 'source', 'type', 'start', 'end', 
               'score', 'strand', 'phase', 'attributes']
    gff = pd.read_csv(file_path, sep='\t', names=columns)
    gff = gff[~gff['chromosome'].str.contains('#')]
    return gff

def read_bed6(file_path):
    columns = ['chromosome','start','end','name','score','strand']
    return pd.read_csv(file_path, sep='\t', names=columns)



beds = read_bed6('alignment.bed')
gffs = read_gff('rrna_annotation.gff')


# In[81]:


beds.head()


# In[83]:


gffs


# ## 1.2 rRNA attributes

# In[71]:


gffs['attributes'] = gffs['attributes'].str.extract("=(.+?S)")
gffs.head()


# ## 1.3 Ugly rRNA_barplot

# In[7]:


RNAs = gffs.groupby(['chromosome','attributes'], as_index=False).agg(RNA_count=('type','count'))
rRNA_barplot = sns.barplot(data=RNAs, hue='attributes', y='chromosome', x='RNA_count')


# ## 1.4 Poor man's bedtools intersect 

# Получаем при помощи мерджа декартово произведение двух матриц - все возможные сочетания между референсами и контигами (ведь 1 контиг может содержать несколько референсов)

# In[33]:


merged = gffs.merge(beds, how='inner', on='chromosome')


# Ищем пересечения между контигами и референсами при помощи одноименной функции:

# In[34]:




def intersect(ass, ae, bs, be):
    if (bs>ae or ass>be):
        return None
    else:
        os = max(ass, bs)
        oe = min(ae, be)
        result = [os, oe]
        return result
    
    


# In[35]:


merged['intersection'] = merged    .apply(lambda x: intersect(x.start_x, x.end_x, x.start_y, x.end_y), axis=1)
merged = merged.dropna(subset='intersection')
#сбрасываем непересеченные с референсами риды


# In[36]:


merged[['inter_start','inter_end']] = pd.DataFrame(
    merged.intersection.tolist(), index=merged.index)
merged = merged.sort_values(by=['start_x','inter_start','inter_end'])
#сортируем риды


# Команда ниже позволяет смотреть пересекается ли конец контига с началом следующего контига - если пересекается, то они создают непрерывную последовательность. Далее команда считает число пересекающихся друг с другом ридом. 

# In[13]:


(merged['inter_start']<=merged['inter_end'].shift(1)).astype(int).sum()


# Если все отсортированные контиги принадлежащие одному референсу пересекаются друг с другом и включают в себя начало и конец референса - они полностью покрывает референс. При этом число пересечени в этом случае равно числу контигов-1

# In[59]:


overlaps = merged.groupby('start_x',as_index=False)    .apply(lambda x: (x['inter_start']<=x['inter_end'].shift(1)).astype(int).sum())
overlaps = overlaps.rename(columns = {None:'overlaps'})
overlaps.head()


# Отбираем подходящие контиги: пересечений на 1 меньше, чем контигов, начало и конец референса входят в пересечение

# In[62]:


contig_data = merged    .groupby(['start_x','end_x','chromosome','attributes'], as_index=False)    .agg(first_inter_start=("inter_start","min"), 
         last_inter_end=("inter_end","max"), 
         all_contigs=('name',lambda x: list(x)), 
         contigs=('source','count'))
contig_overlaps = contig_data.merge(overlaps, on='start_x', how='inner')
start_end = contig_overlaps[(contig_overlaps['start_x']>=contig_overlaps['first_inter_start']) 
                            & (contig_overlaps['end_x']<=contig_overlaps['last_inter_end'])]
full_RNAs = start_end[start_end['contigs']-1 == start_end['overlaps']]
full_RNAs


#  # 2. Chart customization

# In[88]:


diff_exp = pd.read_csv('diffexpr_data.tsv.gz', sep='\t')
diff_exp

    


# In[126]:


def gene_group(logFC, pval_corr):
    if pval_corr <= 0.05:
        sign = 'Significantly'
    else:
        sign = 'Non-significantly'
    if logFC >= 0:
        expr = 'upregulated'
    else:
        expr = 'downregulated'
    return f'{sign} {expr}'
order = ['Significantly downregulated','Significantly upregulated',
         'Non-significantly downregulated', 'Non-significantly upregulated']


# In[127]:


diff_exp['gene_type'] = diff_exp.apply(
    lambda x: gene_group(x.logFC, x.pval_corr), axis = 1)


# In[326]:


sign = diff_exp[diff_exp['gene_type'].str.contains('S')]
sign = sign.sort_values(by='logFC')
top = pd.concat([sign.head(2), sign.tail(2)])
top


# In[379]:


plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.bf'] = 'Arial:italic:bold'
figure(figsize=(10, 6), dpi=100)
ax = sns.scatterplot(data = diff_exp, x = 'logFC',
                     y = 'log_pval', hue = 'gene_type', 
                     hue_order = order, s = 12, linewidth = 0)
ax.axhline(-np.log10(0.05), c='0.5', ls = '--')
ax.axvline(0, c='0.5', ls = '--')
ax.set_xlabel(r'$\mathbf{\log_{2}}$(fold change)', 
              weight='bold', style='italic')
ax.set_ylabel(r'$\mathbf{-\log_{10}}$(p value corrected)', 
              weight='bold', style='italic')
ax.tick_params(axis='both', which='major', labelsize=8, width = 1.2)
ax.xaxis.set_minor_locator(plt.MultipleLocator(1))
ax.yaxis.set_minor_locator(plt.MultipleLocator(5))
ax.xaxis.set_major_locator(plt.MultipleLocator(5))
ax = plt.gca()
ax.set_xlim([diff_exp['logFC'].min()-1, diff_exp['logFC'].max()+1])
plt.title('Volcano plot', weight='bold', style='italic')
legend_properties = {'weight':'bold', 'size':8}
plt.legend(prop=legend_properties, shadow=True, markerscale=0.6)
plt.text(8, -np.log10(0.05)+1, 'p value = 0.05', c='0.3', fontsize=8)
for index, row in top.iterrows():
    plt.annotate(row['Sample'], 
                 (row['logFC'], row['log_pval']), 
                 xytext=(row['logFC']-0.8, row['log_pval']+9), 
                 arrowprops={"arrowstyle":"->", 'linewidth':1,'edgecolor':'r'}, 
                 weight='bold')


# In[341]:


for index, row in top.iterrows():
    print(row['Sample'], row['logFC'], row['log_pval'])

