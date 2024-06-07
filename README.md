To run locally:

```bash
pip install -e .
```

Tasks

- [x] Parse tag from a cif file
- [x] Determine the shortest distance pair in a cif file
- [x] Get unique distances in CifEnsemble
- [x] Get unique supercell size
- [ ] Determine the coordination number from each atomic label
- [ ] Move files based on tags, sgroup, sgname, supercell size, elements, structure, formula
- [ ] Copy files based on tags, sgroup, sgname, supercell size, elements, structure, formula
- [ ] Move files based on min distance
- [ ] Copy files based on min distance
- [ ] Generate histrograms for tags, sgroup, sgname, supercell size, elements, structure, formula


- [x] preprocess symbolic labels
- [x] remove author loop content
- [x] generate supercell of 2 by 2 by 2
- [x] compute distance between element sites
- [x] CIF: compute the coordination number
- [x] CIF: compute minimum distance within cutoff radius
- [x] Get unique  tags, sgroup, sgname, supercell size, elements, structure, formula
- [ ] CifEnsemble: compute supercell, min distance histrogram
- [ ] CIF: compute all homoatomic shortest distances
- [ ] CIF: compute all heteroatomic shortest distances
- [ ] CIF: finds all possible bonds
- [ ] CIF: finds bonds that are missing from shortest distance site

20240529

- The `Cif` class is used to store parsed information and nearest neighbors.

## Nodemon setup

```json
{
    "exec": "black -l 70 . && python -m pytest -v && pytest --cov",
    "ext": "py",
    "ignore": ["*.pyc", "*__pycache__*"],
    "watch": ["*.*"]
  }
```


Initialize
cif_eb

System Analysis:

[ ] CifEsemble.analyze_binary_system
[ ] CifEsemble.analyze_ternary_system
[ ] CifEsemble.analyze_ternary_binary_systems

Bonding Analysis
[ ] CifEsemble.conduct_site_bonding_analysis

Stats:

[ ] CifEsemble.get_unique_formulas(folder_path: str)csv
[ ] CifEsemble.get_unique_formulas_stats(folder_path: str)
[ ] CifEsemble.get_unique_structures(folder_path: str)
[ ] CifEsemble.get_unique_weights(folder_path: str)
[ ] CifEsemble.get_unique_space_groups(folder_path; str)
[ ] CifEsemble.get_unique_space_grouop_numbers
[ ] CifEsemble.generate_formula_histograms(folder_path: )
[ ] CifEsemble.generate_all_unique_stats( )
[ ] CifEsemble.generate_structure_histograms(folder_path: )
[ ] CifEsemble.get_unique_site_labels
[ ] CfiEssemble.generate

Filter
