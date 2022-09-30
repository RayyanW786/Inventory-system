from dataclasses import dataclass
from typing import Union, Iterable


@dataclass
class InventoryItem:
    name: str
    attack: int = 0
    defence: int = 0
    quantity: int = 0
   # attrs = ["name", "attack", "defence", "quantity"]

   # def add_attribute(self, name: str, val: Union[int, str]) -> None:
   #     setattr(self, name, val)
   #     self.attrs.append(str(name))

   # def __dir__(self) -> Iterable[str]:
   #     return self.attrs
