from marmitasdk.connector import as_seq, as_jlist, as_list


def test_as_seq():
    seq = as_seq("hola", 1, "adios")
    assert seq.size() == 3
    assert list(as_jlist(seq)) == ["hola", 1, "adios"]


def test_as_list():
    slist = as_list("hola", 1, "adios")
    assert slist.size() == 3
    assert list(as_jlist(slist)) == ["hola", 1, "adios"]


def test_as_jlist():
    jlist = as_jlist(as_seq("hola", 1, "adios"))
    assert jlist.get(0) == "hola"
    assert jlist.get(1) == 1
    assert jlist.get(2) == "adios"
