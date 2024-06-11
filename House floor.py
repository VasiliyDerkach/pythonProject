class House:
    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self,floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

if __name__=='__main__':
    shome= House()
    shome.setNewNumberOfFloors(19)