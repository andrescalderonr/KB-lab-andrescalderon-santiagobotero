from __future__ import annotations
from typing import List
from Rule import Rule

class KnowledgeBase:
  """ base de conocimiento a partir de reglas bajo la sintaxis pertinente
  """
  @classmethod
  def knowledge_base(cls):
    """ establece una base de conocimiento basada en reglas
    Args:
    Returns:
    """
    pass

  def add_rule(self, condition: List[str], conclusion: str):
    """ añade una nueva regla a la base de conocimiento
    Args:
      condition: lista de proposiones (antecedentes)
      conclusion: proposición que implica de la regla (consecuente)
    Returns:
    """
    pass

  def could_deduce(self, proposition: str) -> List[Rule]:
    """ sustrae las reglas que permiten concluir una proposicion
    Args:
      proposition: nombre de la proposicion
    Returns:
      listado de las reglas desencadenadas
    """
    pass

  def num_rules(self) -> int:
    """ determina cantidad de reglas en la base de conocimiento
    Args:
    Returns:
      número de reglas
    """
    pass

  def get_rule(self, r: int) -> Rule:
    """ obtiene la regla según su indicador
    Args:
      r: indice de la regla
    Returns:
      regla
    """
    pass

  def to_string(self) -> str:
    """ muestra la expresión de una base de conocimiento de reglas en el lenguaje
    Args:
    Returns:
      base de reglas en lenguaje natural
    """
    pass