import torch
import numpy as np
import torch.nn.functional as F

from onegan.utils import to_var


class VisionConv2d:

    def __init__(self, kernel, padding=1, dilation=1, name='VisionConv2d'):
        """
            Args:
                kernel: str or np.ndarray
        """
        if isinstance(kernel, str):
            kernel = {
                'laplacian': laplacian_kernel
            }[kernel]()
        assert kernel.ndim == 2, 'Plain Vision Kernel should be 2D'
        self.kernel = to_var(self._to_tensor(kernel[np.newaxis, np.newaxis, :]))
        self.padding = padding
        self.dilation = dilation
        self.name = name

    def __call__(self, x: torch.autograd.Variable):
        assert x.dim() == 4, 'input tensor should be 4D'
        return F.conv2d(x, self.kernel, padding=self.padding, dilation=self.dilation)

    def _to_tensor(self, kernel):
        return torch.from_numpy(kernel)


def laplacian_kernel():
    return np.array([[-1, -1, -1],
                     [-1,  8, -1],
                     [-1, -1, -1]], dtype='f')
