#!/usr/bin/env python3

#env_set.py can create, update or run project

import argparse, os, sys, subprocess, errno

def clone():
  try:
    print("Invoke command: git init")
    subprocess.run(["git", "init"])
  except Exception as error:
    print(error)
    sys.exit(1)
  try:
    print("Clone Front-end")
    subprocess.run(["git", "clone", "https://github.com/AndriyMazuryk/gallery_fe.git"])
  except Exception as error:
    print(error)
    sys.exit(1)
  try:
    print("Invoke command: git checkout dev for FE")
    subprocess.run(["git", "checkout", "dev"], cwd="./gallery_fe")
  except Exception as error:
    print(error)
    sys.exit(1)
  try:
    print("Clone Backend")
    subprocess.run(["git", "clone", "https://github.com/jjsen/gallery_be.git"])
  except Exception as error:
    print(error)
    sys.exit(1)
  try:
    print("Invoke command: git checkout dev for BE")
    subprocess.run(["git", "checkout", "dev"], cwd="./gallery_be")
  except Exception as error:
    print(error)
    sys.exit(1)


def update():
  print('code to be inserted')


def run():
  try: 
    print("Invoke command: docker-compose up")
    subprocess.run(["docker-compose", "up"])
  except Exception as error:
    print(error)
    sys.exit(1)


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


