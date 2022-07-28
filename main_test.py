from main import main
import io


def test_myoutput(monkeypatch,capsys):  # or use "capfd" for fd-level
    monkeypatch.setattr('sys.stdin', io.StringIO('3 2 1 nn bb aa'))
    main() 
    captured = capsys.readouterr()
    assert captured.out == "1 2 3 aa bb nn\n"
