from calculator.calculator import get_number


def test_get_number_retries_until_valid(monkeypatch, capsys):
    answers = iter(["abc", "", "3.5"])
    monkeypatch.setattr("builtins.input", lambda _prompt="": next(answers))
    assert get_number() == 3.5
    assert "Invalid input" in capsys.readouterr().out
