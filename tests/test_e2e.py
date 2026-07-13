from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
class TestTaskFlowUI:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
 
    def teardown_method(self):
        self.driver.quit()
 
    def test_add_task_via_form(self):
        self.driver.get("http://localhost:5000")
        self.driver.find_element(By.ID, "task-title").send_keys("E2E task")
        self.driver.find_element(By.ID, "submit-btn").click()
        msg = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "success")))
        assert "E2E task" in msg.text
