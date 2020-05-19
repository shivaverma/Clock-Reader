import keras
from keras.models import Model
from keras.layers import Conv2D, Flatten, Dense, Activation, MaxPooling2D, Dropout, Input, BatchNormalization

def get_model():

    inp = Input(shape=(100, 100, 1))

    x = Conv2D(50, kernel_size=5, strides=2, activation='relu')(inp)
    x = MaxPooling2D(pool_size=(2, 2), strides=2)(x)
    x = BatchNormalization()(x)

    x = Conv2D(100, kernel_size=3, strides=1, activation='relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = BatchNormalization()(x)

    x = Conv2D(150, kernel_size=3, strides=1, activation='relu')(x)
    x = MaxPooling2D(pool_size=(2, 2))(x)
    x = BatchNormalization()(x)

    x = Conv2D(200, kernel_size=3, strides=1, activation='relu')(x)
    x = Dropout(.4)(x)

    x = Flatten()(x)

    hour = Dense(144, activation='relu')(x)
    hour = Dense(144, activation='relu')(hour)
    hour = Dense(12, activation='softmax', name='hour')(hour)

    minute = Dense(100, activation='relu')(x)
    minute = Dense(200, activation='relu')(minute)
    minute = Dense(1, activation='linear', name='minute')(minute)

    model = Model(inputs=inp, outputs=[hour, minute])

    return model
    
