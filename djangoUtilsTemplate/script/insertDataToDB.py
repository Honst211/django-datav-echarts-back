import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","djangoUtilsTemplate.settings")
django.setup()
import pandas as pd

from api.models import *


def get_file_path_by_name(file_dir):
    '''
    获取指定路径下所有文件的绝对路径
    :param file_dir:
    :return:
    '''
    L = []
    for root, dirs, files in os.walk(file_dir):  # 获取所有文件
        for file in files:  # 遍历所有文件名
            if os.path.splitext(file)[1] == '.xlsx':
                L.append(os.path.join(root, file))  # 拼接处绝对路径并放入列表
    return L

def getXlsxData(path,ncolsKeys):
    # 显示所有列
    pd.set_option('display.max_columns', None)
    # 显示所有行
    pd.set_option('display.max_rows', None)
    # 设置value的显示长度为100，默认为50
    pd.set_option('max_colwidth', 100)

    dfs = pd.read_excel(path,sheet_name=None)  # 读取所有的sheet数据
    resultList = []
    for key in list(dfs.keys()):
        df = dfs[key]
        # 处理Nan数据置换为None值
        df = df.where(df.notnull(), None)

        # 合并后的单元格会丢失值,在这里每一行仅需要处理time_pod下的数据
        df.iloc[5,0] = df.iloc[4,0]
        df.iloc[7,0] = df.iloc[6,0]
        df.iloc[8,0] = df.iloc[6,0]
        df.iloc[10,0] = df.iloc[9,0]

        # 数据处理,实际需要数据值为6-12行,因为涉及到细节部分,因此代码嵌套率较高,必须要求Excel中的文件格式没有差别,无法直接使用to_dict来解析这个Excel文件
        ncols = df.columns.size # 获取最大列

        # ncolsKeys = ["time_pod","time_interval","false_welding","continuous_tin","deviation",
        #             "broken_copper","tin_beads","fuzzing","reverse_line","yield",
        #             None,None,None,None,None,                   # 一共5列数据为空的,这里将key设置为空来作为预留条件,最好的方法是解析上一列数据后制作中英互译的对照表来进行处理
        #             "bad_quantity","defective_rate","remark"]
        for i in range(4, 11):
            # 读取row的6-12行数据,但是在从Excel转换为df文件时,数据出现了合并,认为第一行为header被忽略,且数值是从0开始
            # 因此获取Excel中6-12行数据是从数字4-10获取,(4,11)左闭右开,取值范围为4-10
            resultDict = {}
            bad_quantity = 0
            for j in range(ncols):
                ncolsKey = ncolsKeys[j]
                ilocData = df.iloc[i, j]
                if ncolsKey == None:
                    # 数据为None的不进行处理
                    continue

                if ilocData == None:
                    ilocData = 0
                # 数据处理
                if j > 1 and j < 14 and ilocData != None:
                    bad_quantity += ilocData

                if ncolsKey == "bad_quantity":
                    # bad_quantity在ncolsKeys参数14后才行,否则计算会存在问题
                    resultDict[ncolsKey] = bad_quantity
                    continue

                if ncolsKey == "defective_rate" and resultDict['yield_d'] != None:
                    if resultDict['yield_d'] == 0:
                        continue

                    resultDict[ncolsKey] = round(bad_quantity / resultDict['yield_d'],4)
                    continue

                # 将指定数据封装为dict数据
                resultDict[ncolsKey] = ilocData
                # 每一列数据进行extend补充数据,补充分别为班次,品名,日期,核准,审核,填表人,任务单号
                resultDict['d_class'] = df.iloc[1, 3]
                resultDict['product_name'] = df.iloc[1, 7]
                resultDict['date'] = df.iloc[1, 14]
                resultDict['approval'] = df.iloc[12, 2]
                resultDict['to_examine'] = df.iloc[12, 6]
                resultDict['completed_by'] = df.iloc[12, 12]
                resultDict['sn'] = df.iloc[12, 14]

            resultList.append(resultDict)

    return resultList

def filteFile(allPath):
    result = {'12车间PCB板外检工段':[],"成型车间SP外检工段":[],"电子车间外检工段":[],"电子车间测试工段":[]}
    for key in list(result.keys()):
        for path in allPath:
            if key in path:
                ncolsKeys = getNcolsKeys(key)
                data = getXlsxData(path,ncolsKeys)
                result[key].extend(data)

    return result

def getNcolsKeys(key):
    if key == '12车间PCB板外检工段':
        ncolsKeys = ["time_pod", "time_interval", "false_welding", "continuous_tin", "deviation",
                     "broken_copper", "tin_beads", "fuzzing", "reverse_line",
                     None, None, None, None, None,  # 一共5列数据为空的,这里将key设置为空来作为预留条件,最好的方法是解析上一列数据后制作中英互译的对照表来进行处理
                     "yield_d","bad_quantity", "defective_rate", "remark"]

    elif key == '成型车间SP外检工段':
        ncolsKeys = ["time_pod", "time_interval","material_grain", "rubber_punching", "lack_of_glue", "dirty_seal", "shrink",
                     "leaky_line", "crack", "eye_of_needle", "variegated", "line_pressing","other", "clearance",
                     "yield_d","bad_quantity", "defective_rate", "remark"]

    elif key == '电子车间外检工段':
        ncolsKeys = ["time_pod", "time_interval", "PCB_board", "wire_rod", "SP",
                     "air_traffic_control","gluing", "f_2C", "f_5C", "f_2C_leakage",
                     "f_5C_leakage", "core_wire", "size", None,  # 一共1列数据为空的,这里将key设置为空来作为预留条件,最好的方法是解析上一列数据后制作中英互译的对照表来进行处理
                     "yield_d","bad_quantity", "defective_rate", "remark"]

    elif key == '电子车间测试工段':
        ncolsKeys = ["time_pod", "time_interval", "short_circuit", "open_circuit", "insulation",
                     "copper_wire_mix_and_match", None, None, None,
                     None, None, None, None, None,  # 一共8列数据为空的,这里将key设置为空来作为预留条件,最好的方法是解析上一列数据后制作中英互译的对照表来进行处理
                     "yield_d","bad_quantity", "defective_rate", "remark"]
    else:
        raise RuntimeError("无效Key值,执行出错,检查是否存在缺少的文件名作为key")

    return ncolsKeys

def insertToDB(result):
    for key in list(result.keys()):
        insertModelData = []
        if key == "12车间PCB板外检工段":
            model = ExternalInspectionSectionForPCB
        elif key == "成型车间SP外检工段":
            model = ExternalInspectionSectionForSP
        elif key == "电子车间外检工段":
            model = ExternalInspectionSectionForElectronics
        elif key == "电子车间测试工段":
            model = TestSectionForElectronics
        else:
            raise RuntimeError("无效Key值,执行出错,检查是否存在缺少的文件名作为key")

        dataList = result[key]

        # print(dataList)
        for data in dataList:
            insertModelData.append(model(**data))

        model.objects.bulk_create(insertModelData)

if __name__ == '__main__':
    current_work_dir = os.path.dirname(__file__)
    allFilePath = get_file_path_by_name(current_work_dir + '/data')

    result = filteFile(allFilePath)

    insertToDB(result)
