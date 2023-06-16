from influxdb_client import InfluxDBClient


def create_client():
    token = "Ry7tP-Fg8l4uSy_HkHO7Uyc1TYcVYtv1P9xa8MNyCzmD6zW9B5HxPZnDYjN0Q3htTlxIKgWH-H0AaJyMUP3oVw=="
    org = "ashutosh-org"
    url = "http://localhost:8086"

    client = InfluxDBClient(url=url, token=token, org=org)
    return client
