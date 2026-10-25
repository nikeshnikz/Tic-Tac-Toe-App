def borrow_book(has_card,ovedue_count,in_stock):
    if has_card :
        if ovedue_count==0 :
            if in_stock :
                return "Approved "
            else :
                return "Error : Book is currently out of stock"
        else :
            return "your card is overdue"
    else :
        return "Error : no library card found"

print(borrow_book(True,0,False))

