

def get_json_from_shareddata(html):
	return html.split("window._sharedData = ")[1].split(";</script>")[0]
