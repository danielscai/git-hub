#!/usr/bin/python 

import copy

target_dict={
        'vm':{
            'hi':'hello',
            'world':'yes',
            'tt':[{'1':'x'}],
            }
        }

needed_checked={
        'vm':{
            'hi':'hello',
            'world':'yes',
            'tt':[{'2':'x'}],
            'world1':'yes'}
        }


def check_json(target_dict,needed_checked,parent=[]):
    current_parent=copy.deepcopy(parent)
    check_type(target_dict,needed_checked,current_parent)
    if is_list(target_dict):
        for items in needed_checked:
            check_json(target_dict[0],items,current_parent)
    elif is_dict(target_dict):
        check=compare_root_key(target_dict,needed_checked)
        if check:
            exception_str="Missing Mandatory Key :  " + \
                    concat_parent(current_parent + list(check))
            raise Exception,exception_str

        for key in target_dict:
            current_parent.append(key)
            check_json(target_dict[key],needed_checked[key],current_parent)
    return True

def check_type(source,exp,parent):
    should_type=type(source)
    exp_type=type(exp)
    if should_type != exp_type:
        exception_str="Type Error: %s should be %s  " % \
                    (concat_parent(parent) , should_type.__name__)
        raise Exception,exception_str

def is_dict(source):
    should_type=type(source)
    if should_type == dict:
        return True
    return False

def is_list(source):
    should_type=type(source)
    if should_type == list:
        return True
    return False


def concat_parent(parent):
    return '->'.join(["'%s'" % x for x in  parent])

def compare_root_key(target_dict,needed_checked):
    a1=set(target_dict)
    a2=set(needed_checked)
    if a1 <= a2:
        return None
    return a1 - a2

try:
    check_json(target_dict,needed_checked)
except Exception,e:
    print e
