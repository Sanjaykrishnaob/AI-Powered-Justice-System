# GPU Setup Instructions for AI-Powered Legal Research System

## Your GPU: NVIDIA GeForce RTX 2050 (4GB VRAM)
## CUDA Version: 13.0

---

## Step 1: Install PyTorch with CUDA Support

You currently have PyTorch CPU version. To use your GPU, install the CUDA version:

```bash
# Uninstall CPU version
pip uninstall torch torchvision torchaudio

# Install CUDA 12.4 version (compatible with CUDA 13.0)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

---

## Step 2: Verify GPU Installation

After installation, verify:

```python
import torch
print("CUDA Available:", torch.cuda.is_available())
print("GPU Device:", torch.cuda.get_device_name(0))
print("CUDA Version:", torch.version.cuda)
```

Expected output:
```
CUDA Available: True
GPU Device: NVIDIA GeForce RTX 2050
CUDA Version: 12.4
```

---

## Step 3: Re-run Your Project

After installation, your system will automatically use GPU:
- 🚀 **3-5x faster inference**
- 🧠 **Better model performance**
- ⚡ **Faster embeddings generation**

---

## Quick Install Command

Copy and paste this in your terminal:

```bash
pip uninstall -y torch torchvision torchaudio && pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

---

## Performance Improvements Expected:

### Before (CPU):
- First query: 3-5 seconds
- Embedding generation: 30-60 seconds
- Model loading: 10-15 seconds

### After (GPU - RTX 2050):
- First query: 1-2 seconds (3x faster)
- Embedding generation: 10-20 seconds (3x faster)
- Model loading: 3-5 seconds (3x faster)

---

## Memory Considerations:

Your RTX 2050 has **4GB VRAM**. The models will fit perfectly:
- Embedder (MiniLM): ~120MB
- Generator (FLAN-T5-small): ~300MB
- Re-ranker (Cross-Encoder): ~90MB
- **Total**: ~510MB (plenty of room!)

---

## Alternative: Keep CPU if Needed

If you want to keep using CPU (for any reason):
- Current setup works fine
- No changes needed
- Just slower performance

---

## Troubleshooting:

### "CUDA out of memory"
Reduce batch size in notebook:
```python
batch_size = 32  # Instead of 64
```

### "GPU not detected"
1. Check NVIDIA drivers are up to date
2. Restart computer after PyTorch installation
3. Run `nvidia-smi` to verify GPU is working

---

**Run the install command above and restart your application for GPU acceleration!**
