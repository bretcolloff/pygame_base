import pygame
import tensorflow as tf

""" Takes input and provides decisions for driving the simulation. """
class AIDriver:
    def __init__(self):
        self.results = []

        # The number of remaining simulation steps.
        self.next = 0
        self.last = 0

    def train_ai(self, distance, car):
        session = tf.Session()
        dist = tf.constant(distance, tf.float32)
        accelSteps = tf.Variable([70.0], tf.float32)
        accel = tf.placeholder(tf.float32) # car.accelStep
        brake = tf.placeholder(tf.float32) # car.brakeStep

        init = tf.global_variables_initializer()
        session.run(init)

        accelValues = tf.multiply(tf.range(tf.reshape(accelSteps, [])), accel)
        top = tf.reduce_max(accelValues)
        travelled = tf.reduce_sum(accelValues)
        # fff = (70 * (70 + 1) / 2) * car.accelStep

        n = session.run(travelled, {accel: car.accelStep}) # Work out the distance travelled
        topSpeed = session.run(top, {accel: car.accelStep}) # What was the last speed we were running at

        brakingSteps = tf.divide(topSpeed, brake)
        brakes = session.run(brakingSteps, {brake: car.brakeStep})

        brakeValues = tf.multiply(tf.range(brakingSteps), brake)
        brakeDistance = tf.reduce_sum(brakeValues)
        d = session.run(brakeDistance, {brake: car.brakeStep})

        loss = dist - (n + d)
        l = session.run(loss)

        optimizer = tf.train.GradientDescentOptimizer(0.01)
        train = optimizer.minimize(loss)

        z = 0.0
        for i in range(1000):
            z = session.run(train, {accel: car.accelStep, brake: car.brakeStep})

        print(z)


    #Provides input responses based on the simulation state.
    def process_input(self, velocity, success, top):
        key_map = {}
        key_map[pygame.K_SPACE] = False
        key_map[pygame.K_RIGHT] = False
        key_map[pygame.K_LEFT] = False

        # If we applied too much power, try less next time.
        if success is False:
            key_map[pygame.K_SPACE] = True
            self.next = self.last - 2
            self.last = self.last - 2
            return key_map
        else:
            if self.next is 0 and velocity is 0:
                self.results.append((self.last, top))
                self.next = self.last + 1
                self.last = self.last + 1
                key_map[pygame.K_SPACE] = True
                return key_map
            if self.next > 0:
                self.next -= 1
                key_map[pygame.K_RIGHT] = True
                return key_map

            # Put the brakes on.
            if self.next is 0 and velocity > 0:
                key_map[pygame.K_LEFT] = True
        return key_map
