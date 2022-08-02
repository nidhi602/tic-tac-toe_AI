# -*- coding: utf-8 -*-
"""

@author: NIDHI

"""

import sys
import engine

if __name__ == "__main__":
    
    if len(sys.argv) == 3:
        p1 = sys.argv[1]
        p2 = sys.argv[2]
    
    else:
        p1 = p2 = "human_player"
            
    engine.play(p1, p2)
    

