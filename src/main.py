#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from process import create_process
from read_write_email import read_email
from hexo import hexo_generate_and_deploy

def update_blog_post_callback():

    """
    update blog post from email callback function
    """

    read_email()
    hexo_generate_and_deploy()

def main():

    """
    main entrance for the whole project
    """

    create_process("./server_config.json", update_blog_post_callback)

if __name__ == "__main__":

    """
    run the project
    """

    main()
