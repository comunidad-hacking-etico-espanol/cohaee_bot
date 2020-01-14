import logging
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#TODO crear funcion para modificar los datos
class GoogleSheet:
    __scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    __creds = ServiceAccountCredentials.from_json_keyfile_name('gdrive.json', __scope)
    __GOOGLE_CLIENT = gspread.authorize(__creds)

    def __init__(self, file, norm, logger=None):
        self.__file = file
        self.__norm = norm
        self.__logger = logging.getLogger()

    def __log(self, log):
        self.__logger.info(log)

    def __get_sheet(self):
        try:
            sheet = self.__GOOGLE_CLIENT.open(self.__file).sheet1.get_all_values()
        except Exception as error:
            self.__log("GoogleSheet Error: {}".format(self.__file))
            self.__log("Exception: {}".format(type(error)))
            self.__log("Args: {}".format(error.args))
            self.__log("Error: {}".format(error))
            return []
        return sheet

    def get_data(self):
        return [self.__norm(row) for row in self.__get_sheet()]
