import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service(host):
    # hostname = host.backend.get_hostname()
    # if hostname != 'nginx-custom':
    service = host.service('nginx')
    assert service.is_running


def test_listening(host):
    out = host.check_output('ss --numeric --listening --tcp')
    print(out)
    assert host.socket('tcp://%d' % 80).is_listening
