"""Pruebas sin red del verificador (respuestas simuladas, no datos reales de artículos)."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import verificar_referencias as v  # noqa: E402


def falla_red(url):
    raise OSError("red bloqueada")


class Pruebas(unittest.TestCase):
    def test_extrae_ids(self):
        texto = ("Autor A. Titulo. Rev. 2020;1:1-2. doi:10.1000/abc.123. PMID: 1234567\n"
                 "Otro. https://doi.org/10.1000/ABC.123 PMID 7654321")
        dois, pmids = v.extract_ids(texto)
        self.assertEqual(dois, ["10.1000/abc.123"])
        self.assertEqual(pmids, ["1234567", "7654321"])

    def test_sin_red_no_verifica(self):
        r = v.check_doi("10.1000/abc", fetch=falla_red)
        self.assertTrue(r["estado"].startswith("No verificable"))
        r = v.check_pmid("1", fetch=falla_red)
        self.assertTrue(r["estado"].startswith("No verificable"))

    def test_prefijo_de_pruebas(self):
        r = v.check_doi("10.5555/xyz", fetch=falla_red)
        self.assertIn("10.5555", r["alertas"][0])

    def test_pubmed_retractado(self):
        simulado = {"result": {"99": {"title": "T", "source": "J", "pubdate": "2001 Jan",
                                      "authors": [{"name": "Perez A"}],
                                      "pubtype": ["Journal Article", "Retracted Publication"]}}}
        r = v.check_pmid("99", fetch=lambda url: simulado)
        self.assertEqual(r["estado"], "Existe en PubMed")
        self.assertIn("PUBLICACIÓN RETRACTADA", r["alertas"])

    def test_pubmed_inexistente(self):
        r = v.check_pmid("5", fetch=lambda url: {"result": {"5": {"error": "cannot get document summary"}}})
        self.assertEqual(r["estado"], "No encontrado en PubMed")

    def test_crossref(self):
        simulado = {"message": {"title": ["T"], "container-title": ["J"],
                                "issued": {"date-parts": [[2019, 3]]},
                                "author": [{"family": "Lopez", "given": "Maria"}]}}
        r = v.check_doi("10.1000/x", fetch=lambda url: simulado)
        self.assertEqual((r["estado"], r["anio"], r["autor"]), ("Existe en Crossref", "2019", "Lopez M"))


if __name__ == "__main__":
    unittest.main()
