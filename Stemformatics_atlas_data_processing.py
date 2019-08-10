#!/usr/bin/env python
# coding: utf-8

# How to use the atlas data from Stemformatics.
# 1. Set up your environment using conda
#     a) Download conda if you don't already have it (https://www.anaconda.com/distribution/)
# 
#     b) Create a new conda environment and activate it
# ```bash
# conda create -n stemcellhack
# source activate stemcellhack
# ```
#     c) Use conda to install required packages
# ```bash
# conda install pandas scikit-learn plotly jupyter
# ```
#     d) Start this notebook using jupyter
# ```bash
# jupyter notebook
# ```
# 
# 2. Download the data files
# Go to stemformatics.org/atlas and use "more..." > download to get 3 files.

# In[2]:


# Set up the environment.
import pandas, os, sklearn.decomposition
from IPython.display import display
import plotly
import plotly.graph_objs as go
plotly.offline.init_notebook_mode()

# Show conda environment which was used to run this notebook
print(os.environ['CONDA_DEFAULT_ENV'])
print(pandas.__version__, plotly.__version__)


# In[3]:


# Read expression matrix
df = pandas.read_csv("imac_atlas_expression_v7.1.tsv", sep="\t", index_col=0)
print(df.shape)
display(df.head())


# This matrix has gene ids as rows and sample ids as columns. It is a concatenation of gene expression across many datasets (microarray and rna-seq), then rank transformed so that all values are on similar scales. We have done some work to filter out genes that have large variance across platforms, leaving us with genes where the biological variability is greater. This list of filtered genes can be found in this file.

# In[4]:


genes = pandas.read_csv("imac_atlas_genes_v7.1.tsv", sep="\t", index_col=0)
print(genes.shape)
display(genes.head())


# In[5]:


# So now make a row subset of the expression matrix based on this inclusion status.
df = df.loc[genes[genes["inclusion"]].index]
print(df.shape)


# In[16]:


# We can perform principle components analysis on this now using the PCA function from the sklearn package. 
# This function will perform PCA on the rows of the input matrix, so we need to transpose df before input.
# It also requires a numpy array object, rather than pandas DataFrame, so use values.
pca = sklearn.decomposition.PCA(n_components=10)
coords = pca.fit_transform(df.transpose().values)

# coords is a numpy array that contains PCA coordinates. 
# Turn this into a DataFrame object, taking only the first 3 components
coords = pandas.DataFrame(coords[:,:3], index=df.columns, columns=['x','y','z'])

print(coords.shape)
display(coords.head())


# In[27]:


# We can now plot this. This is the most basic plot with all default settings.
import plotly.express
fig = plotly.express.scatter_3d(coords, x='x',y='y',z='z')
fig.show()

