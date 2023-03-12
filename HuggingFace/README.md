# HuggingFace

## setup

- 환경
  macAir m2

### conda 및 가상환경 설정

- brew 설치
  brew install wget
- Miniforge 설치
  cd ~/Downloads
  wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
  sh Miniforge3-MacOSX-arm64.sh
- 확인
  conda info

- 가상환경 만들기
  conda create -n huggingface python=3.9
  conda env list
  conda activate huggingface

### TensorFlow 설치

- TensorFlow dependencies 설치
  conda install -c apple tensorflow-deps

- TensorFlow 설치
  python -m pip install tensorflow-macos

- TensorFlow-Metal (GPU framework) 설치
  python -m pip install tensorflow-metal

- TensorFlow 및 GPU 확인
  python

```python
import sys
import tensorflow.keras
import tensorflow as tf
import platform

res = f"""
Python Platform: {platform.platform()}
Tensor Flow Version: {tf.__version__}
Keras Version: {tensorflow.keras.__version__}
Python {sys.version}
"""
gpu = len(tf.config.list_physical_devices('GPU'))>0
print(res, "\nGPU is", "available" if gpu else "NOT AVAILABLE")
```

### torch 설치

- pytorch 설치
  PyTorch 1.12 버전 이후 M1 Mac에서도 GPU 연산을 지원되도록 업데이트

```
conda install -c pytorch pytorch
```

- Pytorch 및 GPU 확인
  python

```python
import torch

print(f"""Pytorch Version: {torch.__version__}
torch.cuda.is_available: {torch.cuda.is_available()}
torch.backends.mps.is_built: {torch.backends.mps.is_built()}
torch.backends.mps.is_available: {torch.backends.mps.is_available()}""")
```
