<html>
<head>
	<title>{{ title }}</title>
	<link rel="stylesheet" href="/css/style.css">
</head>
<body>
<h3>Renaming files with regex:</h3>
<form method="get" target="_self">
<table>
	<tr>
		<td>Directory to work:</td><td><input type="text" name="directory" value="{{ directory }}"></input></td>
	</tr>
	<tr>
		<td>Regex to search:</td><td><input type="text" name="search" value="{{ search }}"></input></td>
	<tr>
	</tr>
		<td>Replacement:</td><td><input type="text" name="replacement" value="{{ replacement }}"></input></td>
	</tr>
	<tr>
		<th colspan="2"><input type="submit" value="Update"></th>
	</tr>
</table>
</form>
{{ content }}
</body>
</html>

