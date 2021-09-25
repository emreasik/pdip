import os

from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

from .service_provider import ServiceProvider


class DependencyContainer:
    Instance: ServiceProvider = None
    Base = declarative_base(metadata=MetaData())

    @classmethod
    def initialize_service(cls, root_directory):
        cls.Instance = ServiceProvider(root_directory)
        cls.Instance.import_controllers()
        cls.Instance.initialize_injection()

        return DependencyContainer

    @classmethod
    def cleanup(cls):
        del cls.Base
        cls.Base = declarative_base(metadata=MetaData())
        del cls.Instance
