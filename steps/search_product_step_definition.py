from behave import given, when, then
import os
import sys

@given(u'I launch browser on desktop PC')
def step_impl(context):
	print('Desktop browser is launched')

@when(u'I search for the droids')
def step_impl(context):
	print('Backend system still searching for your droids')

@then(u'Relevant search results should be shown')
def step_impl(context):
	print('Here are droids you are looking for')
