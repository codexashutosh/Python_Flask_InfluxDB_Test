from flask import jsonify, Blueprint
import time
from influxdb_client import Point
from influxdb_client.client.write_api import SYNCHRONOUS
from connect import create_client

client = create_client()
bucket = "bulk_data"

data_api = Blueprint('data_api', __name__)


@data_api.route('/setData', methods=['GET'])
def set_data():
    write_api = client.write_api(write_options=SYNCHRONOUS)
    message = "Data Saved Successfully"
    try:
        for i in range(5):
            field_name = "field" + str(i)
            val = i * 10
            point = Point("measurement1").field(field_name, val)
            write_api.write(bucket=bucket, org="ashutosh-org", record=point)
            time.sleep(1)
    except Exception as e:
        message = "[ERROR] " + str(e)
    return message


@data_api.route('/getData', methods=['GET'])
def get_data():
    try:
        data = []
        query_api = client.query_api()

        query = """from(bucket: "bulk_data")
             |> range(start: -10m)
             |> filter(fn: (r) => r._measurement == "measurement1")"""
        tables = query_api.query(query, org="ashutosh-org")

        for table in tables:
            for record in table.records:
                print(record, end="\n\n")
                data += [[record.values["_field"], record.values["_time"], record.values["_value"],
                          record.values["_measurement"]]]
        message = jsonify(data)
    except Exception as e:
        message = "[ERROR] " + str(e)
    return message
