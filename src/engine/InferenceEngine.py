from __future__ import annotations
from src.kb import KnowledgeBase
from src.fb import FactBase

class InferenceEngine:
    """ motor de inferencia para un sistema basado en conocimiento con base de reglas
    """

    @classmethod
    def forward(cls, kb: KnowledgeBase, fb: FactBase) -> FactBase:
        """ generar una inferencia con razonamiento hacia adelante
        Args:
          kb: base de conocimiento a base de reglas
          fb: base de hechos que se perciben
        Returns:
           base de hechos actualizada con nuevos hechos inferidos
        """
        pass

    @classmethod
    def backward(cls, kb: KnowledgeBase, fb: FactBase, proposition: str) -> FactBase:
        """ generar una inferencia con razonamiento hacia atras
        Args:
          kb: base de conocimiento a base de reglas
          fb: base de hechos que se perciben
          proposition: nombre de la proposicion, formulada como hipotesis
        Returns:
           base de hechos actualizada con nuevos hechos inferidos
        """
        pass


    @classmethod
    def how(cls, fb: FactBase, proposition: str) -> str:
        """ consultar la fuente de conocimiento del valor de la proposición
        Args:
        proposition: nombre de la proposicion
        Returns:
        valor y fuente de información de la proposición
        :param proposition:
        :param fb:
        """
        pass