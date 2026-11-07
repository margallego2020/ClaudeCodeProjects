import unittest

import tareas


class TestTareas(unittest.TestCase):
    def test_agregar_completar_eliminar(self):
        lista = []
        self.assertEqual(tareas.agregar(lista, "estudiar"), 1)
        tareas.completar(lista, 1)
        self.assertTrue(lista[0]["hecha"])
        self.assertEqual(tareas.eliminar(lista, 1)["texto"], "estudiar")
        self.assertEqual(lista, [])

    def test_guardar_y_cargar(self):
        import tempfile
        from pathlib import Path

        with tempfile.TemporaryDirectory() as d:
            archivo = Path(d) / "t.json"
            tareas.guardar([{"texto": "ñandú", "hecha": False}], archivo)
            self.assertEqual(tareas.cargar(archivo)[0]["texto"], "ñandú")


if __name__ == "__main__":
    unittest.main()
