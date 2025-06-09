from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.optimizers import Adam
from clearml import Task

import time
import tensorflow as tf
import numpy as np


task = Task.init(project_name='TiOp project', task_name='Optimized hyperparameters test', output_uri=True)
logger = task.get_logger()
# General/model_name: resnet101
#   General/img_shape: 128.0
#   General/batch_size: 48.0
#   General/transfer_learning: False
#   General/normalization: False
#   General/augmentation: False
#   General/dropout: 0.2
#   General/extra_data: False
#   General/epochs: 10.0

params = {
    "model_name": "mobilenet",
    "img_shape": (128, 128),
    "batch_size": 48,
    "transfer_learning": False,
    "normalization": False,
    "augmentation": False,
    "dropout": 0.4,
    "extra_data": False,
    "epochs": 5,
}

task.connect(params)


def load_data():
    train_ds = tf.keras.utils.image_dataset_from_directory(
        'madagaskar',
        seed=123,
        image_size=params["img_shape"],
        batch_size=params["batch_size"],
        validation_split=0.2,
        subset='training'
    )

    val_ds = tf.keras.utils.image_dataset_from_directory(
        'madagaskar',
        seed=123,
        image_size=params["img_shape"],
        batch_size=params["batch_size"],
        validation_split=0.2,
        subset='validation'
    )

    return train_ds, val_ds

train_ds, val_ds = load_data()
class_names = train_ds.class_names
class_count= len(class_names)

logger.report_text(f"Number of classes: {class_count}")
logger.report_text(f"Class names: {class_names}")
logger.report_text(f"Train set size (batches): {train_ds}")
logger.report_text(f"Validation set size (batches): {val_ds}")
logger.report_text(f"Image shape: {params['img_shape']}")
logger.report_text(f"Batch size: {params['batch_size']}")

# def preprocess_dataset(ds, is_training=True):
#     AUTOTUNE = tf.data.AUTOTUNE
#
#     def extra_augment(image, label):
#         image = tf.image.resize(image, [params["img_shape"][0] + 4, params["img_shape"][1] + 4])
#         image = tf.image.random_crop(image, size=[params["img_shape"][0], params["img_shape"][1], 3])
#         image = tf.image.random_brightness(image, max_delta=0.2)
#         image = tf.image.random_contrast(image, lower=0.8, upper=1.2)
#         return image, label
#
#     if is_training:
#         ds = ds.unbatch()
#
#         if params["augmentation"]:
#             augmentation_layers = tf.keras.Sequential([
#                 layers.RandomFlip("horizontal"),
#                 layers.RandomRotation(0.1),
#                 layers.RandomZoom(0.1),
#             ])
#             ds = ds.map(lambda x, y: (augmentation_layers(x, training=True), y), num_parallel_calls=AUTOTUNE)
#
#         if params["extra_data"]:
#             new_ds = ds.map(extra_augment, num_parallel_calls=AUTOTUNE)
#             ds = ds.concatenate(new_ds)
#
#         ds = ds.batch(params["batch_size"])
#
#     if params["normalization"]:
#         normalization_layer = tf.keras.layers.Rescaling(1. / 255)
#         ds = ds.map(lambda x, y: (normalization_layer(x), y), num_parallel_calls=AUTOTUNE)
#
#     return ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
#
#
#
# train_ds = preprocess_dataset(train_ds, is_training=True)
# val_ds = preprocess_dataset(val_ds, is_training=False)

def preprocess_dataset(ds):
    if params["augmentation"]:
        augmentation_layers = tf.keras.Sequential([
            layers.RandomFlip("horizontal"),
            layers.RandomRotation(0.1),
            layers.RandomZoom(0.1),
        ])
        ds = ds.map(lambda x, y: (augmentation_layers(x, training=True), y))

    if params["normalization"]:
        normalization_layer = tf.keras.layers.Rescaling(1. / 255)
        ds = ds.map(lambda x, y: (normalization_layer(x), y))

    return ds.cache().shuffle(1000).prefetch(buffer_size=tf.data.AUTOTUNE)


train_ds = preprocess_dataset(train_ds)
val_ds = preprocess_dataset(val_ds)



def get_model(type='resnet50'):
    input_shape = (*params["img_shape"],3)

    base_model=None

    if type == 'resnet50':
        base_model = tf.keras.applications.ResNet50(
            include_top=False,
            input_shape=input_shape,
            weights='imagenet' if params["transfer_learning"] else None,
            classes=class_count,
        )

    elif type == 'vgg16':
        base_model = tf.keras.applications.ResNet50(
            include_top=False,
            weights='imagenet' if params["transfer_learning"] else None,
            input_shape=input_shape,
            classes=class_count,
        )
    elif type == 'resnet101':
        base_model = tf.keras.applications.ResNet101(
            include_top=False,
            weights='imagenet' if params["transfer_learning"] else None,
            input_shape=input_shape,
            classes=class_count,
        )
    elif type == 'inceptionv3':
        base_model = tf.keras.applications.ResNet50(
            include_top=False,
            weights='imagenet' if params["transfer_learning"] else None,
            input_shape=input_shape,
            classes=class_count,
        )
    elif type == 'mobilenet':
        base_model = tf.keras.applications.ResNet50(
            include_top=False,
            weights='imagenet' if params["transfer_learning"] else None,
            input_shape=input_shape,
            classes=class_count,
        )
    else:
        raise ValueError(f'Unknown model type: {type}')

    if params["transfer_learning"]:
        base_model.trainable = False

    x = base_model.output
    x = layers.GlobalAveragePooling2D()(x)

    if params["dropout"] > 0:
        x = layers.Dropout(params["dropout"])(x)


    predictions = layers.Dense(class_count, activation='sigmoid')(x)

    model = Model(inputs=base_model.input, outputs=predictions)


    return model


model = get_model(type=params['model_name'])
model.compile(optimizer="adam",
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

start_time=time.time()


history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=params['epochs']
)
end_time = time.time()
training_time = end_time - start_time


logger = task.get_logger()
for epoch in range(len(history.history['loss'])):
    logger.report_scalar("Loss", "train", value=history.history['loss'][epoch], iteration=epoch)
    logger.report_scalar("Loss", "val", value=history.history['val_loss'][epoch], iteration=epoch)
    logger.report_scalar("Accuracy", "train", value=history.history['accuracy'][epoch], iteration=epoch)
    logger.report_scalar("Accuracy", "val", value=history.history['val_accuracy'][epoch], iteration=epoch)

logger.report_scalar("Training time", "Duration (s)", value=training_time, iteration=0)

task.close()

from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
def evaluate_model(val_ds, model):
    y_pred = []
    y_true = []

    for batch_images, batch_labels in val_ds:
        predictions = model.predict(batch_images, verbose=0)
        y_pred = y_pred + np.argmax(tf.nn.softmax(predictions), axis=1).tolist()
        y_true = y_true + batch_labels.numpy().tolist()

    cm = confusion_matrix(y_true, y_pred)
    print(classification_report(y_true, y_pred, target_names=class_names))

    return cm

cm = evaluate_model(val_ds, model)

import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot()
plt.show()

import matplotlib.pyplot as plt

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(1, params['epochs'] + 1)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='Training accuracy')
plt.plot(epochs_range, val_acc, label='Validation accuracy')
plt.legend(loc='lower right')
plt.title('Training and validation accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training loss')
plt.plot(epochs_range, val_loss, label='Validation loss')
plt.legend(loc='upper right')
plt.title('Training and validation loss')
plt.xlabel('Epoch')
plt.ylabel('Strata')

plt.tight_layout()
plt.show()

# # Następnie możesz wywołać evaluate_model()
# cm = evaluate_model(val_ds, model)