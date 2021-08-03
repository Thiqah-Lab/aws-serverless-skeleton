from http import HTTPStatus

from src.app.destination.model import DestinationModel
from src.common.decorator import api_response
from src.common.exceptions import (ExceptionHandler, ItemNotFoundException)


class GetService(object):
    def __init__(self, path_param):
        self.path_param = path_param

    @api_response()
    def execute(self):
        try:
            return self._get_destination_object(destination_id=self.path_param)
        except ItemNotFoundException as ex:
            ExceptionHandler.handel_exception(exception=ex)
            return HTTPStatus.NOT_FOUND
        except DestinationModel.DoesNotExist as ex:
            ExceptionHandler.handel_exception(exception=ex)
            return HTTPStatus.NOT_FOUND

    def _get_destination_object(self, destination_id):
        destination_object = DestinationModel.get(destination_id)
        print(destination_object)
        return destination_object
