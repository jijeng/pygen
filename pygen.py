# -*- coding: utf-8 -*
class pygen():
    """
    Personal Information generator for Chinese
    """

    def __init__(self, seed=None):
        """
        Initiates the class and creates a Faker() object for later data generation by other methods
        seed: User can set a seed parameter to generate deterministic, non-random output
        """
        from faker import Faker
        import pandas as pd
        from random import randint,choice

        self.fake = Faker()
        self.seed = seed
        self.randnum = randint(1, 9)

        self.city_list = self._initialize_city_list()
        self.domain_list = self._initialize_email_domain_list()
        self.firstname_list =self._initialize_firstname_list()
        self.lastname_list =self._initialize_lastname_list()


    def _initialize_city_list(self):
        import os
        from six import moves
        import ssl

        path = "China_Cities.txt"
        if not os.path.isfile(path):
            print("Not found txt file...")
            context = ssl._create_unverified_context()
            moves.urllib.request.urlretrieve(
                "https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/US_Cities.txt", path)

        city_list = []
        with open(path) as fh:
            city_list = [str(line).strip() for line in fh.readlines()]

        return city_list

    def _initialize_email_domain_list(self):
        import os
        from six import moves
        import ssl

        dir_path = os.path.dirname('./')
        path = dir_path + os.sep + "Mails.txt"

        if not os.path.isfile(path):
            print("Not found txt file...")
            context = ssl._create_unverified_context()
            moves.urllib.request.urlretrieve(
                "https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/US_Cities.txt", path)

        domain_list = []
        with open(path) as fh:
            domain_list = [str(line).strip() for line in fh.readlines()]

        return domain_list
    def _initialize_lastname_list(self):
        import os
        from six import moves
        import ssl

        dir_path =os.path.dirname('./')
        path =dir_path+os.sep +'last_name.txt'

        if not os.path.isfile(path):
            print("Not found txt file...")
            context = ssl._create_unverified_context()
            moves.urllib.request.urlretrieve(
                "https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/US_Cities.txt", path)

        lastname =[]
        with open(path) as fh:
            lastname =[ str(line).strip() for line in fh.readlines()]
        return lastname

    def _initialize_firstname_list(self):
        import os
        from six import moves
        import ssl

        dir_path = os.path.dirname('./')
        path = dir_path + os.sep + 'first_name.txt'
        if not os.path.isfile(path):
            print("Not found txt file...")
            context = ssl._create_unverified_context()
            moves.urllib.request.urlretrieve(
                "https://raw.githubusercontent.com/tflearn/tflearn.github.io/master/resources/US_Cities.txt", path)

        first_name = []
        with open(path) as fh:
            first_name = [str(line).strip() for line in fh.readlines()]
        return first_name

    def city_real(self, seed=None):
        '''
        Picks and returns a random entry out of China cities
        seed: Currently not used. Uses seed from the pydb class if chosen by user
        '''
        import os
        from six import moves
        import ssl
        import random
        from random import randint,choice
        random.seed(self.seed)

        return (choice(self.city_list))


    def _name(self, seed =None):
        '''
        :param seed: not used
        :return: first_name + last_name in chinese
        '''
        import random
        from random import  choice
        random.seed(self.seed)
        return choice(self.lastname_list)+"\t"+choice(self.firstname_list)

    def name(self, seed=None):

        return_name =self._name(seed =seed)
        return_name= return_name.split("\t")
        if len(return_name)==2:
            return return_name[0]+return_name[1]


    def realistic_email(self, name, seed=None):
        '''
        Generates realistic email from first and last name and a random domain address
        seed: Currently not used. Uses seed from the pydb class if chosen by user

        giving name, get the mail
        '''
        import random
        from random import randint,choice
        random.seed(self.seed)

        name = str(name)
        f_name = name.split()[0]
        l_name = name.split()[-1]

        choice_int = choice(range(10))

        domain_list = self._initialize_email_domain_list()
        domain = choice(domain_list)
        # types of formats
        name_formats = ["{f}{last}", "{first}{last}",
                        "{first}.{l}", "{first}_{l}",
                        "{first}.{last}", "{first}_{last}",
                        "{last}_{first}", "{last}.{first}"]
        name_fmt_choice = choice(name_formats)
        name_combo = name_fmt_choice.format(
            f=f_name[0], l=l_name[0], first=f_name, last=l_name)

        if choice_int < 7:
            email = name_combo + '@' + str(domain)
        else:
            random_int = randint(11, 99)
            email = name_combo + str(random_int) + '@' + str(domain)

        return email


    def simple_ph_num(self, seed=None, types=0, format=False):
        """
        Generates 11 digit China phone number in xxx-xxxx-xxxx format
        seed: Currently not used. Uses seed from the pydb class if chosen by user
        types: choice {0,1,2,3}, default ==0, 0: 随机产生"真实"的号码，1：产生移动字段的电话号码， 2：产生联通字段，3：产生电信字段
        format: 是否按照 xxx-xxxx-xxxx format 格式输出
        """
        import random
        from random import randint,choice
        random.seed(self.seed)


        list1 = [134, 135, 136, 137, 138, 139, 147, 148, 150, 151, 152, 157, 158, 159, 178, 182, 183, 184, 187, 188,
                 198, 1440, 1703, 1705, 1706]
        # 联通
        list2 = [130, 131, 132, 155, 156, 185, 186, 145, 146, 166, 167, 175, 176, 1704, 1707, 1708, 1709, 1710, 1711,
                 1712, 1713, 1714, 1715, 1716, 1717, 1718, 1719]
        # 电信
        list3 = [133, 153, 177, 180, 181, 189, 191, 199, 1349, 1410, 1700, 1701, 1702, 1740]

        if types == 0:
            types = random.choice([1, 2, 3])

        result = ''
        if types == 1:
            result += str(random.choice(list1))
        elif types == 2:
            result += str(random.choice(list2))
        elif types == 3:
            result += str(random.choice(list3))
        else:
            return " Error"

        if len(result) == 3:
            for _ in range(4):
                result += str(randint(0, 9))
        else:
            for _ in range(3):
                result += str(randint(0, 9))

        for _ in range(4):
            result += str(randint(0, 9))

        if format:
            phone_format = "{p1}-{p2}-{p3}"
            p1 = result[:3]
            p2 = result[3:7]
            p3 = result[7:]
            return phone_format.format(p1=p1, p2=p2, p3=p3)

        return result


    def get_check_digit(self, id_number):
        """通过身份证号获取校验码"""
        check_sum = 0
        for i in range(0, 17):
            check_sum += ((1 << (17 - i)) % 11) * int(id_number[i])
        check_digit = (12 - (check_sum % 11)) % 11
        return check_digit if check_digit < 10 else 'X'


    def generate_id(self, sex=None):
        """随机生成身份证号，sex = 0表示女性，sex = 1表示男性"""
        import random
        from datetime  import datetime, timedelta
        import constant as const

        if sex == None:

            sex = random.choice([0, 1])


        # 随机生成一个区域码(6位数)
        id_number = str(random.choice(list(const.AREA_INFO.keys())))
        # 限定出生日期范围(8位数)
        start, end = datetime.strptime("1919-01-01", "%Y-%m-%d"), datetime.strptime("2019-04-20", "%Y-%m-%d")
        birth_days = datetime.strftime(start + timedelta(random.randint(0, (end - start).days + 1)), "%Y%m%d")
        id_number += str(birth_days)
        # 顺序码(2位数)
        id_number += str(random.randint(10, 99))
        # 性别码(1位数)
        id_number += str(random.randrange(sex, 10, step=2))
        # 校验码(1位数)
        id_number += str(self.get_check_digit(id_number))

        return id_number


    def verify_id(self, id_number):
        """校验身份证是否正确"""
        import re
        import constant as const
        
        if re.match(const.ID_NUMBER_18_REGEX, id_number):
            # check_digit = cls(id_number).get_check_digit()
            check_digit = self.get_check_digit(id_number)

            return str(check_digit) == id_number[-1]
        else:
            return bool(re.match(const.ID_NUMBER_15_REGEX, id_number))

    def license_plate(self, seed=None, style=None):
        """
        Generates vehicle license plate number in 3 possible styles
        Style can be 1, 2, or 3.
        - 9ABC123 format
        - ABC-1234 format
        - ABC-123 format
        If style is not specified by user, a random style is chosen at runtime
        seed: Currently not used. Uses seed from the pydb class if chosen by user
        """
        import random
        from random import randint,choice
        random.seed(self.seed)
        

        if not style:
            style = choice([1, 2, 3])

        license_place_format = "{p1}{p2}{p3}"

        if style == 1:
            p1 = str(randint(1, 9))
            p2 = "".join([chr(randint(65, 90)) for _ in range(3)])
            p3 = "".join([str(randint(1, 9)) for _ in range(3)])
        elif style == 2:
            p1 = "".join([chr(randint(65, 90)) for _ in range(3)])
            p2 = "-"
            p3 = "".join([str(randint(0, 9)) for _ in range(4)])
        else:
            p1 = "".join([chr(randint(65, 90)) for _ in range(3)])
            p2 = "-"
            p3 = "".join([str(randint(0, 9)) for _ in range(3)])

        return license_place_format.format(p1=p1, p2=p2, p3=p3)

    def gen_data_series(self, num=10, data_type='name', seed=None):
        """
        Returns a pandas series object with the desired number of entries and data type

        Data types available:
        - Name, country, city, real (US) cities, US state, zipcode, latitude, longitude
        - Month, weekday, year, time, date
        - Personal email, official email, SSN
        - Company, Job title, phone number, license plate

        Phone number can be two types:
        'phone_number_simple' generates 10 digit US number in xxx-xxx-xxxx format
        'phone_number_full' may generate an international number with different format

        seed: Currently not used. Uses seed from the pydb class if chosen by user
        """
        import pandas as pd
        if type(data_type) != str:
            raise ValueError(
                "Data type must be of type str, found " + str(type(data_type)))
        try:
            num = int(num)
        except:
            raise ValueError(
                'Number of samples must be a positive integer, found ' + num)

        if num <= 0:
            raise ValueError(
                'Number of samples must be a positive integer, found ' + num)

        num = int(num)
        fake = self.fake
        fake.seed(self.seed)

        func_lookup = {
            # 'name': fake.name,
            'name': self.name,
            'country': fake.country,
            'street_address': fake.street_address,
            'city': fake.city,
            'real_city': self.city_real,
            'state': fake.state,
            'zipcode': fake.zipcode,
            'latitude': fake.latitude,
            'longitude': fake.longitude,
            'name_month': fake.month_name,
            'weekday': fake.day_of_week,
            'year': fake.year,
            'time': fake.time,
            'date': fake.date,
            # 'ssn': fake.ssn,
            'ssn': self.generate_id,
            'email': fake.email,
            'office_email': fake.company_email,
            'company': fake.company,
            'job_title': fake.job,
            'phone_number_simple': self.simple_ph_num,
            'phone_number_full': fake.phone_number,
            'license_plate': self.license_plate
        }

        if data_type not in func_lookup:
            raise ValueError("Data type must be one of " +
                             str(list(func_lookup.keys())))

        datagen_func = func_lookup[data_type]
        return pd.Series((datagen_func() for _ in range(num)))

    def _validate_args(self, num, fields):
        try:
            num = int(num)
        except:
            raise ValueError(
                'Number of samples must be a positive integer, found ' + num)
        if num <= 0:
            raise ValueError(
                'Number of samples must be a positive integer, found ' + num)

        num_cols = len(fields)
        # 根据name 去生成 ssn的那种
        if 'ssn' in fields and 'name' not in fields:
            raise ValueError('Please provide name if you want ssn')

        if num_cols < 0:
            raise ValueError("Please provide at least one type of data field to be generated")


    def gen_dataframe(self, num=10, fields=['name'], real_email=True, real_city=True, phone_simple=True, seed=None):
        import pandas as pd
        """
        Generate a pandas dataframe filled with random entries.
        User can specify the number of rows and data type of the fields/columns

        Data types available:
        - Name, country, city, real (US) cities, US state, zipcode, latitude, longitude
        - Month, weekday, year, time, date
        - Personal email, official email, SSN
        - Company, Job title, phone number, license plate

        Further choices are following:
        real_email: If True and if a person's name is also included in the fields, a realistic email will be generated corresponding to the name
        real_city: If True, a real US city's name will be picked up from a list. Otherwise, a fictitious city name will be generated.
        phone_simple: If True, a 10 digit US number in the format xxx-xxx-xxxx will be generated. Otherwise, an international number with different format may be returned.

        seed: Currently not used. Uses seed from the pydb class if chosen by user

        """
        # 先决条件判断
        self._validate_args(num, fields)

        df = pd.DataFrame(data=self.gen_data_series(num, data_type=fields[0]), columns=[fields[0]])

        if 'name' in fields and 'ssn' in fields:
            name_list =[self._name()  for _ in range(num)]
            
            firstname_list =[name.split('\t')[-1] for name in name_list]
            lastname_list = [name.split('\t')[0] for name in name_list]
            name_list1 = [l + f for (l, f) in zip(lastname_list, firstname_list)]


            import namesex
            ns =namesex.namesex()
            gender_list =ns.predict(firstname_list)


            ssn_list = [self.generate_id(sex=gender) for gender in gender_list]
            dict1 ={'name':name_list1, 'ssn':ssn_list}

            df['name']=dict1['name']
            df['ssn'] =dict1['ssn']

            # add email to dataframe
            if 'email' in fields and real_email:

                from xpinyin import Pinyin
                p =Pinyin()
                f_pin_list =[p.get_pinyin(name) for name in firstname_list]
                l_pin_list =[p.get_pinyin(name) for name in lastname_list]
                name_list2 = [f + " " + l for (l, f) in zip(l_pin_list, f_pin_list)]
                mail_list = [self.realistic_email(name) for name in name_list2]
                df['mail'] =mail_list

                fields.remove('email')

            fields.remove('name')
            fields.remove('ssn')


        for col in fields:

            if col == 'phone':
                if phone_simple:
                    df['phone-number'] = self.gen_data_series(
                        num, data_type='phone_number_simple')
                else:
                    df['phone-number'] = self.gen_data_series(
                        num, data_type='phone_number_full')
            elif col == 'license_plate':
                df['license-plate'] = self.gen_data_series(num, data_type=col)
            elif col == 'city' and real_city:
                df['city'] = self.gen_data_series(num, data_type='real_city')
            else:

                df[col] = self.gen_data_series(num, data_type=col)

        if ('email' in fields) and ('name' in fields) and real_email:
            df['email'] = df['name'].apply(self.realistic_email)

        return df

    #
    def gen_table(self, num=10, fields=['name'], db_file=None, table_name=None, primarykey=None, real_email=True,
                  real_city=True, phone_simple=True, seed=None):
        """
        Attempts to create a table in a database (.db) file using Python's built-in SQLite engine.
        User can specify various data types to be included as database table fields.
        All data types (fields) in the SQLite table will be of VARCHAR type.

        Data types available:
        - Name, country, city, real  cities, zipcode, latitude, longitude
        - Month, weekday, year, time, date
        - Personal email, official email, SSN
        - Company, Job title, phone number, license plate

        Further choices are following:
        real_email: If True and if a person's name is also included in the fields, a realistic email will be generated corresponding to the name
        real_city: If True, a real  city's name will be picked up from a list. Otherwise, a fictitious city name will be generated.
        phone_simple: If True, a 10 digit number in the format xxx-xxx-xxxx will be generated. Otherwise, an international number with different format may be returned.

        Default database and table name will be chosen if not specified by user.
        Primarykey: User can choose a PRIMARY KEY from among the data type fields. If nothing specified, the first data field will be made PRIMARY KEY.

        seed: Currently not used. Uses seed from the pydb class if chosen by user

        """
        self._validate_args(num, fields)

        import sqlite3
        if not db_file:
            conn = sqlite3.connect('NewFakeDB.db')
            c = conn.cursor()
        else:
            conn = sqlite3.connect(str(db_file))
            c = conn.cursor()

        if type(primarykey) != str and primarykey is not None:
            print("Primary key type not identified. Not generating any table")
            return None

        # If primarykey is None, designate the first field as primary key
        if not primarykey:
            table_cols = '(' + str(fields[0]) + \
                         ' varchar PRIMARY KEY NOT NULL,'
            for col in fields[1:-1]:
                table_cols += str(col) + ' varchar,'
            table_cols += str(fields[-1]) + ' varchar' + ')'
            # print(table_cols)
        else:
            pk = str(primarykey)
            if pk not in fields:
                print(
                    "Desired primary key is not in the list of fields provided, cannot generate the table!")
                return None

            table_cols = '(' + str(fields[0]) + ' varchar, '
            for col in fields[1:-1]:
                if col == pk:
                    table_cols += str(col) + ' varchar PRIMARY KEY NOT NULL,'
                else:
                    table_cols += str(col) + ' varchar, '
            table_cols += str(fields[-1]) + ' varchar' + ')'
            # print(table_cols)

        if not table_name:
            table_name = 'Table1'
        else:
            table_name = table_name

        str_drop_table = "DROP TABLE IF EXISTS " + str(table_name) + ';'
        c.execute(str_drop_table)
        str_create_table = "CREATE TABLE IF NOT EXISTS " + \
                           str(table_name) + table_cols + ';'
        # print(str_create_table)
        c.execute(str_create_table)

        # Create a temporary df
        temp_df = self.gen_dataframe(
            num=num, fields=fields, real_email=real_email, real_city=real_city, phone_simple=phone_simple)
        # Use the dataframe to insert into the table
        for i in range(num):
            str_insert = "INSERT INTO " + table_name + \
                         " VALUES " + str(tuple(temp_df.iloc[i])) + ';'
            c.execute(str_insert)

        # Commit the insertions and close the connection
        conn.commit()
        conn.close()

    def gen_excel(self, num=10, fields=['name'], filename='NewExcel.xlsx', real_email=True, real_city=True,
                  phone_simple=True, seed=None):
        """
        Attempts to create an Excel file using Pandas excel_writer function.
        User can specify various data types to be included as fields.

        Data types available:
        - Name, country, city, real (US) cities, US state, zipcode, latitude, longitude
        - Month, weekday, year, time, date
        - Personal email, official email, SSN
        - Company, Job title, phone number, license plate

        Further choices are following:
        real_email: If True and if a person's name is also included in the fields, a realistic email will be generated corresponding to the name
        real_city: If True, a real US city's name will be picked up from a list. Otherwise, a fictitious city name will be generated.
        phone_simple: If True, a 10 digit US number in the format xxx-xxx-xxxx will be generated. Otherwise, an international number with different format may be returned.

        Default file name will be chosen if not specified by user.

        seed: Currently not used. Uses seed from the pydb class if chosen by user

        """
        self._validate_args(num, fields)

        # Create a temporary dataframe
        temp_df = self.gen_dataframe(
            num=num, fields=fields, real_email=real_email, real_city=real_city, phone_simple=phone_simple)
        # Use the dataframe to write to an Excel file using Pandas built-in function
        temp_df.to_excel(filename)

    def gen_csv(self, num=10, fields=['name'], filename='NewExcel.csv', real_email=True, real_city=True,
                  phone_simple=True, seed=None):
        """
        Attempts to create an Excel file using Pandas excel_writer function.
        User can specify various data types to be included as fields.
        almost same as above gen_excel

        """
        self._validate_args(num, fields)

        temp_df = self.gen_dataframe(
            num=num, fields=fields, real_email=real_email, real_city=real_city, phone_simple=phone_simple)
        # Use the dataframe to write to an Excel file using Pandas built-in function
        temp_df.to_csv(filename, sep='\t', encoding ='utf-8')

