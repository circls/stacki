# import pytest
import subprocess


class TestAddHostAlias:
    """APPLIANCE_TEST_DATA = []

    @pytest.mark.parametrize(APPLIANCE_TEST_DATA)
    def test_add_host_alias(self, host):
        host.run('stack load hostfile')  # doesn't need tested, right?
        result = host.run('stack add host alias backend-0-0 alias=test1 interface=eth0')
        assert result.rc == 0"""

    def test_add_host_alias(self):
        # Load hosts
        subprocess.run('stack load hostfile'.split(), encoding='utf-8')  # get this from somewhere?

        # Add aliases on each interface for each backend
        subprocess.run('stack add host alias backend-0-0 alias=testb0 interface=eth0'.split(), encoding='utf-8')
        result = subprocess.run('stack list host alias'.split(), encoding='utf-8')
        output = result.stdout.strip()
        print(output)
