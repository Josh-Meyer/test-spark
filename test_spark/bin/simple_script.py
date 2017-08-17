import os

from pyspark import SparkContext


if __name__ == '__main__':
    sc = SparkContext('local', 'Simple Script')

    derby_log_path = os.path.abspath(os.path.join(
        __file__, '../../../derby.log'))
    log_data = sc.textFile(derby_log_path).cache()

    number_of_As = log_data.filter(lambda s: 'a' in s).count()
    print 'number_of_As:', number_of_As
    number_of_Bs = log_data.filter(lambda s: 'b' in s).count()
    print 'number_of_Bs:', number_of_Bs
