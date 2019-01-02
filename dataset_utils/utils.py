#from keras.preprocessing.image import ImageDataGenerator,img_to_array, load_img
import os
from google_images_download import google_images_download


def downloader(search_term="newspaper sudoku"):
    response = google_images_download.googleimagesdownload()
    absolute_image_paths = response.download({'keywords':search_term, 'limit':20, 'format':'jpg'})

def clip_images():
    pass

def dataset_gen():
    # rename, clip, grayscale and rescale
    pass


# def image_augmentor():
#     datagen = ImageDataGenerator(
#             rotation_range=10,
#             width_shift_range=0.1,
#             height_shift_range=0.1,
#             shear_range=0.1,
#             zoom_range=0.1,
#             horizontal_flip=True,
#             fill_mode='nearest')

#     train_sudoku_img_files =  os.listdir('../data/train/sudoku')
#     train_none_img_files =  os.listdir('../data/train/none')
#     for img_file in train_sudoku_img_files:
#         img = load_img('../data/train/sudoku/'+img_file)
#         x = img_to_array(img)  # creating a Numpy array with shape (3, 150, 150)
#         x = x.reshape((1,) + x.shape)  # converting to a Numpy array with shape (1, 3, 150, 150)

#         i = 0
#         for batch in datagen.flow(x,save_to_dir='preview', save_prefix='', save_format='jpeg'):
#             i += 1
#             if i > 16:
#                 break

#     for img_file in train_none_img_files:
#         img = load_img('../data/train/none/'+img_file)
#         x = img_to_array(img)  # creating a Numpy array with shape (3, 150, 150)
#         x = x.reshape((1,) + x.shape)  # converting to a Numpy array with shape (1, 3, 150, 150)

#         i = 0
#         for batch in datagen.flow(x,save_to_dir='preview', save_prefix='', save_format='jpeg'):
#             i += 1
#             if i > 16:
#                 break
#     return


downloader()