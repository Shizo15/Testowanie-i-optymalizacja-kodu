
import tensorflow as tf
print(f"TensorFlow wersja: {tf.__version__}")
print(f"GPU dostępne: {tf.test.is_gpu_available()}")
print(f"Lista GPU: {tf.config.list_physical_devices('GPU')}")

# #set lerning on GPU/CPU
# useCPU = True  # 'CPU' or 'GPU'
#
# if (useCPU == True):
#     tf.config.set_visible_devices([], 'GPU')  # hide GPU
#     print("Aviable devides:", tf.config.get_visible_devices())
# else:
#     gpu_devices = tf.config.list_physical_devices('GPU')
#     tf.config.set_visible_devices(gpu_devices, 'GPU') # use GPU
#     print("Aviable devides GPU:", tf.config.get_visible_devices())
#
# print("Dostępne urządzenia:", tf.config.list_physical_devices('GPU'))
# print("Czy TensorFlow widzi GPU?", "Tak" if tf.test.is_gpu_available() else "Nie")


##Na razie nie potrzebne
# image_count = len(list(glob.glob('madagaskar/**/*')))
# print(f'{image_count} examples of Madagascar characters')
#
# """### Weryfikowanie rozkładu klas w bazie danych  """
#
# alex_count = len(list(glob.glob('madagaskar/Alex/*')))
# gloria_count = len(list(glob.glob('madagaskar/Gloria/*')))
# marty_count = len(list(glob.glob('madagaskar/Marty/*')))
# melman_count = len(list(glob.glob('madagaskar/Melman/*')))
# print(f'{alex_count} examples of Alex, {gloria_count} Gloria, {marty_count} Marty and {melman_count} Melman to train')
#
# """### Wyświetlanie przykładowych zdjęć"""
#
# alex = list(glob.glob('madagaskar/Alex/*'))
# PIL.Image.open(str(alex[1]))
#
# gloria = list(glob.glob('madagaskar/Gloria/*'))
# PIL.Image.open(str(gloria[4]))
#
# marty = list(glob.glob('madagaskar/Marty/*'))
# PIL.Image.open(str(marty[0]))
#
# melman = list(glob.glob('madagaskar/Melman/*'))
# PIL.Image.open(str(melman[1]))

"""# Trenowanie modelu sieci neuronowej

### Zmienne niezbędne do trenowania modelu
"""



# epochs_range = range(epochs)
#
# plt.figure(figsize=(8, 8))
# plt.subplot(1, 2, 1)
# plt.plot(epochs_range, acc, label='Training Accuracy')
# plt.plot(epochs_range, val_acc, label='Validation Accuracy')
# plt.legend(loc='lower right')
# plt.title('Training and Validation Accuracy')
#
# plt.subplot(1, 2, 2)
# plt.plot(epochs_range, loss, label='Training Loss')
# plt.plot(epochs_range, val_loss, label='Validation Loss')
# plt.legend(loc='upper right')
# plt.title('Training and Validation Loss')
# plt.show()
#
# """### Raport dotyczący jakości klasyfikacji"""

# from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
# def evaluate_model(val_ds, model):
#     y_pred = []
#     y_true = []
#
#     for batch_images, batch_labels in val_ds:
#         predictions = model.predict(batch_images, verbose=0)
#         y_pred = y_pred + np.argmax(tf.nn.softmax(predictions), axis=1).tolist()
#         y_true = y_true + batch_labels.numpy().tolist()
#
#     cm = confusion_matrix(y_true, y_pred)
#     print(classification_report(y_true, y_pred, target_names=class_names))
#
#     return cm
#
# cm = evaluate_model(val_ds, model)
#
# import matplotlib.pyplot as plt
#
# disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
# disp.plot()
# plt.show()


# elif type == 'custom':
#   base_model = Sequential([
#     layers.Rescaling(1./255, input_shape=input_shape),
#     layers.Conv2D(16, 3, padding='same', activation='relu'),
#     layers.MaxPooling2D(),
#     layers.Conv2D(32, 3, padding='same', activation='relu'),
#     layers.MaxPooling2D(),
#     layers.Conv2D(64, 3, padding='same', activation='relu'),
#     layers.MaxPooling2D(),
#     layers.Flatten(),
#     layers.Dense(128, activation='relu'),
#     layers.Dense(class_count)
#   ])