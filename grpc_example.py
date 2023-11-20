from __future__ import print_function

import logging
import os

# Generated code needs the following aliases to be done manually.
import collections.abc
collections.Iterable = collections.abc.Iterable
collections.Mapping = collections.abc.Mapping
collections.MutableSet = collections.abc.MutableSet
collections.MutableMapping = collections.abc.MutableMapping

# GRPC generated code imports.
import grpc
from stargate.supplier.item.v1beta1 import supplier_item_service_pb2_grpc
from stargate.supplier.item.v1beta1 import supplier_item_service_pb2
from stargate.type.v1 import uuid_pb2

# Set grpc log verbosity level.
os.environ["GRPC_VERBOSITY"] = "DEBUG"

# Address to connect to.
ADDR2 = "10.200.0.49:80"

# example uuid = "C3ECA1AE-BF47-4C14-AF8D-4991306C98AA" (stage).
def list_items(stub):
    test = supplier_item_service_pb2.ListItemsRequest(
        supplier_uuid = uuid_pb2.UUID(value = "C3ECA1AE-BF47-4C14-AF8D-4991306C98AA")
    )

    for item in stub.ListItems(test):
        print(item.supplier_item_identifier)

def create_item(stub):
    req = supplier_item_service_pb2.CreateItemRequest(
        supplier_uuid = uuid_pb2.UUID(value = "C3ECA1AE-BF47-4C14-AF8D-4991306C98AA"),
        supplier_item_identifier = "this has to be unique!1",
        item_no = "not unique, but needs to be the steps item no",
        price = 124284.23,
        stock = 1230,
    )

    # No Feedback for now unless there is an error.
    res = stub.CreateItem(req)
    print(res)

def update_item(stub):
    req = supplier_item_service_pb2.UpdateItemRequest(
        supplier_uuid = uuid_pb2.UUID(value = "C3ECA1AE-BF47-4C14-AF8D-4991306C98AA"),
        supplier_item_identifier = "this has to be unique!1",
        item_no = "not unique, but needs to be the steps item no", # Optional on this request.
        price = 124284.23, # Optional on this request.
        stock = 1230, # Optional on this request.
    )

    # No Feedback for now unless there is an error.
    res = stub.UpdateItem(req)
    print(res)

def delete_item(stub):
    req = supplier_item_service_pb2.UpdateItemRequest(
        supplier_uuid = uuid_pb2.UUID(value = "C3ECA1AE-BF47-4C14-AF8D-4991306C98AA"),
        supplier_item_identifier = "this has to be unique!1",
    )

    # No Feedback for now unless there is an error.
    res = stub.DeleteItem(req)
    print(res)

def run():
    with grpc.insecure_channel(ADDR2) as channel:
        stub = supplier_item_service_pb2_grpc.SupplierItemServiceStub(channel)
        print("-------------- ListItems --------------")
        list_items(stub)
        print("-------------- CreateItem --------------")
        create_item(stub)
        print("-------------- UpdateItem --------------")
        update_item(stub)
        print("-------------- DeleteItem --------------")
        delete_item(stub)
        print("-------------- DONE --------------")

if __name__ == "__main__":
    logging.basicConfig()
    run()