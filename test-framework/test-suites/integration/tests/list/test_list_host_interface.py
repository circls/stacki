import json
import pytest

def test_list_host_interface(host):
	# check that we have the correct interfaces expected
	result = host.run("stack list host attr localhost attr='Ignore_Nics' output-format=json")
	my_json = json.loads(result.stdout)
	ignore_nics = my_json[0]['value'] == 'True'
	result = host.run('stack list host interface')
	assert result.rc == 0
	if ignore_nics == True:
		assert len(result.stdout.splitlines()) == 2
	else:
		assert len(result.stdout.splitlines()) > 2

