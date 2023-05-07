.ONESHELL:
SHELL = /bin/bash

## env : Creates and configures the environment

.PHONY : env
env : 
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate notebook
	conda install ipykernel
	python -m ipykernel install --user --name make-env --display-name "IPython - shelter"


## html : build the JupyterBook normally

.PHONY : html
html :
	jupyterbook build .

## all : run all notebooks

.PHONY : all
all :
	jupyterbook execute main.ipynb


## help : include documentation

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<