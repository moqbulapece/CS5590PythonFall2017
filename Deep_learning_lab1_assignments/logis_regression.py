import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
# import the tensorflow and load MNIDT data to folder of data/mnist
MNIST = input_data.read_data_sets("/data/mnist", one_hot=True)
#the following  parameters are used  for the model
learn_rate = 0.01
batch_size = 127
num_epochs = 20
#  creating placeholders for features and labels
# the  image shape  in the MNIST data is  28*28 = 784 and represented by 1X784 tensor
# creating 10 classes for each image and defined by  digits 0 - 9 and each label defined by one hot vector.
X = tf.placeholder(tf.float32, [batch_size, 784])
Y = tf.placeholder(tf.float32, [batch_size, 10])

# the weights w is initiated by   random variables whose  mean value and stddev are 0 & 0.01 respectively
# bias b is started by value 0
w = tf.Variable(tf.random_normal(shape=[784, 10], stddev=0.01), name="weights")
b = tf.Variable(tf.zeros([1, 10]), name="bias")
# the value of  Y is predicted from X and w, b
# the model that returns probability distribution of possible label of the image
# through the softmax layer
# the possibility of the digits is represented by a batch_size x 10 tensor
logits = tf.matmul(X, w) + b
# the logits and softmax entropy combinedly define loss function
# use softmax cross entropy with logits as the loss function
# softmax is applied internally to compute mean cross entropy
entropy = tf.nn.softmax_cross_entropy_with_logits(logits, Y)
loss_cal = tf.reduce_mean(entropy) # computes the mean over examples in the batch
# Step 7: define training op
# the training operation is performed by  learning rate of 0.01 for the minimization of the cost
optimizer =tf.train.GradientDescentOptimizer(learn_rate=learn_rate).minimize(loss_cal)
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    n_batches = int(MNIST.train.num_examples/batch_size)
    for i in range(num_epochs): # the model is trained by  num_epochs times
        for _ in range(n_batches):
            X_batch, Y_batch = MNIST.train.next_batch(batch_size)
            sess.run([optimizer, loss_cal], feed_dict={X: X_batch, Y:Y_batch})
# after 25 epochs average loss mignt  be around 0.35
    n_batches = int(MNIST.test.num_examples/batch_size)
    total_correct_preds = 0
    for i in range(n_batches):
        X_batch, Y_batch = MNIST.test.next_batch(batch_size)
        _, loss_cal_batch, logits_batch = sess.run([optimizer, loss_cal, logits],feed_dict={X: X_batch, Y:Y_batch})
        preds = tf.nn.softmax(logits_batch)
        correct_preds = tf.equal(tf.argmax(preds, 1), tf.argmax(Y_batch, 1))
        accuracy = tf.reduce_sum(tf.cast(correct_preds, tf.float32))
        total_correct_preds += sess.run(accuracy)
    print"Accuracy {0}".format(total_correct_preds/MNIST.test.num_examples)