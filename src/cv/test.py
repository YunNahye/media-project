import os
import torch
import torchvision
from torch.utils.data import random_split
import torchvision.models as models
from torch import nn
from torch import optim
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
from torchvision import datasets
import torchvision.transforms as transforms
from torch.utils.data.sampler import SubsetRandomSampler
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import prepare_data


def load_checkpoint(path):
    checkpoint = torch.load(path)
    model = checkpoint['model']
    model.load_state_dict(checkpoint['state_dict'])
    for parameter in model.parameters():
        parameter.requires_grad = False
    return model.eval()


def testing(path, test_loader):
    classes = ['plastic', 'brown_glass', 'can', 'cloth', 'green_glass', 'newspaper', 'paperbox', 'paperpack',
               'styrofoam', 'vinyl', 'white_glass']
    loaded_model = load_checkpoint(path)
    train_on_gpu = torch.cuda.is_available()
    criterion = torch.nn.CrossEntropyLoss()
    test_loss = 0.0
    class_correct = list(0. for i in range(11))
    class_total = list(0. for i in range(11))
    for data, target in test_loader:
        # move tensors to GPU if CUDA is available
        if train_on_gpu:
            data, target = data.cuda(), target.cuda()
        # forward pass: compute predicted outputs by passing inputs to the model
        output = loaded_model(data)
        # calculate the batch loss
        loss = criterion(output, target)
        # update test loss
        test_loss += loss.item() * data.size(0)
        # convert output probabilities to predicted class
        _, pred = torch.max(output, 1)
        # compare predictions to true label
        correct_tensor = pred.eq(target.data.view_as(pred))
        correct = np.squeeze(correct_tensor.numpy()) if not train_on_gpu else np.squeeze(correct_tensor.cpu().numpy())
        # calculate test accuracy for each object class

        for i in range(len(target.data)):
            label = target.data[i]

            class_correct[label] += correct[i].item()
            class_total[label] += 1

    # average test loss
    test_loss = test_loss / len(test_loader.dataset)
    print('Test Loss: {:.6f}\n'.format(test_loss))
    for i in range(11):
        if class_total[i] > 0:
            print('Test Accuracy of %5s: %2d%% (%2d/%2d)' % (
                classes[i], 100 * class_correct[i] / class_total[i],
                np.sum(class_correct[i]), np.sum(class_total[i])))
        else:
            print('Test Accuracy of %5s: N/A (no training examples)' % (classes[i]))
    print('\nTest Accuracy (Overall): %2d%% (%2d/%2d)' % (
        100. * np.sum(class_correct) / np.sum(class_total),
        np.sum(class_correct), np.sum(class_total)))


if __name__ == "__main__":
    train_loader, valid_loader, test_loader = prepare_data.preprocessing(0, 32, 0.2)
    testing("13.pth", test_loader)
