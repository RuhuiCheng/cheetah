from src.utils import enum

def test_enum():
    layer = enum.etl_layer
    for item in layer:
        print(item.name)