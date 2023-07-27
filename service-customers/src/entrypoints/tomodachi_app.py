import uuid

import tomodachi
from adapters import dynamodb
from aiohttp import web
from customers.commands import CreateCustomerCommand
from service_layer import use_cases, views
from service_layer.response import CreateCustomerResponse
from service_layer.unit_of_work import DynamoDBUnitOfWork


class TomodachiService(tomodachi.Service):
    name = "service-customers"

    async def _start_service(self) -> None:
        await dynamodb.create_dynamodb_table()

    @tomodachi.http("GET", r"/health")
    async def healthcheck(self, request: web.Request) -> web.Response:
        return web.json_response(data={"status": "ok"})

    @tomodachi.http("POST", r"/customers")
    async def create_customer(self, request: web.Request) -> web.Response:
        uow = DynamoDBUnitOfWork.create()

        data = await request.json()
        cmd = CreateCustomerCommand.from_dict(data)
        customer = await use_cases.create_customer(uow, cmd)

        response = CreateCustomerResponse.from_customer(customer)
        return web.json_response(response.to_dict())

    @tomodachi.http("GET", r"/customer/(?P<customer_id>[^/]+?)/?")
    async def get_customer(self, request: web.Request, customer_id: str) -> web.Response:
        uow = DynamoDBUnitOfWork.create()
        response = await views.get_customer(uow, customer_id=uuid.UUID(customer_id))
        return web.json_response(response.to_dict())
