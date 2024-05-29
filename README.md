To run locally:

```bash
pip install -e .
```

Tasks

The package is able to

- [x] preprocess symbolic labels
- [x] remove author loop content
- [x] generate supercell of 2 by 2 by 2
- [x] compute distance between element sites
- [ ] compute the coordination number
- [ ] compute minimum distance within cutoff radius
- [ ] compute all homoatomic shortest distances
- [ ] compute supercell, min distance histrogram
- [ ] compute all heteroatomic shortest distances
- [ ] compute site and element data
- [ ] compute most common bond distribution in a folder across all sites

## Nodemon setup

```json
{
    "exec": "black -l 70 . && python -m pytest -v && pytest --cov",
    "ext": "py",
    "ignore": ["*.pyc", "*__pycache__*"],
    "watch": ["*.*"]
  }
```