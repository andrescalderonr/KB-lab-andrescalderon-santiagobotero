from __future__ import annotations
from typing import Any
from src.enums import Value
from .Fact import Fact

class FactBase:
    """ base de conocimiento a partir de reglas bajo la sintaxis pertinente
    """
    facts = {}

    @classmethod
    def fact_base(cls):
        """ establece una base de hechos bajo el lenguaje
        Args:
        Returns:
        """
        obj = cls()
        obj.facts = {}
        return obj

    def add_fact(self, proposition: str, value: Value, source: str):
        """ establece una nueva base de hechos en la sintaxis
        Args:
          proposition: nombre de la proposicion
          value: valor de la proposición
          source: source: fuente que dio el valor para la proposicion: usuario o regla
        Returns:
        """
        self.facts[proposition] = Fact.fact(proposition, value, source)

    def get_value(self, proposition: str) -> Value:
        """ obtiene el valor de una proposición
        Args:
          proposition: nombre de la proposicion
        Returns:
          valor semántico de la regla
        """
        if proposition in self.facts:
            return self.facts[proposition].value
        return Value.UNKNOWN

    def ask_value(self, proposition: str) -> Value:
        """ le pregunta al usuario el valor de una proposición
        Args:
          proposition: nombre de la proposicion
        Returns:
          valor semántico de la regla
        """
        print(f"\n¿Cuál es el valor de '{proposition}'?")
        print("Opciones: 1 (TRUE), 2 (FALSE), 3 (UNKNOWN)")

        while True:
            try:
                response = int(input("Respuesta: ").strip())
                if response == 1:
                    value = Value.TRUE
                    break
                elif response == 2:
                    value = Value.FALSE
                    break
                elif response == 3:
                    value = Value.UNKNOWN
                    break
                else:
                    print("Opción inválida. Use 1, 2 o 3.")
            except ValueError:
                print("Opción inválida. Use 1, 2 o 3.")

        self.add_fact(proposition, value, "usuario")
        return value

    def num_facts(self) -> int:
        """ determina cantidad de hechos en la base
        Args:
        Returns:
          número de hechos
        """
        return len(self.facts)

    def get_fact(self, f: int) -> Any | None:
        """ obtiene el hecho según su indicador
        Args:
          f: indice del hecho
        Returns:
          hecho
        """
        facts_list = list(self.facts.values())
        if 0 <= f < len(facts_list):
            return facts_list[f]
        return None

    def to_string(self) -> str:
        """ muestra la expresión de una base de hechos en el lenguaje
        Args:
        Returns:
          base de hechos en lenguaje natural
        """
        if not self.facts:
            return "Base de hechos vacía"

        result = "=== BASE DE HECHOS ===\n"
        for fact in self.facts.values():
            result += f"  {fact.to_string()}\n"
        return result