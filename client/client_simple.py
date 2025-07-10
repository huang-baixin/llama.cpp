# -*- coding: utf-8 -*-
import requests as rq
import json as js
import base64
import time
import pdb
import re
from thefuzz import process
import time
import requests


def test_completion(prompt):
    # result = rq.post('http://localhost:8080/completion', data = js.dumps({
    result = rq.post('http://localhost:8080/completion', data = js.dumps({
    "prompt":prompt,
}))
    return result

def eval_subject():
    prompt_str = 'hello'
    result = test_completion(prompt_str)
    
def main():
    eval_subject()

if __name__=="__main__":
    main()