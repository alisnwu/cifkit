def test_cif_properties(cif_URhIn):
    assert isinstance(cif_URhIn.unique_elements, set)
    assert isinstance(cif_URhIn.formula, str)
    assert isinstance(cif_URhIn.structure, str)
    assert isinstance(cif_URhIn.site_labels, list)
    assert isinstance(cif_URhIn.space_group_name, str)
    assert isinstance(cif_URhIn.space_group_number, int)
    assert isinstance(cif_URhIn.tag, str)

    assert cif_URhIn.unique_elements == {"U", "In", "Rh"}
    assert cif_URhIn.formula == "URhIn"
    assert cif_URhIn.structure == "ZrNiAl"
    assert cif_URhIn.site_labels == ["In1", "U1", "Rh1", "Rh2"]
    assert cif_URhIn.space_group_name == "P-62m"
    assert cif_URhIn.space_group_number == 189
    assert cif_URhIn.tag == "rt"

    cif_URhIn.compute_connections()
    assert cif_URhIn.shortest_pair_distance == 2.697
