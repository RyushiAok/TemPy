from os.path import dirname, join

import torch
from dotenv import dotenv_values

config = {
    **dotenv_values(join(dirname(__file__), "../.env.example")),
    **dotenv_values(join(dirname(__file__), "../.env.local")),
}

print(config)

print("hello world")
print(torch.__version__)
print(torch.cuda.is_available())
print(torch.version.cuda)
print(torch.backends.cudnn.version())
print(torch.cuda.get_device_name())
