def test_tmux_is_installed(host):
    pkg = host.package("tmux")
    assert pkg.is_installed


def test_tmux_version(host):
    tmux_version = host.run("tmux -V | cut -d ' ' -f 2")
    assert tmux_version.stdout.startswith("2")
