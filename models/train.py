import sys
sys.path.insert(1, '/tmp/Projects2021/depth_estimation/final-project-monodepth-ccny/dataloaders/')
from dataloaders import *
from unet128 import unet128
from unet256 import unet256
from res50 import res50
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam
import matplotlib.pyplot as plt

dataset_path = '/tmp/Projects2021/rgbd_dataset/dataset2/'
argv = sys.argv

if argv[1] == 'unet128':
    dtloader = dataloader_rgbd(dataset_path, 8, image_size=128)
    checkpoint = ModelCheckpoint('best_model128.hdf5',
                                monitor='loss',
                                save_best_only=True)

    m = unet128(input_shape=[128, 128, 3])
    m.model.compile(optimizer='adam', loss='mse')
    m.model.summary()
    m.model.fit(dtloader, epochs=int(argv[2]), callbacks=[checkpoint])

elif argv[1] == 'unet256':
    dtloader = dataloader_rgbd(dataset_path, 8, image_size=256)
    checkpoint = ModelCheckpoint('best_model256.hdf5',
                                monitor='loss',
                                save_best_only=True)

    m = unet256(input_shape=[256, 256, 3])
    m.model.compile(optimizer='adam', loss='mse')
    m.model.summary()
    m.model.fit(dtloader, epochs=int(argv[2]), callbacks=[checkpoint])

elif argv[1] == 'res50':
    dtloader = dataloader_rgbd(dataset_path, 8, image_size=128)
    checkpoint = ModelCheckpoint('best_modelres50.hdf5',
                                monitor='loss',
                                save_best_only=True)

    m = res50(input_shape=(128, 128, 3))
    m.model.compile(optimizer='adam', loss='mse')
    m.model.summary()
    m.model.fit(dtloader, epochs=int(argv[2]), callbacks=[checkpoint])
else:
    print("Command received: ", argv[1])
    print("\nPlease define the model you want to train and number of epochs!\n")