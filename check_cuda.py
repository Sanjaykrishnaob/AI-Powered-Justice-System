import torch
import sys

print('torch version:', torch.__version__)
print('cuda available:', torch.cuda.is_available())
print('cuda runtime version:', torch.version.cuda)
if torch.cuda.is_available():
    try:
        print('device count:', torch.cuda.device_count())
        print('device name:', torch.cuda.get_device_name(0))
    except Exception as e:
        print('error getting device info:', e)
sys.exit(0)
