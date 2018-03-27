# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:26:23 2018

@author: wuzw
"""

import tensorflow as tf


a = tf.zeros(shape=[1,2])

a = tf.constant([4,2])

a =tf.random_shuffle([[1,2,3],[4,5,6],[6,6,6]], seed=134, name="v8_5") 

sess = tf.InteractiveSession()
print(sess.run(a))

from tensorflow.examples.tutorials.mnist import input_data

b=tf.cast(tf.reduce_mean(a,reduction_indices=[0]),tf.float64)
print(sess.run(b))
