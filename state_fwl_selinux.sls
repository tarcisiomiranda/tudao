{% if grains['os_family'] == 'RedHat' %}
{% set selinux_status = salt['cmd.run']('getenforce') %}
{% set firewall_status = salt['cmd.run']('systemctl is-active firewalld') %}

check_selinux_status:
  cmd.run:
    - name: 'echo "SELinux status: {{ selinux_status }}"'
    - unless: 'test "{{ selinux_status | lower }}" = "enforcing"'

check_firewall_status:
  cmd.run:
    - name: 'echo "FirewallD status: {{ firewall_status }}"'
    - unless: 'test "{{ firewall_status }}" = "active"'

{% else %}
not_redhat_family:
  cmd.run:
    - name: 'echo "Nao faz parte da familia RedHat."'
{% endif %}
