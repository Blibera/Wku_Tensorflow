import tensorflow as tf

"""
a = tf.constant([1, 2, 3])
b = tf.constant([3, 4, 5])

print(tf.add(a, b))
"""

a = tf.constant([1, 2, 3])
b = tf.constant([3, 4, 5])
adding = tf.add(a, b)

sess = tf.Session()
print(sess.run(adding))
