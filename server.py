import numpy as np

def generate_key():
    return np.random.randint(0, 1000)

def generate_matrix(shape):
    return np.random.randint(low=0,high=255,size=shape)

def bird_choise(mat, field_shape, id):
    np.random.seed(id)
    noise = np.random.rand(*field_shape)
    noise = noise * mat
    idx = np.unravel_index(np.argmax(noise, axis=None), noise.shape)
    return idx

