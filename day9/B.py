with open("input.txt","r") as f:
    data = f.readline()

class Block:
    def __init__(self,id,size):
        self.id = id
        self.size = size

    def isFree(self):
        return self.id==-1
    
    def makeFree(self):
        self.id = -1

    def copy(self):
        return Block(self.id,self.size)
    
    def occupyFree(self,dataBlock):
        freeBlockSize = self.size - dataBlock.size
        if freeBlockSize > 0:
            newFreeBlock = Block(-1,self.size-dataBlock.size)
            return [dataBlock.copy(),newFreeBlock]
        else:
            return [dataBlock.copy()]

class Disk:
    def __init__(self,data):
        self.data = []
        self.maxId = 0
        for idx,count in enumerate(data):
            if count=='0':
                continue
            if idx%2==0:
                self.data.append(Block(idx//2,int(count)))
                self.maxId = idx//2
            else:
                self.data.append(Block(-1,int(count)))

    def __repr__(self):
        string = ""
        for block in self.data:
            if block.id==-1:
                string += '.'*block.size
            else:
                string += str(block.id)*block.size
        return string
    
    def __len__(self):
        return len(self.data)
    
    def getChecksum(self):
        idx = 0
        ans = 0
        for block in self.data:
            if block.isFree():
                idx += block.size
                continue
            for _ in range(block.size):
                ans += idx*block.id
                idx+=1
        
        return ans

disk = Disk(data)
currId = disk.maxId

while currId>0:
    right_pointer = len(disk)-1
    left_pointer = 0

    while right_pointer>=0 and disk.data[right_pointer].id != currId:
        right_pointer-=1
    
    while left_pointer<right_pointer:
        if disk.data[left_pointer].isFree() and disk.data[left_pointer].size >= disk.data[right_pointer].size:
            newBlocks = disk.data[left_pointer].occupyFree(disk.data[right_pointer])
            disk.data.pop(left_pointer)
            right_pointer-=1
            for block in newBlocks[::-1]:
                disk.data.insert(left_pointer,block)
                right_pointer+=1
            disk.data[right_pointer].makeFree()
            break
        left_pointer+=1    
    currId -= 1

print(disk.getChecksum())