from abc import ABC, abstractmethod


class BaseEmbedding(ABC):
    @abstractmethod
    def get_embeddings(self, text, **kwargs):
        """
        Generate embeddings for a given text.

        :param text: A string or a list of strings for which to generate embeddings.
        :return: The generated embeddings.
        """
        pass

    @property
    @abstractmethod
    def dimension(self):
        """
        Returns the size (number of dimensions) of the embeddings generated by this model.

        :return: An integer representing the size of the embeddings.
        """
        return 0
