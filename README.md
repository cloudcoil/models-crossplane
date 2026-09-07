# cloudcoil-models-crossplane

Versioned crossplane models for cloudcoil.

[![PyPI](https://img.shields.io/pypi/v/cloudcoil.models.crossplane.svg)](https://pypi.python.org/pypi/cloudcoil.models.crossplane)
[![Downloads](https://static.pepy.tech/badge/cloudcoil.models.crossplane)](https://pepy.tech/project/cloudcoil.models.crossplane)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/license/apache-2-0/)
[![CI](https://github.com/cloudcoil/models-crossplane/actions/workflows/ci.yml/badge.svg)](https://github.com/cloudcoil/models-crossplane/actions/workflows/ci.yml)

Models generated from the upstream tagged CRD schemas pinned in `pyproject.toml`.

```python
from cloudcoil.models.crossplane import get_model

Provider = get_model("Provider", api_version="pkg.crossplane.io/v1")
```
