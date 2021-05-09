from django.db import models

# Create your models here.

class ExternalInspectionSectionForPCB(models.Model):
    time_pod = models.CharField(max_length=255,verbose_name="时间")
    time_interval = models.CharField(max_length=255,verbose_name="时间间隔")
    false_welding = models.IntegerField(verbose_name="假焊",null=True)
    continuous_tin = models.IntegerField(verbose_name="连锡",null=True)
    deviation = models.IntegerField(verbose_name="偏位",null=True)
    broken_copper = models.IntegerField(verbose_name="断铜",null=True)
    tin_beads = models.IntegerField(verbose_name="锡珠",null=True)
    fuzzing = models.IntegerField(verbose_name="起毛",null=True)
    reverse_line = models.IntegerField(verbose_name="反线",null=True)
    yield_d = models.IntegerField(verbose_name="产量",null=True)
    bad_quantity = models.IntegerField(verbose_name="不良数量",null=True)
    defective_rate = models.DecimalField(max_digits=5,decimal_places=4,verbose_name="不良率",null=True)
    remark = models.CharField(max_length=255,verbose_name="备注",null=True)
    d_class = models.CharField(max_length=255,verbose_name="班次",null=True)
    product_name = models.CharField(max_length=255,verbose_name="品名",null=True)
    date = models.CharField(max_length=255,verbose_name="日期",null=True)
    approval = models.CharField(max_length=255,verbose_name="核准",null=True)
    to_examine = models.CharField(max_length=255,verbose_name="审核",null=True)
    completed_by = models.CharField(max_length=255,verbose_name="填表人",null=True)
    sn = models.CharField(max_length=255,verbose_name="任务单号",null=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "12车间PCB板外检工段"
        verbose_name_plural = verbose_name
        db_table = "t_external_inspection_section_PCB"

class ExternalInspectionSectionForSP(models.Model):
    time_pod = models.CharField(max_length=255,verbose_name="时间")
    time_interval = models.CharField(max_length=255,verbose_name="时间间隔")
    material_grain = models.IntegerField(verbose_name="料纹",null=True)
    rubber_punching = models.IntegerField(verbose_name="冲胶",null=True)
    lack_of_glue = models.IntegerField(verbose_name="缺胶",null=True)
    dirty_seal = models.IntegerField(verbose_name="脏印",null=True)
    shrink = models.IntegerField(verbose_name="缩水",null=True)
    leaky_line = models.IntegerField(verbose_name="漏线",null=True)
    crack = models.IntegerField(verbose_name="开裂",null=True)
    eye_of_needle = models.IntegerField(verbose_name="针眼",null=True)
    variegated = models.IntegerField(verbose_name="杂色",null=True)
    line_pressing = models.IntegerField(verbose_name="压线",null=True)
    other = models.IntegerField(verbose_name="其它",null=True)
    clearance = models.IntegerField(verbose_name="间隙",null=True)
    yield_d = models.IntegerField(verbose_name="产量",null=True)
    bad_quantity = models.IntegerField(verbose_name="不良数量",null=True)
    defective_rate = models.DecimalField(max_digits=5,decimal_places=4,verbose_name="不良率",null=True)
    remark = models.CharField(max_length=255,verbose_name="备注",null=True)
    d_class = models.CharField(max_length=255, verbose_name="班次", null=True)
    product_name = models.CharField(max_length=255, verbose_name="品名", null=True)
    date = models.CharField(max_length=255, verbose_name="日期", null=True)
    approval = models.CharField(max_length=255, verbose_name="核准", null=True)
    to_examine = models.CharField(max_length=255, verbose_name="审核", null=True)
    completed_by = models.CharField(max_length=255, verbose_name="填表人", null=True)
    sn = models.CharField(max_length=255, verbose_name="任务单号", null=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "成型车间SP外检工段"
        verbose_name_plural = verbose_name
        db_table = "t_external_inspection_section_SP"

class ExternalInspectionSectionForElectronics(models.Model):
    time_pod = models.CharField(max_length=255,verbose_name="时间")
    time_interval = models.CharField(max_length=255,verbose_name="时间间隔")
    PCB_board = models.IntegerField(verbose_name="PCB板",null=True)
    wire_rod = models.IntegerField(verbose_name="线材",null=True)
    SP = models.IntegerField(verbose_name="SP",null=True)
    air_traffic_control = models.IntegerField(verbose_name="空管",null=True)
    gluing = models.IntegerField(verbose_name="沾胶",null=True)
    f_2C = models.IntegerField(verbose_name="2C",null=True)
    f_5C = models.IntegerField(verbose_name="5C",null=True)
    f_2C_leakage = models.IntegerField(verbose_name="2C漏沾",null=True)
    f_5C_leakage = models.IntegerField(verbose_name="5C漏沾",null=True)
    core_wire = models.IntegerField(verbose_name="芯线",null=True)
    size = models.IntegerField(verbose_name="尺寸",null=True)
    yield_d = models.IntegerField(verbose_name="产量",null=True)
    bad_quantity = models.IntegerField(verbose_name="不良数量",null=True)
    defective_rate = models.DecimalField(max_digits=5,decimal_places=4,verbose_name="不良率",null=True)
    remark = models.CharField(max_length=255,verbose_name="备注",null=True)
    d_class = models.CharField(max_length=255, verbose_name="班次", null=True)
    product_name = models.CharField(max_length=255, verbose_name="品名", null=True)
    date = models.CharField(max_length=255, verbose_name="日期", null=True)
    approval = models.CharField(max_length=255, verbose_name="核准", null=True)
    to_examine = models.CharField(max_length=255, verbose_name="审核", null=True)
    completed_by = models.CharField(max_length=255, verbose_name="填表人", null=True)
    sn = models.CharField(max_length=255, verbose_name="任务单号", null=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "电子车间外检工段"
        verbose_name_plural = verbose_name
        db_table = "t_external_inspection_section_electronics"

class TestSectionForElectronics(models.Model):
    time_pod = models.CharField(max_length=255,verbose_name="时间")
    time_interval = models.CharField(max_length=255,verbose_name="时间间隔")
    short_circuit = models.IntegerField(verbose_name="短路",null=True)
    open_circuit = models.IntegerField(verbose_name="断路",null=True)
    insulation = models.IntegerField(verbose_name="绝缘",null=True)
    copper_wire_mix_and_match = models.IntegerField(verbose_name="铜丝混搭",null=True)
    yield_d = models.IntegerField(verbose_name="产量",null=True)
    bad_quantity = models.IntegerField(verbose_name="不良数量",null=True)
    defective_rate = models.DecimalField(max_digits=5,decimal_places=4,verbose_name="不良率",null=True)
    remark = models.CharField(max_length=255,verbose_name="备注",null=True)
    d_class = models.CharField(max_length=255, verbose_name="班次", null=True)
    product_name = models.CharField(max_length=255, verbose_name="品名", null=True)
    date = models.CharField(max_length=255, verbose_name="日期", null=True)
    approval = models.CharField(max_length=255, verbose_name="核准", null=True)
    to_examine = models.CharField(max_length=255, verbose_name="审核", null=True)
    completed_by = models.CharField(max_length=255, verbose_name="填表人", null=True)
    sn = models.CharField(max_length=255, verbose_name="任务单号", null=True)
    objects = models.Manager()

    class Meta:
        verbose_name = "电子车间测试工段"
        verbose_name_plural = verbose_name
        db_table = "t_test_section_electronics"