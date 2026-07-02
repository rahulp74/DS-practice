"""H1) An Amazon fulfilment centre has a conveyor belt with exactly 8 slots
numbered 0–7. Each slot holds one product. The warehouse manager needs to:
check what's at a slot, find a product, update a slot, and check if the belt is full.
The conveyor belt — fixed 8 slots"""

size=8
p_list=[]

def push(product):
    if len(p_list)==size:
        print("Belt is Full")
    else:
        p_list.append(product)
        print(f"{product} is add..")
        
def peek():
    if p_list:
        print(f"top product {p_list[0]}")
    else:
        print("Belt is empty")
        
def update(product):
    if p_list:
        p_list[0]=product
        print("top product updated")
        print(p_list)
    else:
        print("Belt is empty")
    
def is_full():
    if len(p_list)==size:
        print("Belt is Full")
    else:
        
        print("space is available")
push('laptop')
push("phone")
peek()
update('table')
is_full()