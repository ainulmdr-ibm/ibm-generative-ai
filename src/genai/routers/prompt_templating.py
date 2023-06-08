from genai.exceptions import GenAiException
from genai.options import Options
from genai.services import RequestHandler


class PromptTemplatingRouter:
    PROMPT_TEMPLATES = "/prompt_templates"

    def __init__(self, service_url: str, api_key: str) -> None:
        self.service_url = service_url.rstrip("/")
        self.key = api_key

    def prompt_output(self, inputs, template):
        try:
            endpoint = self.service_url + PromptTemplatingRouter.PROMPT_TEMPLATES + "/output"
            return RequestHandler.post(endpoint, key=self.key, options=Options(inputs=inputs, template=template))
        except Exception as e:
            raise GenAiException(e)

    def prompt_templates(self, name, value):
        try:
            endpoint = self.service_url + PromptTemplatingRouter.PROMPT_TEMPLATES
            return RequestHandler.post(endpoint, key=self.key, options=Options(name=name, value=value))
        except Exception as e:
            raise GenAiException(e)

    def update_prompt_templates(self, id: str, name: str, value: str):
        try:
            endpoint = self.service_url + PromptTemplatingRouter.PROMPT_TEMPLATES + "/" + id
            return RequestHandler.put(endpoint, key=self.key, options=Options(name=name, value=value))
        except Exception as e:
            raise GenAiException(e)

    def get_prompt_templates(self, id: str = None):
        try:
            endpoint = self.service_url + PromptTemplatingRouter.PROMPT_TEMPLATES
            endpoint = endpoint if id is None else endpoint + "/" + id

            return RequestHandler.get(endpoint, key=self.key)
        except Exception as e:
            raise GenAiException(e)

    def delete_prompt_templates(self, id: str):
        if id is None:
            raise GenAiException("ID cannot be None when attempting to delete a prompt.")
        try:
            endpoint = self.service_url + PromptTemplatingRouter.PROMPT_TEMPLATES + "/" + id
            return RequestHandler.delete(endpoint, key=self.key)
        except Exception as e:
            raise GenAiException(e)
