import os
from confobj import Config
from confobj import ConfigYaml
from confobj import ConfigEnv
from confobj import ConfigJson
from confobj import ConfigDict


class Conf(Config):
    def __init__(self):
        self.hello = "world"
        self.num = 42
        super(Conf, self).__init__()
        self.configure()


def test_config():
    os.environ["CONF_NUM"] = "52"
    conf = Conf()
    assert conf.hello == "world"
    assert conf.num == 52
    assert isinstance(conf.num, int)
    assert isinstance(conf.hello, str)
    del os.environ["CONF_NUM"]


class ConfYaml(Config):
    def __init__(self):
        self.hello = "world"
        self.num = 42
        super(ConfYaml, self).__init__(
            order=(ConfigYaml(open("tests/test.yaml")),))
        self.configure()


def test_config_yaml():
    conf = ConfYaml()
    assert conf.hello == "universe"
    assert conf.num == 42
    assert isinstance(conf.num, int)
    assert isinstance(conf.hello, str)


class ConfYamlEnv(Config):
    def __init__(self):
        self.hello = "world"
        self.num = 42
        super(ConfYamlEnv, self).__init__(
            order=(ConfigYaml(open("tests/test.yaml")),
                   ConfigEnv()))
        self.configure()


def test_config_yaml_env():
    os.environ["ConfYamlEnv_hello"] = "conf"
    conf = ConfYamlEnv()
    assert conf.hello == "conf"
    assert conf.num == 42
    assert isinstance(conf.num, int)
    assert isinstance(conf.hello, str)
    del os.environ["ConfYamlEnv_hello"]


class ConfEnvYaml(Config):
    def __init__(self):
        self.hello = "world"
        self.num = 42
        super(ConfEnvYaml, self).__init__(
            order=(ConfigEnv(),
                   ConfigYaml(open("tests/test.yaml"))))
        self.configure()


def test_config_env_yaml():
    os.environ["ConfEnvYaml_hello"] = "conf"
    conf = ConfEnvYaml()
    assert conf.hello == "universe"
    assert conf.num == 42
    assert isinstance(conf.num, int)
    assert isinstance(conf.hello, str)
    del os.environ["ConfEnvYaml_hello"]


class ConfJson(Config):
    def __init__(self):
        self.hello = "world"
        self.num = 42
        super(ConfJson, self).__init__(order=(ConfigJson(open(
            "tests/test.json")),))
        self.configure()


def test_config_json():
    conf = ConfJson()
    assert conf.hello == "json"
    assert conf.num == 42
    assert isinstance(conf.num, int)
    assert isinstance(conf.hello, str)


class ConfDict(Config):
    def __init__(self):
        self.hello = "world"
        self.num = 42
        super(ConfDict, self).__init__(order=(ConfigDict(
            {
                "hello": "dict"
            }
        ),))
        self.configure()


def test_config_dict():
    conf = ConfDict()
    assert conf.hello == "dict"
    assert conf.num == 42
    assert isinstance(conf.num, int)
    assert isinstance(conf.hello, str)
