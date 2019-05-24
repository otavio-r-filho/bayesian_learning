library(ggplot2)
library(dplyr)
library(tidyr)
library(plotly)
library(readr)

setwd("/home/otavio/Workspace/UFBA/MATE33/bayesian_learning")

dataset_dir = "/home/otavio/Workspace/UFBA/MATE33/bayesian_learning/datasets/heartbeat"

test_ds_path = paste(dataset_dir, "mitbih_test.csv", sep = "/")
train_ds_path = paste(dataset_dir, "mitbih_train.csv", sep = "/")

fs = 360

mitbih_train = read_csv(train_ds_path, col_names = F)
mitbih_test = read_csv(test_ds_path, col_names = F)

mitbih_test_X = mitbih_test[,-188]
mitbih_test_Y = mitbih_test[,188]

mitbih_train_X = mitbih_train[,-188]
mitbih_train_Y = mitbih_train[,188]

names(mitbih_test_X) = (1:ncol(mitbih_test_X))
names(mitbih_test_Y) = c("class_code")

names(mitbih_train_X) = (1:ncol(mitbih_train_X))
names(mitbih_train_Y) = c("class_code")

snd_mitbih_test_X = mitbih_test_X.T %>% 
  mean

train_nsamples = nrow(mitbih_train)
test_nsamples = nrow(mitbih_test)

ncol(mitbih_test)
nrow(mitbih_test)

ncol(mitbih_train)
nrow(mitbih_train)
