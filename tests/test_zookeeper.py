import unittest
from src.engine import InferenceEngine
from src.enums import Value
from src.zookeeper import Zookeeper

class TestZookeeperInference(unittest.TestCase):

    def setUp(self):
        """Se ejecuta antes de cada test: crea instancia de Zookeeper"""
        self.zoo = Zookeeper()
        self.kb = self.zoo.initial_rules()
        self.fb = self.zoo.initial_working_memory()

    def test_stretch_forward(self):
        """Razonamiento hacia adelante: Stretch debería ser identificado como giraffe"""
        fb_result = InferenceEngine.forward(self.kb, self.fb)
        # Comprobamos que 'is a giraffe' se dedujo
        facts_true = [prop for prop, fact in fb_result.facts.items() if fact.value == Value.TRUE]
        self.assertIn("is a giraffe", facts_true)

    def test_splashy_backward(self):
        """Razonamiento hacia atrás: Splashy debería ser identificado como penguin"""
        fb_result = InferenceEngine.backward(self.kb, self.fb, "is a penguin")
        facts_true = [prop for prop, fact in fb_result.facts.items() if fact.value == Value.TRUE]
        self.assertIn("is a penguin", facts_true)


if __name__ == '__main__':
    unittest.main()
