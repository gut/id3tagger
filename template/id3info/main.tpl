{% extends "../base.tpl" %}

{% block content %}
<form method="get" target="_self">
<table>
	<tr>
		<th class="submit"><button type="submit" name="change" value="{{ change_value }}">Apply Changes?</button></th>
	</tr>
</table>
</form>
{% endblock %}
