from types import ModuleType

import cloudcoil.models.crossplane as crossplane


def test_has_modules():
    modules = list(filter(lambda x: isinstance(x, ModuleType), crossplane.__dict__.values()))
    assert modules, "No modules found in crossplane"
