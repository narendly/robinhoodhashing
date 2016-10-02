###################################################################
# KPCB Engineering Fellows Program - Challenge Problem Submission #
# Applicant: Hunter Lee                                           #
# Email: hl130@duke.edu                                           #
###################################################################
import string
import random
import statistics
import time
from HashMapRH import HashMap as robinhood
from HashMap import HashMap as naive


def value_generator(num_char=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(num_char))

size = 50000

# Initialize
naive_model = naive(size)
robinhood_model = robinhood(size)

# Add key/value pairs
values = []
for i in range(size):
    value = value_generator()
    naive_model.set(str(i), value)
    robinhood_model.set(str(i), value)
    values.append(value)

# Time it
dummy = 0
index = str(random.randint(0, size))

# naive get
start = time.clock()
dummy = naive_model.get(index)
end = time.clock()
t_naive_get = end - start

# naive delete
start = time.clock()
dummy = naive_model.delete(index)
end = time.clock()
t_naive_delete = end - start
naive_model.set(index, values[int(index)])

# robinhood get
start = time.clock()
dummy = robinhood_model.get(index)
end = time.clock()
t_robinhood_get = end - start

# robinhood delete
start = time.clock()
dummy = robinhood_model.delete(index)
end = time.clock()
t_robinhood_delete = end - start
robinhood_model.set(index, values[int(index)])

# Print statistics (variance)
naive_variance = statistics.variance(naive_model.probe_lengths)
robinhood_variance = statistics.variance(robinhood_model.probe_lengths)
print()
print("Variance in probe lengths: 1) Naive: {}  2) Robin Hood Hashing: {}".format(naive_variance, robinhood_variance))
print("Robin Hood Hashing has lower variance. Difference in variance: {}".format(naive_variance - robinhood_variance))
print()
print("Performance - get(key): 1) Naive: {}  2) Robin Hood Hashing: {}".format(t_naive_get, t_robinhood_get))
print("Performance - delete(key): 1) Naive: {}  2) Robin Hood Hashing: {}".format(t_naive_delete, t_robinhood_delete))
print("For get(key), Robin Hood Hashing is faster by {} seconds".format(t_naive_get - t_robinhood_get))
print("For delete(key), Robin Hood Hashing is faster by {} seconds".format(t_naive_delete - t_robinhood_delete))
print()
