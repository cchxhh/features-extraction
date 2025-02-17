from __future__ import annotations

import torch
from torch.utils.data import Dataset


class AudioFeaturesDataset(Dataset):
    def __init__(self, features_dict, *, use_cuda=False):
        self.features_dict = features_dict
        self.use_cuda = use_cuda
        self.items = list(features_dict.items())

    def __getitem__(self, index):
        (label, _), features = self.items[index]
        features = torch.tensor(features[:256], dtype=torch.float32)
        features = torch.cat([features, torch.zeros(256 - features.shape[0], features.shape[1])])
        if self.use_cuda:
            return features.cuda(), torch.tensor(label, dtype=torch.int64).cuda()
        else:
            return features, torch.tensor(label, dtype=torch.int64)

    def __len__(self):
        return len(self.items)
