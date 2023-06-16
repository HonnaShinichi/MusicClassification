import numpy as np
from dataclasses import dataclass, field

#データクラスで管理しようと思ったけどいらないなぁこれ
@dataclass
class Music:
    name : str
    music : np.ndarray


    
