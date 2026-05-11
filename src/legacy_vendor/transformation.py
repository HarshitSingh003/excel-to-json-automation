'''
Summery Line
    Data type transformation
'''
from datetime import datetime

class DataTypeTransformation:
    '''
    Summery Line
        Data type transformation
    '''
    def __str__(self):
        '''
        Summery Line
            object representation
        '''
        return "DataTypeTransformation object"

    def zipcode_transform(data):
        '''
        Summery Line
            data transformation
        Parameters:
            data(): transform data
        Return:
            data(): after transform
        '''
        try:
            if isinstance(data, int):
                if 1001 <= data <= 9028:
                    data = '0' + str(data)
                else:
                    data = str(data)
            else:
                data = str(data)
        except Exception:
            pass
        return data
    
    def str_transform(data):
        '''
        Summery Line
            data transformation
        Parameters:
            data(): transform data
        Return:
            data(): after transform
        '''
        try:
            data = str(data)
        except Exception:
            pass
        return data

    def int_transformation(data):
        '''
        Summery Line
            data transformation
        Parameters:
            data(): transform data
        Return:
            data(): after transform
        '''
        try:
            data = int(data)
        except Exception:
            pass
        return data

    def float_transformation(data):
        '''
        Summery Line
            data transformation
        Parameters:
            data(): transform data
        Return:
            data(): after transform
        '''
        try:
            data = round(float(data), 2)
        except Exception:
            pass
        return data

    def float_transformation_without_roundof(data):
        '''
        Summery Line
            data transformation
        Parameters:
            data(): transform data
        Return:
            data(): after transform
        '''
        try:
            data = float(data)
        except Exception:
            pass
        return data

    def date_transform(data):
        '''
        Summery Line
            Here we are transforming the date in schema format
        '''
        all_dt_list = ["%d/%m/%Y", "%Y/%m/%d", "%m/%d/%Y", "%d-%m-%Y", \
            "%Y-%m-%d", "%d-%m-%y", "%d.%m.%Y", "%d-%b-%y", "%d-%b-%Y", "%d/%b/%Y", "%d/%m/%y"]
        for dt in all_dt_list:
            try:
                data = datetime.strptime(data, dt).strftime('%Y-%m-%d')
                break
            except Exception as error:
                pass
        return data

    def int_transformation_single(data):
        try:
            num = float(data)
            if num.is_integer():
                trasformed_data = int(num)
            else:
                trasformed_data = round(num,2)
        except Exception as e:
            pass

        return trasformed_data