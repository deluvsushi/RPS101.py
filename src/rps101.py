from requests import get

class RPS101:
	def __init__(self) -> None:
		self.api = "https://rps101.pythonanywhere.com/api/v1"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}


	def get_all_objects(self) -> dict:
		return get(
			f"{self.api}/objects/all",
			headers=self.headers).json()


	def get_object_info(self, object_name: str) -> dict:
		return get(
			f"{self.api}/objects/{object_name}",
			headers=self.headers).json()


	def get_match_result(
			self,
			object_one: str,
			object_two: str) -> dict:
		return get(
			f"{self.api}/match?object_one={object_one}&object_two={object_two}",
			headers=self.headers).json()
