# Wget autogenerated by preomr script
#
{% for w in works %}
echo "{{ w.name }}"
wget "{{ w.link }}" {% endfor %}
