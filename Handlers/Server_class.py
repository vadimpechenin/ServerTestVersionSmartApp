"""
Серверный класс для проекта "Умный Склад", в котором реализованы три метода:
checkIn детали - зафиксировать место и время детали по QR коду
protocolRequest - вызов протокола для клиента
partIdentification - определение типа детали (по QR или нейронным сетям)
"""

#Классы для работы приложения
from Detections.QR_detector import QR_detector
from Detections.NN_class import NN_detector

from db.sql_data_base import SQL_data_base

from Handlers.BaseCommandHandler import BaseCommandHandler
from Handlers.NomRequest.NomRequestCommandHandler import NomRequestCommandHandler
from Handlers.PartIdentification.PartIdentificationCommandHandler import PartIdentificationCommandHandler
from Handlers.CheckIn.CheckInCommandHandler import CheckInCommandHandler

class MainCommandHandler(BaseCommandHandler):
    def __init__(self):
        id = 1
        pl_table = [1, 1, 1, 1, 1]
        imbalance_tolerance = 3
        self.data_base = SQL_data_base(id, pl_table, imbalance_tolerance)
        #self.data_base.table_create()
        self.data_base.create_session()
        # self.data_base.init_repletion_data_base()
        # Класс для обработки QR
        self.qrdet = QR_detector()
        self.dict={}
        self.dict[0] = NomRequestCommandHandler(self.data_base)
        self.dict[1] = PartIdentificationCommandHandler(self.data_base,self.qrdet)
        self.dict[2] = CheckInCommandHandler(self.data_base, self.qrdet)

    def initFunction(self,code_request, parameter):
        result = None
        if code_request in self.dict:
            handler = self.dict[code_request]
            result = handler.execute(parameter)

        return result

        """
            # Инициализация картинки и кода запроса для работы приложения
        # code_request - код запроса к серверу, 3 цифры:
        # Сервер принимает (0) или передает данные (1)?
        # QR (0) или NN (1)?
        # 0 - отобразить деталь из БД (относится к QR и БД); 1 - обновить информацию по детали; 2 - вызов отчета
        if (code_request[0]==0):
            # Блок приема данных
            if (code_request[1] == 0):
                code = self.qrdet.main_detect(image)
                #Внесение изменений в БД
                result_of_query_search = self.data_base.search_for_id(code)
                return result_of_query_search
            elif (code_request[1] == 1):
                code = self.nndet.classification_NN(image,self.classification_model_nn)
                #Запрос к БД
                result_of_query_search = self.data_base.search_for_id(code)
                return result_of_query_search
        else:
            #Запрос к базе данных на получение списка видов деталей
            ciphers = self.data_base.list_of_parts()
            return ciphers
        """