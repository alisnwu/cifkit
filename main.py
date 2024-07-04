from cifkit import CifEnsemble

ensemble = CifEnsemble("danila-test")
for cif in ensemble.cifs:
    print(cif.file_name_without_ext)
    print(cif.formula)
    print("mixing type:", cif.site_mixing_type)
    print()
