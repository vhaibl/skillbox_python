import os

import cv2


class Postcards:
    def __init__(self, daterus, temperature, condition, wind, humidity, pressure, picture, day):
        self.daterus = daterus
        self.temperature = temperature
        self.condition = condition
        self.wind = wind
        self.humidity = humidity
        self.pressure = pressure
        self.picture = picture
        self.day = day

    def draw_postcard(self):
        image = cv2.imread('python_snippets\\external_data\\probe.jpg')

        self.gradient(image)

        self.temperature = self.temperature.replace('°', '')
        self.temperature = self.temperature.replace('\n', ' ')
        self.daterus = self.daterus.replace('Сегодня', '')
        cv2.putText(image, self.daterus, (180, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
        cv2.putText(image, self.condition, (30, 220), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0))
        cv2.putText(image, self.temperature, (66, 142), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
        cv2.putText(image, f'Влажность:{self.humidity}', (250, 220), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0))
        cv2.putText(image, f'Давление:{self.pressure}', (250, 190), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0))
        cv2.putText(image, f'Ветер:{self.wind}', (30, 190), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 0))
        s_img = cv2.imread(self.picture)
        x_offset = 48
        y_offset = 10
        image[y_offset:y_offset + s_img.shape[0], x_offset:x_offset + s_img.shape[1]] = s_img
        image_path = f'images/{self.day}.jpg'
        if os.path.exists("images"):
            pass
        else:
            os.mkdir('images')
        cv2.imwrite(image_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
        return image

    def gradient(self, image):
        for y in range(255):
            weather_background = {'снег': (255, 255, y), 'ясно': (y, 255, 255), 'облачно': (y + 64, y + 64, y + 64),
                                  'дождь': (255, y, y), 'дождь/гроза': (192, y - 64, y - 64)}

            # TODO Не понятно, как вынести словарь в атрибуты, так как y переопределяется в цикле
            if self.condition in weather_background:
                weather_state = weather_background[self.condition]
            else:
                weather_state = (y + 64, y + 64, y + 64)
            cv2.line(image, (0, y), (512, y), color=weather_state)

#
# def viewImage(image, name_of_window):
#     cv2.namedWindow(name_of_window, cv2.WINDOW_AUTOSIZE)
#     cv2.imshow(name_of_window, image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#
# #
# draw = Postcards(daterus='Сегодня 26 Июня 2020', temperature=f'Днем +26° \n Ночью +15°', condition='ясно', wind='2 м/с',
#                  humidity='88%', pressure='746 мм', picture='python_snippets\\external_data\\weather_img\\cloud.jpg',
#                  day=datetime.date(2020, 6, 2))
# draw.draw_postcard()
