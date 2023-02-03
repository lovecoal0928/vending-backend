from django.db import models

class Drinks(models.Model):
    """ドリンク一覧モデル"""
    
    id = models.AutoField(primary_key=True)
    name = models.CharField("ドリンク名", max_length=50)
    price = models.IntegerField("価格")
    src = models.CharField(verbose_name="イメージ画像", max_length=100)
    hot_flag = models.BooleanField("温度フラグ", default=False)
    soda_flag = models.BooleanField("炭酸フラグ", default=False)
    created_at = models.DateTimeField(verbose_name="追加日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    
    def __str__(self):
        return self.name
