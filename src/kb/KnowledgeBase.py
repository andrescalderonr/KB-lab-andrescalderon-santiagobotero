from __future__ import annotations
from typing import List, Any
from .Rule import Rule

class KnowledgeBase:
    """ base de conocimiento a partir de reglas bajo la sintaxis pertinente
    """
    rules = []

    @classmethod
    def knowledge_base(cls):
        """ establece una base de conocimiento basada en reglas
        Args:
        Returns:
        """
        obj = cls()
        obj.rules = []
        return obj

    def add_rule(self, condition: List[str], conclusion: str):
        """ añade una nueva regla a la base de conocimiento
        Args:
        condition: lista de proposiones (antecedentes)
        conclusion: proposición que implica de la regla (consecuente)
        Returns:
        """
        rule = Rule.rule(condition, conclusion)
        self.rules.append(rule)

    def could_deduce(self, proposition: str) -> List[Rule]:
        """ sustrae las reglas que permiten concluir una proposicion
        Args:
        proposition: nombre de la proposicion
        Returns:
        listado de las reglas desencadenadas
        """
        return [rule for rule in self.rules if rule.get_conclusion() == proposition]

    def num_rules(self) -> int:
        """ determina cantidad de reglas en la base de conocimiento
        Args:
        Returns:
        número de reglas
        """
        return len(self.rules)

    def get_rule(self, r: int) -> Any | None:
        """ obtiene la regla según su indicador
        Args:
        r: indice de la regla
        Returns:
        regla
        """
        if 0 <= r < len(self.rules):
            return self.rules[r]
        return None

    def to_string(self) -> str:
        """ muestra la expresión de una base de conocimiento de reglas en el lenguaje
        Args:
        Returns:
        base de reglas en lenguaje natural
        """
        if not self.rules:
            return "Base de conocimiento vacía"

        result = "=== BASE DE CONOCIMIENTO ===\n"
        for i, rule in enumerate(self.rules):
            result += f"  R{i + 1}: {rule.to_string()}\n"
        return result
