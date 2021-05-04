import tensorflow as tf
import cv2
import numpy as np
import os
import keras
import sys
sys.path.insert(1, '/tmp/Projects2021/depth_estimation/final-project-monodepth-ccny/dataloaders/')
sys.path.insert(1, '/tmp/Projects2021/depth_estimation/final-project-monodepth-ccny/losses/')
from ssim_loss import *
from dataloaders import *
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam


rgb_images = os.listdir('/tmp/Projects2021/rgbd_dataset/dataset/rgb/')
rgb_images.sort()
rgb_images = [str('/tmp/Projects2021/rgbd_dataset/dataset/rgb/') + file for file in rgb_images]
depth_images = os.listdir('/tmp/Projects2021/rgbd_dataset/dataset/depth/')
depth_images.sort()
depth_images = [str('/tmp/Projects2021/rgbd_dataset/dataset/depth/') + file for file in depth_images]

test_size = 20
rgb_images_test = rgb_images[:test_size]
depth_images_test = depth_images[:test_size]

# rgb_images_train = rgb_images[test_size:]
# depth_images_train = depth_images[test_size:]

# Load data:

load_data = DataGenerator()

# X_train, y_train = load_data.load_all(rgb_files=rgb_images_train, 
#                                       depth_files=depth_images_train)

X_test, y_test = load_data.load_all(rgb_files=rgb_images_test, 
                                  depth_files=depth_images_test)

print(y_test.shape)
import matplotlib.pyplot as plt
plt.subplot(2,1,1)
pr = y_test[0]
plt.imshow(pr)
plt.subplot(2,1,2)
plt.imshow(y_test[0])
plt.savefig('test_imgs.png', dpi=200, format='png')
for i in range(len(pr)):
    print(pr[i])
print(np.max(y_test[0]))
# checkpoint = ModelCheckpoint('best_model128_ssim.hdf5',
#                             monitor='loss',
#                             save_best_only=True)

# loss = ssim_loss(X_train[0], X_train[0])

# amount = loss.call()
# print(amount)
# m = unet128(input_shape=[128, 128, 3])
# m.model.compile(optimizer='adam', loss=ssim_loss())
# m.model.summary()
# m.model.fit(X_train, y_train, epochs=20,callbacks=[checkpoint])


