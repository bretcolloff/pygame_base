import pygame
import tensorflow as tf
import engine.ml.helpers as helpers

""" Takes input and provides decisions for driving the simulation. """
class AIDriver:
    def __init__(self):
        self.results = []

        # The number of remaining simulation steps.
        self.steps = 0

    def train_ai(self, distance, car):
        session = tf.Session()
        dist = tf.constant(distance, tf.float32)
        accelSteps = tf.Variable(65.8, tf.float32)
        accel = tf.placeholder(tf.float32) # car.accelStep
        brake = tf.placeholder(tf.float32) # car.brakeStep

        # Start the TensorFlow session.
        init = tf.global_variables_initializer()
        session.run(init)

        # Work out distance travelled with current step value and get the highest acceleration value.
        s = tf.mul(accelSteps, accel)
        a = s * tf.div(accelSteps, 2)
        # How long will we be braking for?
        b = s * ((s / brake) / 2)

        loss = dist - (a + b)

        optimizer = tf.train.GradientDescentOptimizer(0.01)
        train = optimizer.minimize(loss)

        helpers.print_tensorboard(session, loss, {accel: car.accelStep, brake: car.brakeStep})

        for x in range(100):
           session.run(train, {accel: car.accelStep, brake: car.brakeStep})

        self.steps = session.run(accelSteps)
        print (self.steps)


    #Provides input responses based on the simulation state.
    def process_input(self, velocity):
        key_map = {}
        key_map[pygame.K_SPACE] = False
        key_map[pygame.K_RIGHT] = False
        key_map[pygame.K_LEFT] = False

        # If we applied too much power, try less next time.
        if self.steps > 0:
            self.steps -= 1
            key_map[pygame.K_RIGHT] = True
        elif velocity > 0:
            key_map[pygame.K_LEFT] = True
        else:
            self.steps = 0
            key_map[pygame.K_SPACE] = True

        return key_map
