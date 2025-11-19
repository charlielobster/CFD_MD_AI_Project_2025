-    import torch.nn as nn
+    from dataclasses import dataclass
+    from physicsnemo.models.meta import ModelMetaData
+    from physicsnemo.models.module import Module

-    class UNet(nn.Module):
+    @dataclass
+    class MetaData(ModelMetaData):
+        name: str = "UNet"
+        # Optimization
+        jit: bool = False
+        cuda_graphs: bool = True
+        amp_cpu: bool = True
+        amp_gpu: bool = True
+
+    class UNet(Module):
         def __init__(self, in_channels=1, out_channels=1):
-            super(UNet, self).__init__()
+            super(UNet, self).__init__(meta=MetaData())

             self.enc1 = self.conv_block(in_channels, 64)
             self.enc2 = self.conv_block(64, 128)