# genpark-product-quantization-compression-engine-skill

Product Quantization (PQ) vector compression engine splitting high-dimensional float embeddings into compact centroid codebook indices.

## Architecture

```mermaid
flowchart LR
    V["1024-dim Float Vector (4096 bytes)"] --> Slicer["Subvector Slicer (M=8)"]
    Slicer --> CB["Sub-Space Centroid Codebooks"]
    CB --> Code["Quantized Byte Indices (8 bytes)"]
```

## Features
- **Massive Compression**: Up to 64x memory footprint reduction.
- **Zero External Dependencies**: 100% Python Standard Library.
