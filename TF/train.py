import tensorflow as tf
import reader
gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
class_dim = 10
EPOCHS = 100
BATCH_SIZE=32

model = tf.keras.models.Sequential([
    tf.keras.applications.ResNet50V2(include_top=False, weights=None, input_shape=(128, None, 1)),
    tf.keras.layers.ActivityRegularization(l2=0.5),
    tf.keras.layers.Dropout(rate=0.5),
    tf.keras.layers.GlobalMaxPooling2D(),
    tf.keras.layers.Dense(units=class_dim, activation=tf.nn.softmax)
])

model.summary()


# 定义优化方法
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-3)

train_dataset = reader.train_reader_tfrecord('dataset/train.tfrecord', EPOCHS, batch_size=BATCH_SIZE)
test_dataset = reader.test_reader_tfrecord('dataset/test.tfrecord', batch_size=BATCH_SIZE)