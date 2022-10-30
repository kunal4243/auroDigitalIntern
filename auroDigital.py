from xml.dom import minidom
import os

file = minidom.parse('orderso.xml')
Add = file.getElementsByTagName('AddOrder')
Delete=file.getElementsByTagName('DeleteOrder')

print('model #2 attribute:')
print(Add[2].attributes['price'].value)


table =minidom.Document()
table.toprettyxml(encoding="utf-8")
xml=table.createElement('table')
table.appendChild(xml)

book=table.createElement('Book1')
xml.appendChild(book)
Sell=table.createElement('Sell')
newNode=table.getElementsByTagName( "Book1" )
newNode[0].appendChild(Sell)
Buy=table.createElement('Buy')
newNode=table.getElementsByTagName( "Book1" )
newNode[0].appendChild(Buy)

xml_str = table.toprettyxml(indent ="\t",encoding="UTF-8") 
save_path_file = "gfg.xml"
with open(save_path_file, "w") as f:
    f.write(xml_str) 


def createBook(bookName):
    file=minidom.parse('gfg.xml')
    book=file.createElement(bookName)
    file.firstChild.appendChild(book)
    Sell=file.createElement('Sell')
    newNode=file.getElementsByTagName( bookName)
    newNode[0].appendChild(Sell)
    Buy=file.createElement('Buy')
    newNode=file.getElementsByTagName( bookName )
    newNode[0].appendChild(Buy)





    with open( "gfg.xml", "w" ) as fs: 
    
            fs.write( file.toxml() )
            fs.close()


def add(book,opr,price,volume,ordId):
    file=minidom.parse('gfg.xml')
    newNode=file.getElementsByTagName( book)
    order=file.createElement(ordId)
    order.setAttribute('price', price)
    order.setAttribute('volume', volume)

    newNode=file.getElementsByTagName( book )
    if(opr=="Sell"):
        newNode[0].childNodes[0].appendChild(order)
    else:
        newNode[0].childNodes[0].appendChild(order)
    
    with open( "gfg.xml", "w" ) as fs: 
    
            fs.write( file.toxml() )
            fs.close()

def deleteNode(ordId):
    file=minidom.parse('gfg.xml')
    newNode=file.getElementsByTagName(ordId)
    
    


    with open( "gfg.xml", "w" ) as fs: 
    
            fs.write( file.toxml() )
            fs.close()




createBook("Book2")

add("Book2","Sell","34","50","1345")

