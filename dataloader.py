import numpy as np

def load_citeulike():

    raw_data = dict()
    raw_data['total_users'] = 5551
    raw_data['total_items'] = 16980
    
    raw_data['train_data'] = np.load('dataset/citeulike/rsrf_user_data_train.npy')
    raw_data['val_data'] = np.load('dataset/citeulike/rsrf_user_data_val.npy')
    raw_data['test_data'] = np.load('dataset/citeulike/rsrf_user_data_test.npy')
    
    return raw_data

