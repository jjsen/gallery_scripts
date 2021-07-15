#!/usr/bin/env python3

#env_set.py can create, update or run project

import argparse, os, sys, subprocess, errno

def clone():
  try:
    print("Invoke command: git init")
    subprocess.run(["git", "init"])
  except:
    print("Can't init")
  try:
    print("Clone Front-end")
    subprocess.run(["git", "clone", "https://github.com/AndriyMazuryk/gallery_fe.git"])
  except:
    print("ERROR: Unlucky clone of Front-end")
  try:
    print("Clone Backend")
    subprocess.run(["git", "clone", "https://github.com/jjsen/gallery_be.git"])
  except:
    print("ERR: Unlucky clone of Backend")

def update():
  print('code to be inserted')


def run():
  print('Docker-compose startup:')


if __name__=='__main__':
    parser = argparse.ArgumentParser(description='clone, update or run a project')
    parser.add_argument('command', help='Commands to run: clone, update or run')
    args = parser.parse_args()
    
    if args.command in ['clone', 'CLONE']:
        print('Clone the project')
        clone()

    if args.command in ['update', 'UPDATE']:
        print('Update the project')
        update()

    if args.command in ['run', 'RUN']:
        print('Start the project')
        run()


