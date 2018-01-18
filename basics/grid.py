def plusHyphen():
    print '+','-'*4,'+','-'*4,'+','-'*4,'+','-'*4,'+'

def spacedVirt():
    print '|',' '*4,'|',' '*4,'|',' '*4,'|',' '*4,'|'

def createGrid():
    plusHyphen()
    spacedVirt()
    spacedVirt()
    spacedVirt()
    spacedVirt()
    plusHyphen()
    spacedVirt()
    spacedVirt()
    spacedVirt()
    spacedVirt()
    
def createLargeGrid():
    createGrid()
    createGrid()
    plusHyphen()
            
createLargeGrid()
