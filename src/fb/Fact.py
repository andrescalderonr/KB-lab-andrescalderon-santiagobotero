from __future__ import annotations
from src.enums import Value

class Fact:
  """ definicion de hechos bajo el lenguaje establecido y su sintaxis
  """

  @classmethod
  def fact(cls, proposition: str, value: Value, source: str):
    """ establece un nuevo hecho
    Args:
      proposition: nombre de la proposicion
      value: valor que toma la proposición
      source: fuente que dio el valor para la proposicion: usuario o regla
    Returns:
    """
    pass

  def to_string(self) -> str:
    """ muestra la expresión de un hecho en el lenguaje
    Args:
    Returns:
      hecho en lenguaje natural: nombre, valor y fuente que permitio conocer su valor
    """
    pass