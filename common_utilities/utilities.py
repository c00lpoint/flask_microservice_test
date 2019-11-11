from py_eureka_client import eureka_client
from socket import gethostname

from common_utilities.configs import CommonConfig


def register_eureka_service(app_name, instance_port, eureka_server=CommonConfig.EUREKA_SERVICE):
    eureka_client.init(eureka_server=eureka_server,
                       instance_port=instance_port,
                       app_name=app_name)
