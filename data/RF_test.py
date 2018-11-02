""" Random Forest.

Implement Random Forest algorithm with TensorFlow, and apply it to classify
handwritten digit images. This example is using the MNIST database of
handwritten digits as training samples (http://yann.lecun.com/exdb/mnist/).

Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
"""

from __future__ import print_function

import tensorflow as tf
from tensorflow.contrib.tensor_forest.python import tensor_forest
from tensorflow.python.ops import resources
import sys

sys.path.append('/home/wingsby/develop/python/photovoltaicPower/')
# Ignore all GPUs, tf random forest does not benefit from it.
import os

from data.preprocess import getData, getValData, getPredictData, writePredictData

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

# Import MNIST data
from tensorflow.examples.tutorials.mnist import input_data

# mnist = input_data.read_data_sets("/tmp/data/", one_hot=False)
# X, Y = getData()
fileid = 2
# Parameters
num_steps = 10000
batch_size = 64

num_features = 11
num_trees = 2000
max_nodes = 1000

# Input and Target data
X = tf.placeholder(tf.float32, shape=[None, num_features])
# For random forest, labels must be integers (the class id)
Y = tf.placeholder(tf.float32, shape=[None])

# Random Forest Parameters
hparams = tensor_forest.ForestHParams(regression=True,
                                      num_classes=1,
                                      num_features=num_features,
                                      num_trees=num_trees,
                                      max_nodes=max_nodes).fill()

# Build the Random Forest
forest_graph = tensor_forest.RandomForestGraphs(hparams)
# Get training graph and loss
train_op = forest_graph.training_graph(X, Y)
loss_op = forest_graph.training_loss(X, Y)

# Measure the accuracy
infer_op, _, _ = forest_graph.inference_graph(X)
# correct_prediction = tf.equal(tf.argmax(infer_op, 1), tf.cast(Y, tf.int64))
accuracy_op = tf.reduce_mean(tf.abs(infer_op - Y))

# Initialize the variables (i.e. assign their default value) and forest resources
init_vars = tf.group(tf.global_variables_initializer(),
                     resources.initialize_resources(resources.shared_resources()))
# Start TensorFlow session
val_x, val_y = getValData(fileid=fileid)
test_x = getPredictData(fileid=fileid)
sess = tf.Session()
# Run the initializer
sess.run(init_vars)

# Training
i = 0
for batch_x, batch_y in getData(batch_size, fileid=fileid):  # Prepare Data
    # Get the next batch of MNIST data (only images are needed, not labels)
    _, l = sess.run([train_op, loss_op], feed_dict={X: batch_x, Y: batch_y})
    if i % 50 == 0 or i == 1:
        acc = sess.run(accuracy_op, feed_dict={X: batch_x, Y: batch_y})
        print('Step %i, Loss: %f, Acc: %f' % (i, l, acc))
    i += 1
    if i > num_steps:
        break

# Test Model
# test_x, test_y = mnist.test.images, mnist.test.labels

print("Test Accuracy:", sess.run(accuracy_op, feed_dict={X: val_x, Y: val_y}))
forecast = sess.run([infer_op], feed_dict={X: test_x})
writePredictData(forecast, fileid=fileid)
print(forecast)
