from mrjob.job import MRJob

class MRCustomerPurchase(MRJob):

    def mapper(self, _, line):
        (customer, item, purchase) = line.split(',')
        yield customer, float(purchase)

    def reducer(self, customer,purchase):
            
        yield customer,sum(purchase)


if __name__ == '__main__':
    MRCustomerPurchase.run()