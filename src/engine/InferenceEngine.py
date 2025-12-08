from __future__ import annotations
from src.kb import KnowledgeBase
from src.fb import FactBase
from src.enums import Value

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
        print("\n=== RAZONAMIENTO HACIA ADELANTE ===")
        changed = True
        iteration = 0

        while changed:
            changed = False
            iteration += 1
            print(f"\nIteración {iteration}:")

            for i in range(kb.num_rules()):
                rule = kb.get_rule(i)

                can_apply = rule.can_apply(fb)

                if can_apply == Value.TRUE:
                    conclusion = rule.get_conclusion()

                    if fb.get_value(conclusion) == Value.UNKNOWN:
                        fb.add_fact(conclusion, Value.TRUE, f"R{i + 1}")
                        print(f"  ✓ Aplicada R{i + 1}: {conclusion}")
                        changed = True

        print(f"\nRazonamiento completado en {iteration} iteraciones.")
        return fb

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
        print(f"\n=== RAZONAMIENTO HACIA ATRÁS ===")
        print(f"Objetivo: {proposition}")

        result = cls._backward_recursive(kb, fb, proposition, set())

        if result == Value.TRUE:
            print(f"\n✓ Se pudo probar: {proposition}")
        elif result == Value.FALSE:
            print(f"\n✗ Se probó falso: {proposition}")
        else:
            print(f"\n? No se pudo determinar: {proposition}")

        return fb


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
        if proposition in fb.facts:
            fact = fb.facts[proposition]
            return f"{proposition} = {fact.value.name} (fuente: {fact.source})"
        return f"{proposition} = UNKNOWN (no hay información)"


    @classmethod
    def _backward_recursive(cls, kb: KnowledgeBase, fb: FactBase,
                            proposition: str, visited: set) -> Value:
        """generar una inferencia con razonamiento hacia atras (recursivo)
        Args:
          kb: base de conocimiento a base de reglas
          fb: base de hechos que se perciben
          proposition: nombre de la proposicion, formulada como hipotesis
          visited: conjunto de proposiciones visitadas para evitar ciclos
        Returns:
           valor de la proposición
        """
        if proposition in visited:
            return Value.UNKNOWN

        visited.add(proposition)

        current_value = fb.get_value(proposition)
        if current_value != Value.UNKNOWN:
            print(f"  → {proposition} ya conocido: {current_value.name}")
            return current_value

        rules = kb.could_deduce(proposition)

        if not rules:
            print(f"  ? No hay reglas para {proposition}")
            value = fb.ask_value(proposition)
            return value

        for rule in rules:
            print(f"  Intentando regla: {rule.to_string()}")

            all_conditions_true = True

            for condition in rule.condition:
                condition_value = cls._backward_recursive(kb, fb, condition, visited.copy())

                if condition_value != Value.TRUE:
                    all_conditions_true = False
                    break

            if all_conditions_true:
                fb.add_fact(proposition, Value.TRUE, "regla")
                print(f"  ✓ Conclusión: {proposition} = TRUE")
                return Value.TRUE

        return Value.UNKNOWN