To run locally:

```bash
pip install -e .
```

Tasks

The package is able to

- Preproces atomic sites that have symbols instead of element names
- Compute the coordination number from atomic label site.
- Compute the distance from each atomic site within a cutoff radius
- Distnace
  - Minimum distances from each atomic site
  - Homoatomic pair minimum distances
  - Heteroatomic pair minimum distances
- Generate a supercell


- [x] preprocess symbolic labels
- [x] remove author loop content
- [x] generate supercell of 2 by 2 by 2
- [x] compute distance between element sites
- [x] compute the coordination number
- [x] compute minimum distance within cutoff radius
- [ ] compute all nearest site bonding (CBA) work
- [ ] compute all homoatomic shortest distances
- [ ] compute supercell, min distance histrogram
- [ ] compute all heteroatomic shortest distances
- [ ] compute most common bond distribution in a folder across all sites
- [ ] finds all possible bonds
- [ ] finds bonds that are missing 
- [ ] finds all site and element information


## Nodemon setup

```json
{
    "exec": "black -l 70 . && python -m pytest -v && pytest --cov",
    "ext": "py",
    "ignore": ["*.pyc", "*__pycache__*"],
    "watch": ["*.*"]
  }
```