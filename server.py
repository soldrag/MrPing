import asyncio


async def receiver():
    pass


def run_server(host: str, port: int):
    class ClientServerProtocol(asyncio.Protocol):

        def connection_made(self, transport) -> None:
            self.transport = transport

        def data_received(self, data: bytes) -> None:
            resp = data.decode()
            print(resp)
            #self.transport.write(b"hello")

    def resonse_handler(data):
        data.decode()

    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, str(host), port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if __name__ == "__main__":
    run_server("127.0.0.1", 8787)
