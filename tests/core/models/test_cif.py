def test_cif_static_properties(cif_URhIn):
    assert cif_URhIn.unique_elements == {"U", "In", "Rh"}
    assert cif_URhIn.formula == "URhIn"
    assert cif_URhIn.structure == "ZrNiAl"
    assert cif_URhIn.site_labels == ["In1", "U1", "Rh1", "Rh2"]
    assert cif_URhIn.space_group_name == "P-62m"
    assert cif_URhIn.space_group_number == 189
    assert cif_URhIn.tag == "rt"
    assert cif_URhIn.heterogeneous_bond_pairs == {
        ("In", "Rh"),
        ("In", "U"),
        ("Rh", "U"),
    }
    assert cif_URhIn.homogenous_bond_pairs == {
        ("U", "U"),
        ("Rh", "Rh"),
        ("In", "In"),
    }

    assert cif_URhIn.all_bond_pairs == {
        ("U", "U"),
        ("Rh", "Rh"),
        ("In", "In"),
        ("In", "Rh"),
        ("In", "U"),
        ("Rh", "U"),
    }


def test_cif_lazy_propertes_after_compute_connection(cif_URhIn):
    cif_URhIn.compute_connections()
    assert cif_URhIn.shortest_pair_distance == 2.697

    connections_CN = cif_URhIn.connections_CN
    assert len(connections_CN.get("In1")) == 14
    assert len(connections_CN.get("U1")) == 11
    assert len(connections_CN.get("Rh1")) == 9
    assert len(connections_CN.get("Rh2")) == 9


def test_cif_lazy_propertes(cif_URhIn):
    assert cif_URhIn.shortest_pair_distance == 2.697

    connections_CN = cif_URhIn.connections_CN
    assert len(connections_CN.get("In1")) == 14
    assert len(connections_CN.get("U1")) == 11
    assert len(connections_CN.get("Rh1")) == 9
    assert len(connections_CN.get("Rh2")) == 9
