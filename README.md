# stemcellhack
Guide on using the data from stemformatics.org

## Download the data files 
Go to stemformatics.org/atlas and use "more..." > download to get 3 files.

## Set up your environment using conda 
If you want to run the jupyter notebook from this repository, follow these instructions.

a) Download conda if you don't already have it (https://www.anaconda.com/distribution/)

b) Create a new conda environment and activate it
```bash
conda create -n stemcellhack
source activate stemcellhack
```
c) Use conda to install required packages
```bash
conda install pandas scikit-learn plotly jupyter
```
d) Start jupyter notebook and load the .ipynb file from this repo.
```bash
jupyter notebook
```


