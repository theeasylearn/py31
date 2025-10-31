import random

print(random.random())
#o/p:0.13525954806246865

print(random.uniform(10,90))
#o/p:48.03574630531223

print(random.randint(10,90))
#o/p:33

print(random.randrange(0,100,5))
#o/p:15

fruit=['apple','banana','watermelon','papaya']
print(random.choice(fruit))
#o/p:papaya

print(random.choices(fruit,k=2))
#o/p:['papaya', 'watermelon']

print(random.shuffle(fruit))
#o/p:None

print(fruit)
#o/p:['banana', 'apple', 'papaya', 'watermelon']

print(random.sample(fruit,4))
#o/p:['apple', 'papaya', 'banana', 'watermelon']

print(fruit)
#o/p:['banana', 'apple', 'papaya', 'watermelon']
