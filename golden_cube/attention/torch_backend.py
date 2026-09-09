from golden_cube.attention.backend import AttentionBackend


class TorchAttentionBackend(AttentionBackend):
    def forward(self, *args, **kwargs):
        raise NotImplementedError
