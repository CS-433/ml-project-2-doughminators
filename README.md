[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/fEFF99tU)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13028598&assignment_repo_type=AssignmentRepo)

## This repo is essentially a copy of [MEDIAR](https://github.com/Lee-Gihun/MEDIAR/tree/main).

## Experiments
Our experiments can be found in the notebook ```MEDIAR Experiments.ipynb```. For reproducibility, or to use the fine-tuned weights resulting from the experiments, please see the last section "Reproducibility of best results on a test set" in the notebook. A quick demonstration of the (fine-tuned) model is shown in ```Fine_tuned_MEDIAR_Tutorial.ipynb```.

## Model checkpoints
The fine-tuned weights are downloadable from [google drive](https://drive.google.com/file/d/1yrLncA-wf594qKAE43o3BDP-Za7S1YV0/view?usp=sharing).

## What can be found in this repository?
In this repository, we also include some configurations files in the ```config``` folder. The ```image_processing.ipynb``` notebook contains the pre-processing methods for the YeaZ dataset. Finally, the ```train_tools/data_utils/utils.py``` file was modified to obtain correct image-label mapping for the YeaZ data; the original file can be found in the [original MEDIAR repo](https://github.com/Lee-Gihun/MEDIAR/tree/main).

## Reproducibility
All requirements are the same as in the original publication. However, we train our model with a NVIDIA A100-SXM4-40GB GPU which requires an extra installation (see below).

```
pip install -r requirements.txt
pip install segmentation-models-pytorch==0.3.1
pip install wandb
# Run the next line if training on google colab A100 GPUs
pip install torch==1.11.0+cu113 --extra-index-url https://download.pytorch.org/whl/cu113


