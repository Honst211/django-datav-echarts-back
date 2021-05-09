from django.db.models import Sum
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from api.models import ExternalInspectionSectionForPCB, ExternalInspectionSectionForSP, \
    ExternalInspectionSectionForElectronics, TestSectionForElectronics


class centerLeftView(APIView):
    def get(self,request):
        """获取AE下每天生产总量,失败总量和,失败率"""
        externalInspectionSectionForPCBs = ExternalInspectionSectionForPCB.objects.exclude(yield_d=0).values("yield_d","bad_quantity","defective_rate","date")
        externalInspectionSectionForSPs = ExternalInspectionSectionForSP.objects.exclude(yield_d=0).values("yield_d","bad_quantity","defective_rate","date")
        externalInspectionSectionForElectronicss = ExternalInspectionSectionForElectronics.objects.exclude(yield_d=0).values("yield_d","bad_quantity","defective_rate","date")
        testSectionForElectronicss = TestSectionForElectronics.objects.exclude(yield_d=0).values("yield_d","bad_quantity","defective_rate","date")

        resultData = {}
        for externalInspectionSectionForPCB in externalInspectionSectionForPCBs:
            if externalInspectionSectionForPCB['date'] in list(resultData.keys()):
                resultData[externalInspectionSectionForPCB['date']]['yield_d'] += externalInspectionSectionForPCB['yield_d']
                resultData[externalInspectionSectionForPCB['date']]['bad_quantity'] += externalInspectionSectionForPCB['bad_quantity']
                resultData[externalInspectionSectionForPCB['date']]['defective_rate'] += externalInspectionSectionForPCB['defective_rate']
                resultData[externalInspectionSectionForPCB['date']]['count'] += 1
            else:
                resultData[externalInspectionSectionForPCB['date']] = {}
                resultData[externalInspectionSectionForPCB['date']]['yield_d'] = externalInspectionSectionForPCB['yield_d']
                resultData[externalInspectionSectionForPCB['date']]['bad_quantity'] = externalInspectionSectionForPCB['bad_quantity']
                resultData[externalInspectionSectionForPCB['date']]['defective_rate'] = externalInspectionSectionForPCB['defective_rate']
                resultData[externalInspectionSectionForPCB['date']]['count'] = 1

        for externalInspectionSectionForSP in externalInspectionSectionForSPs:
            if externalInspectionSectionForSP['date'] in list(resultData.keys()):
                resultData[externalInspectionSectionForSP['date']]['yield_d'] += externalInspectionSectionForSP['yield_d']
                resultData[externalInspectionSectionForSP['date']]['bad_quantity'] += externalInspectionSectionForSP['bad_quantity']
                resultData[externalInspectionSectionForSP['date']]['defective_rate'] += externalInspectionSectionForSP['defective_rate']
                resultData[externalInspectionSectionForSP['date']]['count'] += 1
            else:
                resultData[externalInspectionSectionForSP['date']] = {}
                resultData[externalInspectionSectionForSP['date']]['yield_d'] = externalInspectionSectionForSP['yield_d']
                resultData[externalInspectionSectionForSP['date']]['bad_quantity'] = externalInspectionSectionForSP['bad_quantity']
                resultData[externalInspectionSectionForSP['date']]['defective_rate'] = externalInspectionSectionForSP['defective_rate']
                resultData[externalInspectionSectionForSP['date']]['count'] = 1

        for externalInspectionSectionForElectronics in externalInspectionSectionForElectronicss:
            if externalInspectionSectionForElectronics['date'] in list(resultData.keys()):
                resultData[externalInspectionSectionForElectronics['date']]['yield_d'] += externalInspectionSectionForElectronics['yield_d']
                resultData[externalInspectionSectionForElectronics['date']]['bad_quantity'] += externalInspectionSectionForElectronics['bad_quantity']
                resultData[externalInspectionSectionForElectronics['date']]['defective_rate'] += externalInspectionSectionForElectronics['defective_rate']
                resultData[externalInspectionSectionForElectronics['date']]['count'] += 1
            else:
                resultData[externalInspectionSectionForElectronics['date']] = {}
                resultData[externalInspectionSectionForElectronics['date']]['yield_d'] = externalInspectionSectionForElectronics['yield_d']
                resultData[externalInspectionSectionForElectronics['date']]['bad_quantity'] = externalInspectionSectionForElectronics['bad_quantity']
                resultData[externalInspectionSectionForElectronics['date']]['defective_rate'] = externalInspectionSectionForElectronics['defective_rate']
                resultData[externalInspectionSectionForElectronics['date']]['count'] = 1

        for testSectionForElectronics in testSectionForElectronicss:
            if testSectionForElectronics['date'] in list(resultData.keys()):
                resultData[testSectionForElectronics['date']]['yield_d'] += testSectionForElectronics['yield_d']
                resultData[testSectionForElectronics['date']]['bad_quantity'] += testSectionForElectronics['bad_quantity']
                resultData[testSectionForElectronics['date']]['defective_rate'] += testSectionForElectronics['defective_rate']
                resultData[testSectionForElectronics['date']]['count'] += 1
            else:
                resultData[testSectionForElectronics['date']] = {}
                resultData[testSectionForElectronics['date']]['yield_d'] = testSectionForElectronics['yield_d']
                resultData[testSectionForElectronics['date']]['bad_quantity'] = testSectionForElectronics['bad_quantity']
                resultData[testSectionForElectronics['date']]['defective_rate'] = testSectionForElectronics['defective_rate']
                resultData[testSectionForElectronics['date']]['count'] = 1

        result = {}
        result['category'] = list(resultData.keys())
        result['lineData'] = [resultData[key]['yield_d'] for key in resultData.keys()]
        result['barData'] = [resultData[key]['bad_quantity'] for key in resultData.keys()]

        data = {
            "code": 200,
            "data": result,
            "msg": ""
        }

        return JsonResponse(data)


class bottomLeftView(APIView):
    def get(self,request):
        """获取AE下所有数据的上午,下午,加班的生产总数,失败总数及其失败率"""
        externalInspectionSectionForPCBs = ExternalInspectionSectionForPCB.objects.exclude(yield_d=0).values("yield_d", "bad_quantity", "defective_rate", "time_pod")
        externalInspectionSectionForSPs = ExternalInspectionSectionForSP.objects.exclude(yield_d=0).values("yield_d","bad_quantity","defective_rate","time_pod")
        externalInspectionSectionForElectronicss = ExternalInspectionSectionForElectronics.objects.exclude(yield_d=0).values("yield_d", "bad_quantity", "defective_rate", "time_pod")
        testSectionForElectronicss = TestSectionForElectronics.objects.exclude(yield_d=0).values("yield_d","bad_quantity","defective_rate","time_pod")

        resultData = {}
        for externalInspectionSectionForPCB in externalInspectionSectionForPCBs:
            if externalInspectionSectionForPCB['time_pod'] in list(resultData.keys()):
                resultData[externalInspectionSectionForPCB['time_pod']]['yield_d'] += externalInspectionSectionForPCB['yield_d']
                resultData[externalInspectionSectionForPCB['time_pod']]['bad_quantity'] += externalInspectionSectionForPCB['bad_quantity']
                resultData[externalInspectionSectionForPCB['time_pod']]['defective_rate'] += externalInspectionSectionForPCB['defective_rate']
                resultData[externalInspectionSectionForPCB['time_pod']]['count'] += 1
            else:
                resultData[externalInspectionSectionForPCB['time_pod']] = {}
                resultData[externalInspectionSectionForPCB['time_pod']]['yield_d'] = externalInspectionSectionForPCB['yield_d']
                resultData[externalInspectionSectionForPCB['time_pod']]['bad_quantity'] = externalInspectionSectionForPCB['bad_quantity']
                resultData[externalInspectionSectionForPCB['time_pod']]['defective_rate'] = externalInspectionSectionForPCB['defective_rate']
                resultData[externalInspectionSectionForPCB['time_pod']]['count'] = 1

        for externalInspectionSectionForSP in externalInspectionSectionForSPs:
            if externalInspectionSectionForSP['time_pod'] in list(resultData.keys()):
                resultData[externalInspectionSectionForSP['time_pod']]['yield_d'] += externalInspectionSectionForSP['yield_d']
                resultData[externalInspectionSectionForSP['time_pod']]['bad_quantity'] += externalInspectionSectionForSP['bad_quantity']
                resultData[externalInspectionSectionForSP['time_pod']]['defective_rate'] += externalInspectionSectionForSP['defective_rate']
                resultData[externalInspectionSectionForSP['time_pod']]['count'] += 1
            else:
                resultData[externalInspectionSectionForSP['time_pod']] = {}
                resultData[externalInspectionSectionForSP['time_pod']]['yield_d'] = externalInspectionSectionForSP['yield_d']
                resultData[externalInspectionSectionForSP['time_pod']]['bad_quantity'] = externalInspectionSectionForSP['bad_quantity']
                resultData[externalInspectionSectionForSP['time_pod']]['defective_rate'] = externalInspectionSectionForSP['defective_rate']
                resultData[externalInspectionSectionForSP['time_pod']]['count'] = 1

        for externalInspectionSectionForElectronics in externalInspectionSectionForElectronicss:
            if externalInspectionSectionForElectronics['time_pod'] in list(resultData.keys()):
                resultData[externalInspectionSectionForElectronics['time_pod']]['yield_d'] += externalInspectionSectionForElectronics['yield_d']
                resultData[externalInspectionSectionForElectronics['time_pod']]['bad_quantity'] += externalInspectionSectionForElectronics['bad_quantity']
                resultData[externalInspectionSectionForElectronics['time_pod']]['defective_rate'] += externalInspectionSectionForElectronics['defective_rate']
                resultData[externalInspectionSectionForElectronics['time_pod']]['count'] += 1
            else:
                resultData[externalInspectionSectionForElectronics['time_pod']] = {}
                resultData[externalInspectionSectionForElectronics['time_pod']]['yield_d'] = externalInspectionSectionForElectronics['yield_d']
                resultData[externalInspectionSectionForElectronics['time_pod']]['bad_quantity'] = externalInspectionSectionForElectronics['bad_quantity']
                resultData[externalInspectionSectionForElectronics['time_pod']]['defective_rate'] = externalInspectionSectionForElectronics['defective_rate']
                resultData[externalInspectionSectionForElectronics['time_pod']]['count'] = 1

        for testSectionForElectronics in testSectionForElectronicss:
            if testSectionForElectronics['time_pod'] in list(resultData.keys()):
                resultData[testSectionForElectronics['time_pod']]['yield_d'] += testSectionForElectronics['yield_d']
                resultData[testSectionForElectronics['time_pod']]['bad_quantity'] += testSectionForElectronics['bad_quantity']
                resultData[testSectionForElectronics['time_pod']]['defective_rate'] += testSectionForElectronics['defective_rate']
                resultData[testSectionForElectronics['time_pod']]['count'] += 1
            else:
                resultData[testSectionForElectronics['time_pod']] = {}
                resultData[testSectionForElectronics['time_pod']]['yield_d'] = testSectionForElectronics['yield_d']
                resultData[testSectionForElectronics['time_pod']]['bad_quantity'] = testSectionForElectronics['bad_quantity']
                resultData[testSectionForElectronics['time_pod']]['defective_rate'] = testSectionForElectronics['defective_rate']
                resultData[testSectionForElectronics['time_pod']]['count'] = 1

        for result in resultData.values():
            result['defective_rate_r'] = round(result['defective_rate'] / result['count'], 4)

        data = {
            "code": 200,
            "data": resultData,
            "msg": ""
        }

        return JsonResponse(data)


class bottomRightView(APIView):
    def get(self,request):
        """获取AE下各个车间中所有数据的上午,下午,加班的生产总数"""
        externalInspectionSectionForPCBs = ExternalInspectionSectionForPCB.objects.exclude(yield_d=0).values("yield_d", "time_pod")
        externalInspectionSectionForSPs = ExternalInspectionSectionForSP.objects.exclude(yield_d=0).values("yield_d","time_pod")
        externalInspectionSectionForElectronicss = ExternalInspectionSectionForElectronics.objects.exclude(yield_d=0).values("yield_d", "time_pod")
        testSectionForElectronicss = TestSectionForElectronics.objects.exclude(yield_d=0).values("yield_d","time_pod")

        externalInspectionSectionForPCB_result = {}
        for externalInspectionSectionForPCB in externalInspectionSectionForPCBs:
            if externalInspectionSectionForPCB['time_pod'] in list(externalInspectionSectionForPCB_result.keys()):
                externalInspectionSectionForPCB_result[externalInspectionSectionForPCB['time_pod']] += externalInspectionSectionForPCB['yield_d']
            else:
                externalInspectionSectionForPCB_result[externalInspectionSectionForPCB['time_pod']] = externalInspectionSectionForPCB['yield_d']

        externalInspectionSectionForPCB_resultList = []
        for key in list(externalInspectionSectionForPCB_result.keys()):
            data = {
                "name": key,
                "value": externalInspectionSectionForPCB_result[key]
            }
            externalInspectionSectionForPCB_resultList.append(data)

        externalInspectionSectionForSP_result = {}
        for externalInspectionSectionForSP in externalInspectionSectionForSPs:
            if externalInspectionSectionForSP['time_pod'] in list(externalInspectionSectionForSP_result.keys()):
                externalInspectionSectionForSP_result[externalInspectionSectionForSP['time_pod']] += externalInspectionSectionForSP['yield_d']
            else:
                externalInspectionSectionForSP_result[externalInspectionSectionForSP['time_pod']] = externalInspectionSectionForSP['yield_d']

        externalInspectionSectionForSP_resultList = []
        for key in list(externalInspectionSectionForSP_result.keys()):
            data = {
                "name": key,
                "value": externalInspectionSectionForSP_result[key]
            }
            externalInspectionSectionForSP_resultList.append(data)

        externalInspectionSectionForElectronics_result = {}
        for externalInspectionSectionForElectronics in externalInspectionSectionForElectronicss:
            if externalInspectionSectionForElectronics['time_pod'] in list(externalInspectionSectionForElectronics.keys()):
                externalInspectionSectionForElectronics_result[externalInspectionSectionForElectronics['time_pod']] += externalInspectionSectionForElectronics['yield_d']
            else:
                externalInspectionSectionForElectronics_result[externalInspectionSectionForElectronics['time_pod']] = externalInspectionSectionForElectronics['yield_d']

        externalInspectionSectionForElectronics_resultList = []
        for key in list(externalInspectionSectionForElectronics_result.keys()):
            data = {
                "name": key,
                "value": externalInspectionSectionForElectronics_result[key]
            }
            externalInspectionSectionForElectronics_resultList.append(data)

        testSectionForElectronics_result = {}
        for testSectionForElectronics in testSectionForElectronicss:
            if testSectionForElectronics['time_pod'] in list(testSectionForElectronics.keys()):
                testSectionForElectronics_result[testSectionForElectronics['time_pod']] += testSectionForElectronics['yield_d']
            else:
                testSectionForElectronics_result[testSectionForElectronics['time_pod']] = testSectionForElectronics['yield_d']

        testSectionForElectronics_resultList = []
        for key in list(testSectionForElectronics_result.keys()):
            data = {
                "name": key,
                "value": testSectionForElectronics_result[key]
            }
            testSectionForElectronics_resultList.append(data)

        resultData = {
            "12车间PCB板外检工段": externalInspectionSectionForPCB_resultList,
            "成型车间SP外检工段": externalInspectionSectionForSP_resultList,
            "电子车间外检工段": externalInspectionSectionForElectronics_resultList,
            "电子车间测试工段": testSectionForElectronics_resultList
        }

        data = {
            "code": 200,
            "data": resultData,
            "msg": ""
        }

        return JsonResponse(data)


class centerRight01View(APIView):
    def get(self,request):
        externalInspectionSectionForPCBs = ExternalInspectionSectionForPCB.objects.exclude(yield_d=0).values("date")\
            .annotate(false_welding=Sum("false_welding"),continuous_tin=Sum("continuous_tin"),deviation=Sum("deviation"),
                      broken_copper=Sum("broken_copper"),tin_beads=Sum("tin_beads"),fuzzing=Sum("fuzzing"),
                      reverse_line=Sum("reverse_line"))\
            .values("false_welding","continuous_tin",
                    "deviation","broken_copper","tin_beads",
                    "fuzzing","reverse_line","date").order_by("date")

        date = []
        false_welding = []
        continuous_tin = []
        deviation = []
        broken_copper = []
        tin_beads = []
        fuzzing = []
        reverse_line = []
        for externalInspectionSectionForPCB in externalInspectionSectionForPCBs:
            for key in list(externalInspectionSectionForPCB.keys()):
                if externalInspectionSectionForPCB[key] == None:
                    externalInspectionSectionForPCB[key] = 0

            date.append(externalInspectionSectionForPCB['date'])
            false_welding.append(externalInspectionSectionForPCB['false_welding'])
            continuous_tin.append(externalInspectionSectionForPCB['continuous_tin'])
            deviation.append(externalInspectionSectionForPCB['deviation'])
            broken_copper.append(externalInspectionSectionForPCB['broken_copper'])
            tin_beads.append(externalInspectionSectionForPCB['tin_beads'])
            fuzzing.append(externalInspectionSectionForPCB['fuzzing'])
            reverse_line.append(externalInspectionSectionForPCB['reverse_line'])

        resultData = {
            "date": date,
            "false_welding": false_welding,
            "continuous_tin": continuous_tin,
            "deviation": deviation,
            "broken_copper": broken_copper,
            "tin_beads": tin_beads,
            "fuzzing": fuzzing,
            "reverse_line": reverse_line,
        }

        data = {
            "code": 200,
            "data": resultData,
            "msg": ""
        }

        return JsonResponse(data)


class centerRight02View(APIView):
    def get(self, request):
        externalInspectionSectionForSPs = ExternalInspectionSectionForSP.objects.exclude(yield_d=0).values("date")\
            .annotate(material_grain=Sum("material_grain"),rubber_punching=Sum("rubber_punching"),lack_of_glue=Sum("lack_of_glue"),
                      dirty_seal=Sum("dirty_seal"),shrink=Sum("shrink"),leaky_line=Sum("leaky_line"),
                      crack=Sum("crack"),eye_of_needle=Sum("eye_of_needle"),variegated=Sum("variegated"),
                      line_pressing=Sum("line_pressing"),other=Sum("other"),clearance=Sum("clearance"))\
            .values("material_grain", "rubber_punching",
            "lack_of_glue", "dirty_seal", "shrink",
            "leaky_line", "crack","eye_of_needle","variegated",
            "line_pressing","other","clearance","date").order_by("date")

        date = []
        material_grain = []
        rubber_punching = []
        lack_of_glue = []
        dirty_seal = []
        shrink = []
        leaky_line = []
        crack = []
        eye_of_needle = []
        variegated = []
        line_pressing = []
        other = []
        clearance = []
        for externalInspectionSectionForSP in externalInspectionSectionForSPs:
            for key in list(externalInspectionSectionForSP.keys()):
                if externalInspectionSectionForSP[key] == None:
                    externalInspectionSectionForSP[key] = 0

            date.append(externalInspectionSectionForSP['date'])
            material_grain.append(externalInspectionSectionForSP['material_grain'])
            rubber_punching.append(externalInspectionSectionForSP['rubber_punching'])
            lack_of_glue.append(externalInspectionSectionForSP['lack_of_glue'])
            dirty_seal.append(externalInspectionSectionForSP['dirty_seal'])
            shrink.append(externalInspectionSectionForSP['shrink'])
            leaky_line.append(externalInspectionSectionForSP['leaky_line'])
            crack.append(externalInspectionSectionForSP['crack'])
            eye_of_needle.append(externalInspectionSectionForSP['eye_of_needle'])
            variegated.append(externalInspectionSectionForSP['variegated'])
            line_pressing.append(externalInspectionSectionForSP['line_pressing'])
            other.append(externalInspectionSectionForSP['other'])
            clearance.append(externalInspectionSectionForSP['clearance'])

        resultData = {
            "date": date,
            "material_grain": material_grain,
            "rubber_punching": rubber_punching,
            "lack_of_glue": lack_of_glue,
            "dirty_seal": dirty_seal,
            "shrink": shrink,
            "leaky_line": leaky_line,
            "crack": crack,
            "eye_of_needle": eye_of_needle,
            "variegated": variegated,
            "line_pressing": line_pressing,
            "other": other,
            "clearance": clearance,
        }

        data = {
            "code": 200,
            "data": resultData,
            "msg": ""
        }

        return JsonResponse(data)


class centerRight03View(APIView):
    def get(self, request):
        externalInspectionSectionForElectronicss = ExternalInspectionSectionForElectronics.objects.exclude(yield_d=0).values("date")\
            .annotate(PCB_board=Sum("PCB_board"),wire_rod=Sum("wire_rod"),SP=Sum("SP"),
                      air_traffic_control=Sum("air_traffic_control"),gluing=Sum("gluing"),f_2C=Sum("f_2C"),
                      f_5C=Sum("f_5C"),f_2C_leakage=Sum("f_2C_leakage"),f_5C_leakage=Sum("f_5C_leakage"),
                      core_wire=Sum("core_wire"),size=Sum("size"))\
            .values("PCB_board", "wire_rod",
            "SP", "air_traffic_control", "gluing",
            "f_2C", "f_5C","f_2C_leakage","f_5C_leakage",
            "core_wire","size","date").order_by("date")

        date = []
        PCB_board = []
        wire_rod = []
        SP = []
        air_traffic_control = []
        gluing = []
        f_2C = []
        f_5C = []
        f_2C_leakage = []
        f_5C_leakage = []
        core_wire = []
        size = []
        for externalInspectionSectionForElectronics in externalInspectionSectionForElectronicss:
            for key in list(externalInspectionSectionForElectronics.keys()):
                if externalInspectionSectionForElectronics[key] == None:
                    externalInspectionSectionForElectronics[key] = 0

            date.append(externalInspectionSectionForElectronics['date'])
            PCB_board.append(externalInspectionSectionForElectronics['PCB_board'])
            wire_rod.append(externalInspectionSectionForElectronics['wire_rod'])
            SP.append(externalInspectionSectionForElectronics['SP'])
            air_traffic_control.append(externalInspectionSectionForElectronics['air_traffic_control'])
            gluing.append(externalInspectionSectionForElectronics['gluing'])
            f_2C.append(externalInspectionSectionForElectronics['f_2C'])
            f_5C.append(externalInspectionSectionForElectronics['f_5C'])
            f_2C_leakage.append(externalInspectionSectionForElectronics['f_2C_leakage'])
            f_5C_leakage.append(externalInspectionSectionForElectronics['f_5C_leakage'])
            core_wire.append(externalInspectionSectionForElectronics['core_wire'])
            size.append(externalInspectionSectionForElectronics['size'])

        resultData = {
            "date": date,
            "PCB_board": PCB_board,
            "wire_rod": wire_rod,
            "SP": SP,
            "air_traffic_control": air_traffic_control,
            "gluing": gluing,
            "f_2C": f_2C,
            "f_5C": f_5C,
            "f_2C_leakage": f_2C_leakage,
            "f_5C_leakage": f_5C_leakage,
            "core_wire": core_wire,
            "size": size,
        }

        data = {
            "code": 200,
            "data": resultData,
            "msg": ""
        }

        return JsonResponse(data)


class centerRight04View(APIView):
    def get(self,request):
        testSectionForElectronicss = TestSectionForElectronics.objects.exclude(yield_d=0).values("date")\
            .annotate(short_circuit=Sum("short_circuit"),open_circuit=Sum("open_circuit"),insulation=Sum("insulation"),
                      copper_wire_mix_and_match=Sum("copper_wire_mix_and_match"))\
            .values("short_circuit","open_circuit",
                    "insulation","copper_wire_mix_and_match","date").order_by("date")

        date = []
        short_circuit = []
        open_circuit = []
        insulation = []
        copper_wire_mix_and_match = []
        for testSectionForElectronics in testSectionForElectronicss:
            for key in list(testSectionForElectronics.keys()):
                if testSectionForElectronics[key] == None:
                    testSectionForElectronics[key] = 0

            date.append(testSectionForElectronics['date'])
            short_circuit.append(testSectionForElectronics['short_circuit'])
            open_circuit.append(testSectionForElectronics['open_circuit'])
            insulation.append(testSectionForElectronics['insulation'])
            copper_wire_mix_and_match.append(testSectionForElectronics['copper_wire_mix_and_match'])

        resultData = {
            "date": date,
            "short_circuit": short_circuit,
            "open_circuit": open_circuit,
            "insulation": insulation,
            "copper_wire_mix_and_match": copper_wire_mix_and_match,
        }

        data = {
            "code": 200,
            "data": resultData,
            "msg": ""
        }

        return JsonResponse(data)
