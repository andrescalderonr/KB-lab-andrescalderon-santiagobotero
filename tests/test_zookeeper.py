from src.engine import InferenceEngine
from src.kb import KnowledgeBase
from src.fb import FactBase
from src.enums import Value


def create_zookeeper_kb():
    """Crea la base de conocimiento del Zookeeper"""
    kb = KnowledgeBase.knowledge_base()

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


def test_stretch_forward():
    """Test con Stretch usando razonamiento hacia adelante"""
    print("\n" + "=" * 70)
    print("TEST 1: STRETCH - RAZONAMIENTO HACIA ADELANTE")
    print("=" * 70)

    kb = create_zookeeper_kb()
    fb = FactBase.fact_base()

    # Working memory A (Stretch)
    print("\n Cargando hechos iniciales de Stretch...")
    fb.add_fact("has hair", Value.TRUE, "usuario")
    fb.add_fact("chews cud", Value.TRUE, "usuario")
    fb.add_fact("has long legs", Value.TRUE, "usuario")
    fb.add_fact("has long neck", Value.TRUE, "usuario")
    fb.add_fact("has tawny color", Value.TRUE, "usuario")
    fb.add_fact("has dark spots", Value.TRUE, "usuario")

    print("\n Hechos iniciales:")
    print(fb.to_string())

    # Razonamiento hacia adelante
    fb = InferenceEngine.forward(kb, fb)

    print("\n" + "=" * 70)
    print("RESULTADO FINAL:")
    print("=" * 70)
    print(fb.to_string())

    # Explicar conclusión
    print("\n EXPLICACIÓN DEL RESULTADO:")
    print(InferenceEngine.how(fb, "is a giraffe"))


def test_splashy_backward():
    """Test con Splashy usando razonamiento hacia atrás"""
    print("\n" + "=" * 70)
    print("TEST 2: SPLASHY - RAZONAMIENTO HACIA ATRÁS")
    print("=" * 70)

    kb = create_zookeeper_kb()
    fb = FactBase.fact_base()

    # Working memory B (Splashy)
    print("\n Cargando hechos iniciales de Splashy...")
    fb.add_fact("has feathers", Value.TRUE, "usuario")
    fb.add_fact("lays eggs", Value.TRUE, "usuario")
    fb.add_fact("does not fly", Value.TRUE, "usuario")
    fb.add_fact("is black and white", Value.TRUE, "usuario")
    fb.add_fact("swims", Value.TRUE, "usuario")

    print("\n Hechos iniciales:")
    print(fb.to_string())

    # Razonamiento hacia atrás
    fb = InferenceEngine.backward(kb, fb, "is a penguin")

    print("\n" + "=" * 70)
    print("RESULTADO FINAL:")
    print("=" * 70)
    print(fb.to_string())

    # Explicar conclusión
    print("\n EXPLICACIÓN DEL RESULTADO:")
    print(InferenceEngine.how(fb, "is a penguin"))


if __name__ == "__main__":
    print("=" * 70)
    print("SISTEMA DE INFERENCIA BASADO EN REGLAS - ZOOKEEPER")
    print("=" * 70)

    test_stretch_forward()
    input("\nPresiona ENTER para continuar...")
    test_splashy_backward()

    print("\n" + "=" * 70)
    print("TESTS COMPLETADOS ✓")
    print("=" * 70)