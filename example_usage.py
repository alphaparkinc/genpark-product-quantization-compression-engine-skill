from client import ProductQuantizer

pq = ProductQuantizer(m_subvectors=2, k_centroids=8)
vector = [0.1, -0.4, 0.9, 0.3]
code = pq.encode(vector)
print("Original Vector (4 floats):", vector)
print("Quantized Code (2 byte centroids):", code)
