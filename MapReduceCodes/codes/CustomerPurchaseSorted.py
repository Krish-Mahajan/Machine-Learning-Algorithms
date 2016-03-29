
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRCustomerPurchase(MRJob):
    
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_purchases,
                   reducer=self.reducer_sum_purchases),
            MRStep(mapper=self.mapper_make_purchases_key,
                   reducer = self.reducer_purchases_sort)
        ]

    def mapper_get_purchases(self, _, line):
        (customer, item, purchase) = line.split(',')
        yield customer, float(purchase)

    def reducer_sum_purchases(self, customer,purchase):
        yield customer,sum(purchase)
        
    def mapper_make_purchases_key(self,customer,totalpurchase):
        yield '%04.02f'%float(totalpurchase),customer  

    def reducer_purchases_sort(self,totalpurchase,customer):
        for id in customer:
            yield totalpurchase,customer

if __name__ == '__main__':
    MRCustomerPurchase.run()