from main import main


def test_main_output(capsys):
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from py001!\n"
