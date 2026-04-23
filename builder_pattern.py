from abc import ABC, abstractmethod
from csv import Error
from typing import Any


class Builder(ABC):
    """
    The builder interface specifies methods for creating the different parts of Product Objects.
    """

    @property
    @abstractmethod
    def product(self) -> Any:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class Product1:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {','.join(self.parts)}", end="")


class ConcreteBuilder1(Builder):
    """
    The Concrete Builder classes follow the Builder interface and provide
    specific implementations of the building steps. Your program may have
    several variations of Builders, implemented differently.
    """

    def __init__(self) -> None:
        """"""
        super().__init__()
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:

        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("PartB1")

    def produce_part_b(self) -> None:
        self._product.add("PartB1")

    def produce_part_c(self) -> None:
        self._product.add("PartC1")


class Director:
    def __init__(self) -> None:
        self._builder: Builder | None = None

    @property
    def builder(self) -> Builder | None:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        if not self.builder:
            raise Error(f"The value of builder is {self.builder}")

        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        if not self.builder:
            raise Error(f"The value of builder is {self.builder}")
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "main":
    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()
