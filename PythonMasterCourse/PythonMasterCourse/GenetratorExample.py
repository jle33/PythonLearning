import random
#Generator Example
def get_data():
    """Return 3 random integers between 0 and 9"""
    print("At get_data()")
    return random.sample(range(10), 3)

def consume():
    """Displays a running average across lists of integers sent to it"""
    running_sum = 0
    data_items_seen = 0
    print("At top of consume()")

    while True:
        print("Calling consume() Yield")
        data = yield #Saves current state and sends control back to the caller. Resumes at this spot when a callee calls send #Resumes here
        print("At consume() after send({}) was called".format(data))
        data_items_seen += len(data) 
        running_sum += sum(data)
        print('The running average is {}'.format(running_sum / float(data_items_seen)))

def produce(consumer):
    """Produces a set of values and forwards them to the pre-defined consumer
    function"""
    print("At top of produce()")
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        print("Before consumer.send({}) is called".format(data))
        consumer.send(data) #Saves current state and sends control to consumer
        print("Calling produce() Yield") #Resumes here
        yield
        print("At produce() after next(producer) is called")

if __name__ == '__main__':
    consumer = consume()
    print("Before consumer.send(none)")
    consumer.send(None)
    producer = produce(consumer)

    for _ in range(10):
        print('Producing...')
        next(producer)