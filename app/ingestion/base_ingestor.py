from abc import ABC, abstractmethod

import pandas as pd


class BaseIngestor(ABC):

    @abstractmethod
    def extract(self):

        pass

    @abstractmethod
    def validate(self, df):

        pass

    @abstractmethod
    def load(self, df):

        pass
