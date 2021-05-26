from django.db import models

# Create your models here.

#게시글 기본 틀 설정
class StrategyArticle(models.Model):
    title       = models.CharField(max_length=120)
    content     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    strategy_num= models.IntegerField()
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.strategy_num)