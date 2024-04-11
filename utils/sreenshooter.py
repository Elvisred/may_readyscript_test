import os

import allure
import cv2
import numpy as np


class ScreenShooter:

    def __init__(self, web_driver):
        self.web_driver = web_driver

    def get_web_driver_image(self):
        screenshot = self.web_driver.get_screenshot_as_png()
        screenshot = np.frombuffer(screenshot, np.uint8)
        screenshot = cv2.imdecode(screenshot, cv2.IMREAD_COLOR)
        return screenshot

    @allure.step("Сравнение скриншотов")
    def compare_screenshots(self, reference_image_path, output_dir='output', threshold=0.98):
        template_image = cv2.imread(reference_image_path, cv2.IMREAD_UNCHANGED)
        if template_image.shape[2] == 4:
            template_image_mask = cv2.cvtColor(template_image[:, :, 3], cv2.COLOR_GRAY2BGR)
            template_image = cv2.cvtColor(template_image, cv2.COLOR_BGRA2BGR)
        else:
            template_image_mask = np.ones(template_image.shape, dtype=template_image.dtype) * 255

        screenshot = self.get_web_driver_image()
        methods = [cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
        best_match_value = -1

        for method in methods:
            result = cv2.matchTemplate(screenshot, template_image, method, mask=template_image_mask[:, :, 0])
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                match_value = 1 - min_val
            else:
                match_value = max_val

            if match_value > best_match_value:
                best_match_value = match_value

        if best_match_value < threshold:
            message = f"Изображения сильно различаются. Лучшее сходство: {best_match_value}"
            allure.attach(message, name="Различие в сходстве", attachment_type=allure.attachment_type.TEXT)
            raise AssertionError("Скриншоты не совпадают")

        message = f"Скриншоты совпадают. Сходство: {best_match_value}"
        allure.attach(message, name="Сходство", attachment_type=allure.attachment_type.TEXT)

        top_left = (0, 0)
        bottom_right = (top_left[0] + template_image.shape[1], top_left[1] + template_image.shape[0])
        cv2.rectangle(screenshot, top_left, bottom_right, (255, 0, 0), 2)

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        screenshot_path = os.path.join(output_dir, 'marked_screenshot.png')
        cv2.imwrite(screenshot_path, screenshot)

        with open(screenshot_path, "rb") as f:
            file_content = f.read()
            allure.attach(file_content, name="Отмеченный скриншот", attachment_type=allure.attachment_type.PNG)

        return True
