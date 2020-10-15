from src.utils import cli


def test_run():
    cmd = "sleep 5 && echo 'hello'"
    res = cli.run(cmd)
    print(res)
    print('test_run done')


