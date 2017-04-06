from django import template

register = template.Library()

@register.filter
def addstr(str1, str2):
	''' concatinates two strings '''
	return str(str1) + str(str2)