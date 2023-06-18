import torch

print("hello world")
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.version.cuda)
print(torch.backends.cudnn.version())
print(torch.cuda.get_device_name())
