from __future__ import annotations
from typing import List
from src.enums import Value
from src.fb import FactBase

class Rule:
    """"Definition of rules under the established language and syntax."""

    @classmethod
    def rule(cls, condition: List[str], conclusion: str):
        """ establece una nueva regla en la sintaxis del lenguaje
        Args:
          condition: lista de reglas en lenguaje natural (antecedentes)
          conclusion: proposición que implica de la regla (consecuente)
        Returns:
        """
        obj = cls()
        obj.condition = condition
        obj.conclusion = conclusion
        return obj

    def can_apply(self, fb: FactBase) -> Value:
        """ evalua la semantica de la regla a partir de los hechos
        Args:
          fb: base de hechos que se perciben
        Returns:
           valor semántico de la regla
        """
        has_unknown = False

        for prop in self.condition:
            value = fb.get_value(prop)
            if value == Value.FALSE:
                return Value.FALSE
            elif value == Value.UNKNOWN:
                has_unknown = True

        if has_unknown:
            return Value.UNKNOWN

        return Value.TRUE

    def get_conclusion(self) -> str:
        """ obtener la conclusion que implica (entail) de la regla
        Args:
        Returns:
           proposicion consecuente
        """
        return self.conclusion

    def to_string(self) -> str:
        """ muestra la expresión de una regla en el lenguaje
        Args:
        Returns:
          regla en lenguaje natural
        """
        conditions_str = " AND ".join(self.condition)
        return f"IF {conditions_str} THEN {self.conclusion}"