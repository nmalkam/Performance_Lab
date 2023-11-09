def report_values(tests, values):
    import json

    def nested_dict(main_dict):
        if main_dict['id'] in testid_dic.keys():
            main_dict['value'] = testid_dic[main_dict['id']]

        for k, v in main_dict.items():
            if isinstance(v, list):
                for itm in v:
                    nested_dict(itm)

    with open(tests, encoding='UTF-8') as tests:
        tests_records = json.load(tests)

    with open(values, encoding='UTF-8') as values:
        values_records = json.load(values)

    values_records_dic = values_records['values']
    tests_records_dic = tests_records['tests']

    testid_dic = {}

    for dic in values_records_dic:
        testid_dic[dic['id']] = dic['value']

    for item in tests_records_dic:
        if item['id'] in testid_dic.keys():
            item['value'] = testid_dic[item['id']]
        nested_dict(item)
    new_records = tests_records_dic

    with open('report.json', 'w', encoding="UTF-8") as report:
        json.dump(new_records, report, ensure_ascii=False, indent=2)


def main():
    import os

    current_directory = os.path.dirname(os.path.abspath(__file__))
    tests = current_directory + "\\tests.json"
    values = current_directory + "\\values.json"

    report_values(tests, values)


if __name__ == '__main__':
    main()
