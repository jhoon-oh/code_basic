import numpy as np
import copy

def make_new_mtx(mtx, query):
    x1, y1, x2, y2 = query
    x1_, y1_, x2_, y2_ = x1-1, y1-1, x2-1, y2-1
    
    new_mtx = copy.deepcopy(mtx)
    new_mtx[x1_, y1:y2] = mtx[x1_, y1_:y2_]
    new_mtx[x1:x2, y2_] = mtx[x1_:x2_, y2_]
    new_mtx[x2_, y1_:y2_] = mtx[x2_, y1:y2]
    new_mtx[x1_:x2_, y1_] = mtx[x1:x2, y1_]
    
    return new_mtx, min(list(mtx[x1_, y1_:y2_])+
                        list(mtx[x1_:x2_, y2_])+
                        list(mtx[x2_, y1:y2])+
                        list(mtx[x1:x2, y1_]))

def solution(rows, columns, queries):
    mtx_flat = np.array(list(range(1, rows*columns+1)))
    mtx = mtx_flat.reshape(rows, columns)
    
    answer = []
    for i, query in enumerate(queries):
        if i == 0:
            new_mtx, min_val = make_new_mtx(mtx, query)
        else:
            new_mtx, min_val = make_new_mtx(new_mtx, query)
        answer.append(int(min_val))
    
    return answer