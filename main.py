from flask import Flask, render_template, request
from functions import insert_sql, getAll, edit_data, delete_data
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    bucket_list = getAll()
    if request.method == 'POST':
        data = request.form['item']
        data_to_edit = request.form['to_edit']
        data_to_delete = request.form['to_delete']
        reverting_duplicate = [item for item in bucket_list if item[1] == data]
        editing_part = [
            item for item in bucket_list if item[1] == data_to_edit]
        item_to_delete = [
            item for item in bucket_list if item[1] == data_to_delete]

        if len(reverting_duplicate) > 0:
            return render_template('index.html', list_of_items=bucket_list)
        elif len(editing_part) > 0:
            edit_data(data_to_edit, data)
            for idx, item in enumerate(bucket_list):
                itemList = list(item)
                if itemList[0] == editing_part[0][0]:
                    itemList[1] = data
                    item = tuple(itemList)
                    bucket_list[idx] = item

        elif len(item_to_delete) > 0 or item_to_delete != []:
            to_delete = item_to_delete[0][1]
            delete_data((to_delete,))
            # bucket_list.remove(tuple(item_to_delete))
            # Approach1: delete item from list by manual loop
            # idx_to_delete = -1
            # cur_idx = -1
            # for i in bucket_list:
            # 	cur_idx += 1
            # 	if i[0][0] == item_to_delete[0][0] and i[0][1] == item_to_delete[0][1]:
            # 		# bucket_list.remove(i)
            # 		idx_to_delete = cur_idx
            # if idx_to_delete != -1:
            # 	del bucket_list[idx_to_delete]

            # # Approach2: delete item from list using iterator index
            # idx_to_delete = -1
            # for cur_idx,item in enumerate(bucket_list):
            # 	if item[0][0] == item_to_delete[0][0] and item[0][1] == item_to_delete[0][1]:
            # 		# bucket_list.remove(i)
            # 		idx_to_delete = cur_idx
            # if idx_to_delete != -1:
            # 	del bucket_list[idx_to_delete]

            # # Approach3: remove item from list using lambda syntax + filter
            # filtered_iterator = filter(lambda item: not (item[0][0] == item_to_delete[0][0] and item[0][1] == item_to_delete[0][1]), bucket_list)
            # bucket_list = list(filtered_iterator)

            # Approach4: remove item from list using list comprehension
            bucket_list = [item for item in bucket_list if (
                item[0] != item_to_delete[0][0] and item[0] != item_to_delete[0][1])]

        elif data != "":
            insert_sql((data,))
            bucket_list.insert(0,(0,data))




    return render_template('index.html', list_of_items=bucket_list)


if __name__ == '__main__':    app.run(debug=True, port=3001)
