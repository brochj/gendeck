# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 09:16:41 2020

@author: broch
"""


from bing_image_downloader import downloader

query_string = "dog"

filters = '+filterui:imagesize-medium+filterui:photo-photo+filterui:aspect-wide&form=IRFLTR&first=1'

downloader.download(query_string, limit=10,  output_dir='dataset', 
adult_filter_off=True, force_replace=False, timeout=60, filters=filters)