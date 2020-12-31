from aip import AipOcr

# 认证信息
APP_ID = '23420526'
API_KEY = 'OBNFyivUp8XtIMFu6Sbd3CWS'
SECRET_KEY = '6tyIH4cX1Ib0KqLwQm8qgzFZ49UCP4FY'


def get_ocr_str(file_path, origin_format=True):
    """
    图片转文字
    :param file_path: 图片路径
    :return:
    """
    with open(file_path, 'rb') as fp:
        file_bytes = fp.read()
    return get_ocr_str_from_bytes(file_bytes, origin_format)


def get_ocr_str_from_bytes(file_bytes, origin_format=True):
    """
    图片转文字
    :param file_bytes: 图片的字节
    :return:
    """
    options = {
        'detect_direction': 'false',
        'language_type': 'CHN_ENG',
    }
    ocr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    result_dict = ocr.basicGeneral(file_bytes, options)
    if origin_format:
        result_str = '\n'.join([entity['words'] for entity in result_dict['words_result']])
    else:
        result_str = ''.join([entity['words'] for entity in result_dict['words_result']])
    return result_str


if __name__ == '__main__':
    IMAGE_PATH = "./tmp/v2-2657fddd956e8764dd584dd82c1f6926_720w.jpg"
    str = get_ocr_str(IMAGE_PATH)
    str = str.replace("\n", "")
    print(str)
    print("======================")
    idx = str.find("打卡成功")
    print(idx)
