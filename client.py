"""Product Quantization Compression Engine.
100% Python Standard Library.
"""

import math
import random

def euclidean_dist(v1, v2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(v1, v2)))

class ProductQuantizer:
    """Sub-vector partitioning and codebook vector quantization."""
    def __init__(self, m_subvectors=2, k_centroids=4):
        self.m = m_subvectors
        self.k = k_centroids
        self.codebooks = []

    def train_mock(self, dim):
        sub_dim = dim // self.m
        random.seed(42)
        self.codebooks = []
        for i in range(self.m):
            sub_centroids = []
            for _ in range(self.k):
                sub_centroids.append([random.uniform(-1, 1) for _ in range(sub_dim)])
            self.codebooks.append(sub_centroids)

    def encode(self, vector):
        dim = len(vector)
        sub_dim = dim // self.m
        if not self.codebooks:
            self.train_mock(dim)
        codes = []
        for i in range(self.m):
            sub_vec = vector[i * sub_dim : (i + 1) * sub_dim]
            best_idx = 0
            best_dist = float('inf')
            for c_idx, centroid in enumerate(self.codebooks[i]):
                d = euclidean_dist(sub_vec, centroid)
                if d < best_dist:
                    best_dist = d
                    best_idx = c_idx
            codes.append(best_idx)
        return codes
