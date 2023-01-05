import awkward as ak  # noqa: F401
import numpy as np  # noqa: F401
import pytest  # noqa: F401

import fastjet._pyjet  # noqa: F401

vector = pytest.importorskip("vector")  # noqa: F401


def test_softdrop():
    array = ak.Array(
        [
            [
                {"px": 1.2, "py": 3.2, "pz": 5.4, "E": 2.5, "ex": 0.78},
                {"px": 32.2, "py": 64.21, "pz": 543.34, "E": 24.12, "ex": 0.35},
                {"px": 32.45, "py": 63.21, "pz": 543.14, "E": 24.56, "ex": 0.0},
            ],
            [
                {"px": 1.2, "py": 3.2, "pz": 5.4, "E": 2.5, "ex": 0.78},
                {"px": 32.2, "py": 64.21, "pz": 543.34, "E": 24.12, "ex": 0.35},
                {"px": 32.45, "py": 63.21, "pz": 543.14, "E": 24.56, "ex": 0.0},
            ],
        ]
    )
    jetdef = fastjet.JetDefinition(fastjet.antikt_algorithm, 0.6)
    cluster = fastjet._pyjet.AwkwardClusterSequence(array, jetdef)
    jets_out = [
        [
            {"px": 1.2, "py": 3.2, "pz": 5.4, "E": 2.5},
            {"px": 64.65, "py": 127.41999999999999, "pz": 1086.48, "E": 48.68},
        ],
        [
            {"px": 1.2, "py": 3.2, "pz": 5.4, "E": 2.5},
            {"px": 64.65, "py": 127.41999999999999, "pz": 1086.48, "E": 48.68},
        ],
    ]
    assert jets_out == cluster.jets().to_list()

    assert jets_out == cluster.softdrop_jets().to_list()
