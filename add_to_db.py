import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Synapps.settings")
django.setup()

from Reports.dal.report.report_type_dal import ReportTypeDal
from Reports.dal.report.report_location_dal import ReportLocationDal

REPORT_TYPES_FILE = './report_types.json'
REPORT_LOCATIONS_FILE = './report_locations.json'


def add_data_from_file(file, dal):
    print("#####################################################")
    print("File Name:  ", file)
    with open(file) as f:
        data = json.load(f)
    i = 0
    for obj in data:
        i += 1
        obj_id = obj.get("pk")
        obj_name = obj.get("fields").get("name")
        dal.create_or_update(id=obj_id, name=obj_name)
        print(i, obj_id, obj_name)


if __name__ == '__main__':
    report_type_dal = ReportTypeDal()
    report_location_dal = ReportLocationDal()

    datas = [
        (REPORT_TYPES_FILE, report_type_dal),
        (REPORT_LOCATIONS_FILE, report_location_dal)
    ]

    for data in datas:
        add_data_from_file(*data)
    