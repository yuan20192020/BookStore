from django import forms

from .. import models

class BookForm(forms.Form):
	
	title = forms.CharField(max_length = 4)

	def __init__(self, instance = None, *args, **kwargs):
		self.instance = instance
		super(BookForm, self).__init__( *args, **kwargs)

	def save(self):
		#如果instance不为空，那么是views.py里的put方法调用的
		#更新请求要先找到这本书，所以上面多传一个参数instance
		#is_valid()只校验数据。
		#cleaned_data是个字典，传过来的新数据。用items一个一个的键值对取出来
		#把新的key value赋值给instance。通过反射的形式，通过字符串形式设置新值
		#保存新的值

		if self.instance is not None:
			for key, value in self.cleaned_data.items():
				setattr(self.instance, key, value)

			self.instance.save()
			return self.instance

		#如果instance为空，那么是views.py里的post方法调用的，直接创建
		return models.Book.objects.create(**self.cleaned_data)		
