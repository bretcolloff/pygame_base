import tensorflow as tf

def print_tensorboard(sess, tensor, feed):
        # add this line to use TensorBoard.
        writer = tf.summary.FileWriter('./graphs', sess.graph)
        print(sess.run(tensor, feed))
        writer.close()
