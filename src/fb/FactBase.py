from __future__ import annotations
from src.enums import Value
from Fact import Fact

class FactBase:
  """ base de conocimiento a partir de reglas bajo la sintaxis pertinente
  """
  @classmethod
  def fact_base(cls):
    """ establece una base de hechos bajo el lenguaje
    Args:
    Returns:
    """
    pass

  def add_fact(self, proposition: str, value: Value, source: str):
    """ establece una nueva base de hechos en la sintaxis
    Args:
      proposition: nombre de la proposicion
      value: valor de la proposición
      source: source: fuente que dio el valor para la proposicion: usuario o regla
    Returns:
    """
    pass

  def get_value(self, proposition: str) -> Value:
    """ obtiene el valor de una proposición
    Args:
      proposition: nombre de la proposicion
    Returns:
      valor semántico de la regla
    """
    pass

  def ask_value(self, proposition: str) -> Value:
    """ le pregunta al usuario el valor de una proposición
    Args:
      proposition: nombre de la proposicion
    Returns:
      valor semántico de la regla
    """
    pass

  def num_facts(self) -> int:
    """ determina cantidad de hechos en la base
    Args:
    Returns:
      número de hechos
    """
    pass

  def get_fact(self, f: int) -> Fact:
    """ obtiene el hecho según su indicador
    Args:
      f: indice del hecho
    Returns:
      hecho
    """
    pass

  def to_string(self) -> str:
    """ muestra la expresión de una base de hechos en el lenguaje
    Args:
    Returns:
      base de hechos en lenguaje natural
    """
    pass