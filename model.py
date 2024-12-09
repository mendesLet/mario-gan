import tensorflow as tf

class DCGAN(object):
    def __init__(self, img_rows=16, img_cols=4, channel=4, latent_dim=46):

        self.img_rows = img_rows
        self.img_cols = img_cols
        self.channel = channel
        self.latent_dim = latent_dim
        self.D = None   # Feature Extraction (Discriminator)
        self.G = None   # Generation (Generator)
        self.AM = None  # Adversarial model
        self.DM = None  # Discriminator model

    def feature_extraction(self):
        """Feature extraction network (similar to discriminator but for latent vector)."""
        if self.D:
            return self.D

        input_shape = (self.img_rows, self.img_cols, self.channel)
        feature_input = tf.keras.Input(shape=input_shape)  # Ensure correct 4D input

        x = tf.keras.layers.Conv2D(16, kernel_size=3, strides=1, padding='same', activation='relu')(feature_input)
        x = tf.keras.layers.Conv2D(32, kernel_size=3, strides=1, padding='same', activation='relu')(x)
        x = tf.keras.layers.Flatten()(x)  # Flatten to 1D for latent vector

        # Latent vector
        latent_vector = tf.keras.layers.Dense(self.latent_dim, activation='relu')(x)

        self.D = tf.keras.Model(feature_input, latent_vector, name="Feature_Extraction")
        self.D.summary()
        return self.D


    def generator(self):
        """Generator network."""
        if self.G:
            return self.G
        
        # Input: latent vector and feature extraction output
        latent_input = tf.keras.Input(shape=(self.latent_dim,))
        feature_input = tf.keras.Input(shape=(self.img_rows, self.img_cols, self.channel))
        
        # Concatenate latent vector and reshaped feature input
        combined = tf.keras.layers.Concatenate()([latent_input, tf.keras.layers.Flatten()(feature_input)])
        
        # Dense layer to reshape the concatenated input
        x = tf.keras.layers.Dense(self.img_rows * self.img_cols * 32, activation='relu')(combined)
        x = tf.keras.layers.Reshape((self.img_rows, self.img_cols, 32))(x)
        
        # Transposed convolutions for generation
        x = tf.keras.layers.Conv2DTranspose(64, kernel_size=3, strides=1, padding='same', activation='relu')(x)
        x = tf.keras.layers.Conv2DTranspose(32, kernel_size=3, strides=1, padding='same', activation='relu')(x)
        x = tf.keras.layers.Conv2DTranspose(16, kernel_size=3, strides=1, padding='same', activation='relu')(x)
        generated_output = tf.keras.layers.Conv2D(self.channel, kernel_size=3, padding='same', activation='sigmoid')(x)
        
        self.G = tf.keras.Model([latent_input, feature_input], generated_output, name="Generator")
        self.G.summary()
        return self.G

    def discriminator_model(self):
        """Feature extraction model."""
        if self.DM:
            return self.DM
        optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.0002)

        feature_extractor = self.feature_extraction()  # Uses feature extraction model
        self.DM = tf.keras.Model(feature_extractor.input, feature_extractor.output, name="Discriminator_Model")
        self.DM.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
        return self.DM

    def adversarial_model(self):
        """Adversarial model combines generator and feature extraction."""
        if self.AM:
            return self.AM
        optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.0001)
        
        generator = self.generator()
        feature_extractor = self.feature_extraction()
        
        # Adversarial model takes a latent vector and raw feature input
        latent_input = tf.keras.Input(shape=(self.latent_dim,))
        feature_input = tf.keras.Input(shape=(self.img_rows, self.img_cols, self.channel))
        
        generated_output = generator([latent_input, feature_input])
        classification = feature_extractor(generated_output)
        
        self.AM = tf.keras.Model([latent_input, feature_input], classification, name="Adversarial_Model")
        self.AM.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])
        return self.AM
