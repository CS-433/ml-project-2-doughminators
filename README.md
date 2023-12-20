[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/fEFF99tU)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13028598&assignment_repo_type=AssignmentRepo)

## This repo is essentially a copy of [MEDIAR](https://github.com/Lee-Gihun/MEDIAR/tree/main).

Our experiments can be found in the notebook ```MEDIAR Experiments.ipynb```. For reproducibility, or to use the fine-tuned weights resulting from the experiments, please see the last section "Reproducibility of best results on a test set" in the notebook. 

The fine-tuned weights are downloadable from [google drive]().

In this repository, we also include some configurations files in the ```config``` folder. The ```image_processing.ipynb``` notebook contains the pre-processing methods for the YeaZ dataset. Finally, the ```train_tools/data_utils/utils.py``` file was modified to obtain correct image-label mapping for the YeaZ data; the original file can be found in the [original MEDIAR repo](https://github.com/Lee-Gihun/MEDIAR/tree/main).