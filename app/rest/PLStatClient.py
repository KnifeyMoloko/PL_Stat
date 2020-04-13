from app.rest.rest_client import RestClient


class PLStatClient:
    def __init__(self,
                 ssl: bool,
                 host: str = None,
                 endpoint: str = None,
                 api_key: str = None):
        self.__client = RestClient(ssl=ssl,
                                   host="bdl.stat.gov.pl",
                                   endpoint="/api/v1/",
                                   api_key=api_key)

    @property
    def client(self) -> RestClient:
        return self.__client

    def get_levels(self):
        path = "levels"
        headers = {"sort": "Id, Name"}
        response = self.client\
            .get(resource_path=path,
                 additional_headers=headers)
        return response
