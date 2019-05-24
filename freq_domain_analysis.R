library(ggplot2)
library(dplyr)
library(tidyr)
library(plotly)
library(readr)

setwd("/home/otavio/Workspace/UFBA/MATE33/bayesian_learning")

dataset_dir = "/home/otavio/Workspace/UFBA/MATE33/bayesian_learning/datasets/heartbeat"

test_ds_path = paste(dataset_dir, "mitbih_test.csv", sep = "/")
train_ds_path = paste(dataset_dir, "mitbih_train.csv", sep = "/")

mitbih_train = read_csv(train_ds_path, col_names = F)
mitbih_test = read_csv(test_ds_path, col_names = F)

train_nsamples = nrow(mitbih_train)
test_nsamples = nrow(mitbih_test)

ncol(mitbih_test)
nrow(mitbih_test)
