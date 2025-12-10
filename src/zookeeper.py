from src.fb import FactBase
from src.kb import KnowledgeBase
from src.enums import Value

class Zookeeper:
    kb = {}
    fb = {}

    @classmethod
    def initial_rules(cls):
        kb = KnowledgeBase.knowledge_base()
        """Crea la base de conocimiento del Zookeeper"""
        # Z1-Z4: Clasificación básica
        kb.add_rule(["has hair"], "is a mammal")
        kb.add_rule(["gives milk"], "is a mammal")
        kb.add_rule(["has feathers"], "is a bird")
        kb.add_rule(["flies", "lays eggs"], "is a bird")

        # Z5-Z8: Subclasificación de mamíferos
        kb.add_rule(["is a mammal", "eats meat"], "is carnivore")
        kb.add_rule(["is a mammal", "has pointed teeth", "has claws", "has forward-pointing eyes"],
                    "is a carnivore")
        kb.add_rule(["is a mammal", "has hoofs"], "is an ungulate")
        kb.add_rule(["is a mammal", "chews cud"], "is an ungulate")

        # Z9-Z12: Identificación de especies específicas
        kb.add_rule(["is a carnivore", "has tawny color", "has dark spots"], "is a cheetah")
        kb.add_rule(["is a carnivore", "has tawny color", "has black strips"], "is a tiger")
        kb.add_rule(["is an ungulate", "has long legs", "has long neck",
                     "has tawny color", "has dark spots"], "is a giraffe")
        kb.add_rule(["is an ungulate", "has white color", "has black stripes"], "is a zebra")

        # Z13-Z15: Aves específicas
        kb.add_rule(["is a bird", "does not fly", "has long legs",
                     "has long neck", "is black and white"], "is an ostrich")
        kb.add_rule(["is a bird", "does not fly", "swims", "is black and white"], "is a penguin")
        kb.add_rule(["is a bird", "is a good flyer"], "is an albatross")

        return kb

    @classmethod
    def initial_working_memory(cls):
        fb = FactBase.fact_base()

        # Stretch
        fb.add_fact("has hair", Value.TRUE, "initial")
        fb.add_fact("chews cud", Value.TRUE, "initial")
        fb.add_fact("has long legs", Value.TRUE, "initial")
        fb.add_fact("has long neck", Value.TRUE, "initial")
        fb.add_fact("has tawny color", Value.TRUE, "initial")
        fb.add_fact("has dark spots", Value.TRUE, "initial")

        # Splashy
        fb.add_fact("has feathers", Value.TRUE, "initial")
        fb.add_fact("lays eggs", Value.TRUE, "initial")
        fb.add_fact("does not fly", Value.TRUE, "initial")
        fb.add_fact("is black and white", Value.TRUE, "initial")
        fb.add_fact("swims", Value.TRUE, "initial")

        return fb
