import numpy as np
import pandas as pd
import time

mnist = pd.read_csv("../input/train.csv")
mnist.head()


y_train = mnist.label.values
x_train = mnist.drop('label',axis=1) 
x_train = (x_train / 255.0).values
x_train = np.reshape(x_train,(42000,1,28,28))
x_train.shape

from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from keras.optimizers import SGD
from keras import backend as K

K.set_image_data_format('channels_first')
IMG_SIZE = 28
NUM_CLASSES = 10

def cnn_model():
    model = Sequential()

    model.add(Conv2D(32, (3, 3), padding='same',
                     input_shape=(1, IMG_SIZE, IMG_SIZE),
                     activation='relu'))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Conv2D(64, (3, 3), padding='same',
                     activation='relu'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Conv2D(128, (3, 3), padding='same',
                     activation='relu'))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.2))

    model.add(Flatten())
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(NUM_CLASSES, activation='softmax'))
    return model

model = cnn_model()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)

test = pd.read_csv("../input/test.csv")
test.describe()

x_test = (test / 255.0).values
x_test = np.reshape(x_test,(28000,1,28,28))
x_test.shape

predictions = model.predict(x_test)

import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid('off')
    plt.imshow(np.reshape(x_test[i],(28,28)), cmap=plt.cm.binary)
    predicted_label = np.argmax(predictions[i])
    #true_label = y_test[i]
    #if predicted_label == true_label:
    #  color = 'green'
    #else:
    #  color = 'red'
    plt.xlabel("{} ".format(predicted_label),
                                  color='green')

model_name = "digit_clf_model_"+ time.strftime("%Y-%m-%d-%H%M") +".h5"
model.save_weights("models/"+model_name)

# f=open("submissions.csv","w")
# # Write headers
# f.write("ImageId,Label\n")
# for key,p in enumerate(predictions):
#     i = key+1
#     line = str(i)+","+str(np.argmax(p))+"\n"
#     f.write(line)
# f.close()
# sub = pd.read_csv("submissions.csv")
# sub.head()
