from __future__ import annotations
from src.enums import Value

class Fact:
  """Definition of facts in the language."""
  proposition: str
  value: Value
  source: str

  @classmethod
  def fact(cls, proposition: str, value: Value, source: str):
      """
      Creates a Fact object WITHOUT calling a constructor.
      Attributes are attached dynamically.
      """
      obj = cls()
      obj.proposition = proposition
      obj.value = value
      obj.source = source
      return obj

  def to_string(self) -> str:
    """
    Returns the natural-language representation of the fact.
    """
    return f"{self.proposition} = {self.value.name} (source: {self.source})"