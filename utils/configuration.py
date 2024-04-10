import os


class Configuration:
    __instance = None

    @staticmethod
    def instance() -> "Configuration":
        if Configuration.__instance is None:
            Configuration.__instance = Configuration()

        return Configuration.__instance

    @property
    def is_headless_disabled(self) -> bool:
        return os.environ.get("DISABLE_HEADLESS") == "True"

    @is_headless_disabled.setter
    def is_headless_disabled(self, value: bool):
        os.environ["DISABLE_HEADLESS"] = str(value)
