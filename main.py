from leboncoin_wrapper import wrapper
from item import item
from database import database

def main():
    leboncoin = wrapper.Wrapper()
    item_type = "appartement"
    results = leboncoin.get_research("10",item_type)["ads"]
    #print_item(results[0])
    print("gonna create table")
    connection = database.create_connection("./database/leboncoin.db")
    database.creat_table(connection)
    print("creation complete")
    print("gonna add all items")
    for result in results:
        item_to_add = item.Item(result)
        database.insert_if_not_exist(connection,item_to_add, item_type)
    print("insert done !")

    #leboncoin.print_item(results[0])
    #leboncoin.export_to_excel(results,"test_result.csv")
    """for result in results:
        if "price" not in result:
            leboncoin.print_item(result)
        else:
            if result["price"][0] == 0:
                leboncoin.print_item(result)"""


def print_item(i):
    item_to_print = item.Item(i)
    item_to_print.do_print()

if __name__ == '__main__':
    main()