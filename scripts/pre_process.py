import numpy as np
import pandas as pd
from PIL import Image

def preprocess(im):
    
    im = im/255
    im -= .5
    return im


def load_data_batch(ids, batch_size=32, channel=1, im_size=100, path='data'):
    
    '''
        This function create a batch of training data
    '''
    
    data = pd.read_csv(path + '/label.csv')
    
    path = path + '/images/'
    
    image_batch = np.zeros((batch_size, im_size, im_size, channel))
    
    label_hour = np.zeros((batch_size, 1))
    label_min = np.zeros((batch_size, 1))
    batch_ids = np.random.choice(ids, batch_size)
    
    ind = 0
    for i in range(len(batch_ids)):
        
        if channel == 1:
            im = Image.open(path + str(batch_ids[i]) + '.jpg').convert('L')
        else:
            im = Image.open(path + str(batch_ids[i]) + '.jpg')
            
        im = im.resize((im_size,im_size), Image.ANTIALIAS)
        im = np.array(im)
        
        image_batch[ind] = preprocess(im).reshape((im_size, im_size, channel))
        label_hour[ind] = (data['hour'][data.index==batch_ids[i]])
        label_min[ind] = (data['minute'][data.index==batch_ids[i]])/60
        ind += 1
            
    return (np.array(image_batch), np.array(label_hour), np.array(label_min))
