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
        accelSteps = tf.Variable(80.0, tf.float32)
        accel = tf.placeholder(tf.float32) # car.accelStep
        brake = tf.placeholder(tf.float32) # car.brakeStep

        # Start the TensorFlow session.
        init = tf.global_variables_initializer()
        session.run(init)

        # Work out distance travelled with current step value and get the highest acceleration value.
        accelValues = tf.multiply(tf.range(accelSteps), accel)
        top = tf.reduce_max(accelValues)
        travelled = tf.reduce_sum(accelValues)

        topSpeed = session.run(top, {accel: car.accelStep}) # What was the last speed we were running at

        # How long will we be braking for?
        brakingSteps = tf.divide(topSpeed, brake)
        brakeValues = tf.multiply(tf.range(brakingSteps), brake)

        # How far will we travel while braking?
        brakeDistance = tf.reduce_sum(brakeValues)

        loss = dist - (travelled + brakeDistance)
        a = session.run(loss, {accel: car.accelStep, brake: car.brakeStep})

        optimizer = tf.train.GradientDescentOptimizer(0.01)
        train = optimizer.minimize(loss, var_list=[accelSteps])

        z = 100.0
        while z > 0.5:
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
