import multiprocessing

class ProsesWahana(multiprocessing.Process):

    def run(self):
        print ('called run method in %s' %self.name)
        return

if __name__ == '__main__':
    for i in range(10):
        process = ProsesWahana()
        process.start()
        process.join()
