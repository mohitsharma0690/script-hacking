import numpy as np
import tensorflow as tf

def create_network(N=5, structure=(5, 3), learning_rate=0.01):

  inp_pl = tf.placeholder(tf.float32, shape=(N, 1))
  prev_layer = inp_pl
  for i in xrange(len(structure)):
    output = tf.layers.dense(prev_layer,
                             structure[i],
                             activation=tf.nn.relu,
                             kernel_initializer=None,
                             use_bias=True,
                             name='dense_' + str(i))
    prev_layer = output
  y = tf.layers.dense(prev_layer, 1, activation=None, use_bias=False)
  y = tf.reshape(y, [-1])

  trainable_vars = tf.trainable_variables()

  grads_pl = tf.placeholder(tf.float32, shape=(N,))
  # Backprop for the main graph
  grads = tf.gradients(y,
                       trainable_vars,
                       grad_ys=grads_pl)

  grads_and_vars = list(zip(grads, trainable_vars))
  optimizer = tf.train.AdamOptimizer(learning_rate)
  train_op = optimizer.apply_gradients(grads_and_vars)

  return inp_pl, grads_pl, y, train_op


def main(num_iters=100, learning_rate=1e-2, N=5):
  inp_pl, grads_pl, output, train_op = create_network(N=N,
      learning_rate=learning_rate)

  # Initialize
  config = tf.ConfigProto()
  config.gpu_options.allow_growth=True
  sess = tf.Session(config=config)
  sess.run(tf.global_variables_initializer())

  for i in xrange(num_iters):
    X = np.random.rand(N)
    Y = np.square(X)

    Y_hat, = sess.run([output], feed_dict={inp_pl: X[:, np.newaxis]})
    grad = (-2.0/N)*(Y - Y_hat)

    sess.run([output, train_op],
             feed_dict={
               inp_pl: X[:, np.newaxis],
               grads_pl: np.array(grad),
               })
    if i % 500 == 0:
      print('=====')
      print(np.array_str(np.vstack([X, Y, Y_hat]).T, precision=4,
                         suppress_small=True))
      print('=====')


if __name__ == '__main__':
  main(num_iters=50000, learning_rate=1e-4)
