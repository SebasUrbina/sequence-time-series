# %%
import tensorflow as tf

dataset = tf.data.Dataset.range(10)
dataset = dataset.window(5, shift=1, drop_remainder=True)
dataset = dataset.flat_map(lambda window: window.batch(5))
dataset = dataset.map(lambda window: (window[:-1], window[-1]))
dataset = dataset.shuffle(buffer_size=10)
# dataset = dataset.batch(2).prefetch(1) # Create 3 batchs of size 2 

for x,y in dataset:
    print(x.numpy(), y.numpy())

## Output
# [1 2 3 4] 5
# [3 4 5 6] 7
# [5 6 7 8] 9
# [4 5 6 7] 8
# [0 1 2 3] 4
# [2 3 4 5] 6
# %%
