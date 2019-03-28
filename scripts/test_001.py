import pytest,allure

class Test_Severity:
    @allure.step(title="BLOCKER")
    @pytest.allure.severity (pytest.allure.severity_level.BLOCKER)
    def test_001(self):
        assert False

    @allure.step (title="CRITICAL")
    @pytest.allure.severity (pytest.allure.severity_level.CRITICAL)
    def test_002(self):
        assert True

    @allure.step (title="NORMAL")
    @pytest.allure.severity (pytest.allure.severity_level.NORMAL)
    def test_003(self):
        assert True

    @allure.step (title="MINOR")
    @pytest.allure.severity (pytest.allure.severity_level.MINOR)
    def test_004(self):
        assert True

    @allure.step (title="TRIVIAL")
    @pytest.allure.severity (pytest.allure.severity_level.TRIVIAL)
    def test_005(self):
        assert False