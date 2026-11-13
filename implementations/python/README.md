# Python reference parser

Python 3.10+; no dependencies.

```python
from nids import parse
print(parse("source_destination__router_description::VLAN:1,2,,3"))
```

Run tests from the repository root with `python -m unittest discover -s tests -v`.
