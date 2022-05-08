auction_dic={}
bidding_finnished = False
new_val = 0
while bidding_finnished == False:
    name = input("enter name\n")
    bid = input("enter bidding price\n")
    auction_dic[name]=bid
    bidding_f = input ("is bidding finnished? y/n\n")
    if bidding_f == "n":
        bidding_finnished = False
    elif bidding_f == "y":
        bidding_finnished = True
    for things in auction_dic:
        if (int(auction_dic[things]) > int(new_val)):
            new_val = int(auction_dic[things])   
            print ("greatest value is {}".format(new_val))
input()