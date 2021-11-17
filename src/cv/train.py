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

train_on_gpu = torch.cuda.is_available()
if not train_on_gpu:
    print('CUDA is not available.  Training on CPU ...')
else:
    print('CUDA is available!  Training on GPU ...')


# 모델 학습
def train(train_loader, valid_loader, class_num, requires_grad, n_epochs, learning_rate):
    model = models.resnet50(pretrained=True)
    # Use GPU if it's available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(device)
    for layer, param in model.named_parameters():
        param.requires_grad = requires_grad
    # 출력단 설정
    model.fc = nn.Sequential(nn.Linear(2048, 256),
                             nn.ReLU(),
                             nn.Dropout(0.2),
                             nn.Linear(256, class_num),
                             nn.LogSoftmax(dim=1))
    # 손실 함수, optimizer 설정
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    model.to(device)
    valid_loss_min = np.Inf
    # 학습 시작
    for epoch in range(1, n_epochs + 1):
        train_loss = 0.0
        valid_loss = 0.0
        model.train()
        for data, target in train_loader:
            # CUDA
            if train_on_gpu:
                data, target = data.cuda(), target.cuda()
            optimizer.zero_grad()
            # 결과
            output = model(data)
            # 배치 LOSS 계산
            loss = criterion(output, target)
            # backward pass
            loss.backward()
            optimizer.step()
            # update training loss
            train_loss += loss.item() * data.size(0)

        # 모델 validation
        model.eval()
        for data, target in valid_loader:
            # CUDA
            if train_on_gpu:
                data, target = data.cuda(), target.cuda()
            # 결과
            output = model(data)
            # 배치 LOSS 계산
            loss = criterion(output, target)
            valid_loss += loss.item() * data.size(0)

        # 평균 LOSS 계산
        train_loss = train_loss / len(train_loader.sampler)
        valid_loss = valid_loss / len(valid_loader.sampler)

        # print training/validation statistics
        print('Epoch: {} \tTraining Loss: {:.6f} \tValidation Loss: {:.6f}'.format(
            epoch, train_loss, valid_loss))

        # Validation loss 가 좋아진 모델 저장
        if valid_loss <= valid_loss_min:
            print('Validation loss decreased ({:.6f} --> {:.6f}).  Saving model ...'.format(
                valid_loss_min,
                valid_loss))
            best_epoch = epoch
            checkpoint = {'model': model,
                          'state_dict': model.state_dict(),
                          'optimizer': optimizer.state_dict()}

            torch.save(checkpoint, '{}.pth'.format(epoch))
            print("Model saved")
            valid_loss_min = valid_loss


def main():
    train_loader, valid_loader, test_loader = prepare_data.preprocessing(0, 32, 0.2)
    train(train_loader, valid_loader, 11, False, 20, 0.003)


if __name__ == "__main__":
    main()
