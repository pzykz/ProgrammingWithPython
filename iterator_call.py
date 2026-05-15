from iterator_class import SequenceNumber


def iterator_call():
    sequence_number = SequenceNumber(0, 3)
    # print 0
    print(next(sequence_number))
    # print 1
    print(next(sequence_number))
    # print 2
    print(next(sequence_number))
    # an error occurred: StopIteration
    print(next(sequence_number))


if __name__ == '__main__':
    iterator_call()
