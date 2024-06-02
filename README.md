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
[ ] CifEsemble.

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

Filter:

[ ] CifEsemble.copy_files_by_elements(elements: list[str], from, to)
[ ] CifEsemble.move_files_by_elements(elements: list[str], from, to)
[ ] CifEsemble.copy_files_by_formula(structure)
[ ] CifEsemble.copy_files_by_formula(structure)
[ ] CifEsemble.copy_files_by_formula(structure)
[ ] CifEsemble.copy_files_by_structure(structure)
[ ] CifEsemble.copy_files_by_structure(structure)
[ ] CifEsemble.copy_files_by_space_group(structure)
[ ] CifEsemble.move_files_based_on_wrong_format( )
[ ] CifEsemble.format_files_for_CIF_processing()

