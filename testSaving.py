import csv


def write_to_csv(data, filename='./data.csv', has_header=False):
    print("saving beginning....")
    """
    将数据写入CSV文件。

    :param data: 要写入的数据，格式为列表的列表。
    :param filename: CSV文件的名称。
    :param has_header: 是否写入标题行，默认为False。
    """
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if has_header and data:
            writer.writerow('x')  # 写入标题行
            for row in data[1:]:  # 写入数据行
                writer.writerow(row)
        else:
            for row in data:
                writer.writerow(row)

    print("saving end....")


data = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

write_to_csv(data, './data.csv', True)
